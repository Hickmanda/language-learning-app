# ============================================================
# IMPORTS
# ============================================================
from flask import (
    Flask, render_template, request, redirect, url_for, session,
    jsonify, Response, flash, g
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps
import random
import csv
import io
import os

from data.ui_translations import UI_TRANSLATIONS, LANGUAGES
from data.word_bank import COURSES, find_course, count_words, search_words
from data.lessons import LESSON_CATEGORIES

# ============================================================
# APP SETUP
# ============================================================
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

SPEECH_LANGS = {
    "en": "en-US", "ru": "ru-RU", "ro": "ro-RO", "uk": "uk-UA",
    "zh": "zh-CN", "es": "es-ES", "fr": "fr-FR", "de": "de-DE",
    "it": "it-IT", "ja": "ja-JP",
}

# ============================================================
# MODELS
# ============================================================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    cards = db.relationship(
        'Card', backref='owner', lazy=True, cascade='all, delete-orphan'
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    word = db.Column(db.String(200), nullable=False)
    translation = db.Column(db.String(200), nullable=False)
    language = db.Column(db.String(5), nullable=False)
    base_language = db.Column(db.String(5), nullable=False)
    known = db.Column(db.Boolean, default=False)

# ============================================================
# AUTH HELPERS
# ============================================================
def login_required(f):
    """Decorator: redirect to login page if user isn't authenticated."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please sign in first.', 'error')
            return redirect(url_for('login', next=request.path))
        return f(*args, **kwargs)
    return decorated


def current_user():
    """Return the current User object, or None."""
    uid = session.get('user_id')
    return db.session.get(User, uid) if uid else None

# ============================================================
# PROGRESS HELPER
# ============================================================
def course_progress(user, course):
    """
    Return (learned, total) for a user and a course.
    A word counts as 'learned' if the user has a Card with
    that word (in the course's target language) marked as known.
    """
    total = count_words(course)
    if not user:
        return (0, total)

    target = course.get('target_lang', 'en')
    course_words = set()
    for topic in course['topics']:
        for w in topic['words']:
            val = w.get(target)
            if val:
                course_words.add(val)

    learned_words = set()
    for card in user.cards:
        if card.language == target and card.known and card.word in course_words:
            learned_words.add(card.word)

    return (len(learned_words), total)

# ============================================================
# CONTEXT PROCESSOR
# ============================================================
@app.context_processor
def inject_globals():
    ui_lang    = session.get('ui_lang', 'en')
    learn_lang = session.get('learn_lang', 'en')
    base_lang  = session.get('base_lang', 'ru')
    theme      = session.get('theme', 'light')
    course_id  = session.get('course_id', 'all')

    return {
        't': UI_TRANSLATIONS.get(ui_lang, UI_TRANSLATIONS['en']),
        'ui_lang': ui_lang,
        'learn_lang': learn_lang,
        'base_lang': base_lang,
        'theme': theme,
        'course_id': course_id,
        'LANGUAGES': LANGUAGES,
        'COURSES': COURSES,
        'SPEECH_LANGS': SPEECH_LANGS,
        'user': current_user(),
    }

# ============================================================
# AUTH ROUTES
# ============================================================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email    = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm  = request.form.get('confirm', '')

        errors = []
        if len(username) < 3:
            errors.append('Username must be at least 3 characters.')
        if '@' not in email:
            errors.append('Please enter a valid email.')
        if len(password) < 6:
            errors.append('Password must be at least 6 characters.')
        if password != confirm:
            errors.append('Passwords do not match.')
        if User.query.filter_by(username=username).first():
            errors.append('Username is already taken.')
        if User.query.filter_by(email=email).first():
            errors.append('Email is already registered.')

        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('register.html')

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id
        flash(f'Welcome, {user.username}!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('index'))

    if request.method == 'POST':
        login_value = request.form.get('login', '').strip()
        password    = request.form.get('password', '')

        user = User.query.filter(
            (User.username == login_value) | (User.email == login_value.lower())
        ).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            flash(f'Welcome back, {user.username}!', 'success')
            next_url = request.args.get('next') or url_for('index')
            return redirect(next_url)

        flash('Invalid username or password.', 'error')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been signed out.', 'success')
    return redirect(url_for('index'))

# ============================================================
# SETTINGS ROUTES
# ============================================================
@app.route('/set_ui_lang/<code>')
def set_ui_lang(code):
    if code in LANGUAGES:
        session['ui_lang'] = code
        session['base_lang'] = code
    return redirect(request.referrer or url_for('index'))

@app.route('/set_learn_lang/<code>')
def set_learn_lang(code):
    if code in LANGUAGES:
        session['learn_lang'] = code
    return redirect(request.referrer or url_for('index'))

@app.route('/set_base_lang/<code>')
def set_base_lang(code):
    if code in LANGUAGES:
        session['base_lang'] = code
    return redirect(request.referrer or url_for('index'))

@app.route('/set_course/<course_id>')
def set_course(course_id):
    session['course_id'] = course_id
    return redirect(request.referrer or url_for('dictionary'))

@app.route('/toggle_theme')
def toggle_theme():
    current = session.get('theme', 'light')
    session['theme'] = 'dark' if current == 'light' else 'light'
    return redirect(request.referrer or url_for('index'))

# ============================================================
# MAIN ROUTES
# ============================================================
@app.route('/')
def index():
    user = current_user()
    cards = []
    if user:
        cards = (Card.query
                 .filter_by(user_id=user.id)
                 .order_by(Card.id.desc())
                 .all())
    return render_template('index.html', cards=cards)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        db.session.add(Card(
            user_id=session['user_id'],
            word=request.form['word'].strip(),
            translation=request.form['translation'].strip(),
            language=request.form['language'],
            base_language=request.form['base_language'],
        ))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:card_id>', methods=['POST'])
@login_required
def delete_card(card_id):
    card = db.session.get(Card, card_id)
    if card and card.user_id == session['user_id']:
        db.session.delete(card)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    user = current_user()
    if request.method == 'POST':
        card_id = request.form.get('card_id')
        answer = request.form.get('answer', '').strip().lower()
        card = db.session.get(Card, int(card_id)) if card_id else None
        if card and card.user_id == user.id and card.translation.lower() == answer:
            card.known = True
            db.session.commit()
            return redirect(url_for('quiz'))
        error = UI_TRANSLATIONS[session.get('ui_lang', 'en')]['wrong']
        return render_template('quiz.html', card=card, error=error)

    unknown = Card.query.filter_by(user_id=user.id, known=False).all()
    if not unknown:
        return render_template('quiz.html', card=None)
    return render_template('quiz.html', card=random.choice(unknown))

@app.route('/stats')
@login_required
def stats():
    user = current_user()
    total = Card.query.filter_by(user_id=user.id).count()
    known = Card.query.filter_by(user_id=user.id, known=True).count()
    return render_template('stats.html',
                           total=total, known=known, unknown=total - known)

# ============================================================
# DICTIONARY
# ============================================================
@app.route('/dictionary')
def dictionary():
    selected = session.get('course_id', 'all')
    query = request.args.get('q', '').strip()
    learn = session.get('learn_lang', 'en')
    base = session.get('base_lang', 'ru')

    if selected == 'all':
        courses_to_show = COURSES
    else:
        c = find_course(selected)
        courses_to_show = [c] if c else COURSES
        if c and c.get('target_lang'):
            session['learn_lang'] = c['target_lang']
            session['base_lang'] = session.get('ui_lang', 'en')
            learn = session['learn_lang']
            base = session['base_lang']

    results = None
    if query:
        results = search_words(query, learn, base)

    return render_template('dictionary.html',
                           courses=courses_to_show,
                           results=results,
                           query=query,
                           learn=learn,
                           base=base)

@app.route('/add_from_bank', methods=['POST'])
@login_required
def add_from_bank():
    user = current_user()
    word = request.form['word']
    translation = request.form['translation']
    language = request.form['language']
    base_language = request.form['base_language']

    existing = Card.query.filter_by(
        user_id=user.id, word=word,
        language=language, base_language=base_language
    ).first()

    if not existing:
        db.session.add(Card(
            user_id=user.id, word=word, translation=translation,
            language=language, base_language=base_language,
        ))
        db.session.commit()

    return redirect(request.referrer or url_for('dictionary'))

# ============================================================
# COURSES
# ============================================================
@app.route('/courses')
def courses():
    user = current_user()
    progress = {}
    for c in COURSES:
        progress[c['id']] = course_progress(user, c)
    return render_template('courses.html', courses=COURSES, progress=progress)

@app.route('/course/<course_id>')
def course_detail(course_id):
    course = find_course(course_id)
    if not course:
        return redirect(url_for('courses'))

    if course.get('target_lang'):
        session['learn_lang'] = course['target_lang']
    session['base_lang'] = session.get('ui_lang', 'en')

    user = current_user()
    learned, total = course_progress(user, course)

    return render_template('course_detail.html',
                           course=course,
                           learn=session.get('learn_lang', 'en'),
                           base=session.get('base_lang', 'ru'),
                           learned=learned, total=total)

@app.route('/course/<course_id>/videos')
def course_videos(course_id):
    course = find_course(course_id)
    if not course or not course.get('video_url'):
        return redirect(url_for('course_detail', course_id=course_id))
    return render_template('course_videos.html', course=course)

# ============================================================
# LESSONS
# ============================================================
@app.route('/lessons')
def lessons():
    return render_template('lessons.html', categories=LESSON_CATEGORIES)

@app.route('/lesson/<lesson_id>')
def lesson_detail(lesson_id):
    lesson = None
    for cat in LESSON_CATEGORIES:
        for l in cat['lessons']:
            if l['id'] == lesson_id:
                lesson = l
                break
        if lesson:
            break

    if not lesson:
        return redirect(url_for('lessons'))

    course = find_course(lesson['course_id'])
    if not course:
        return redirect(url_for('lessons'))

    topic = course['topics'][lesson['topic_index']]

    if course.get('target_lang'):
        session['learn_lang'] = course['target_lang']
    session['base_lang'] = session.get('ui_lang', 'en')

    return render_template('lesson_detail.html',
                           lesson=lesson, topic=topic,
                           learn=session.get('learn_lang', 'en'),
                           base=session.get('base_lang', 'ru'))

# ============================================================
# CSV EXPORT / IMPORT
# ============================================================
@app.route('/export/csv')
@login_required
def export_csv():
    user = current_user()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['word', 'translation', 'language', 'base_language', 'known'])
    for c in user.cards:
        writer.writerow([c.word, c.translation, c.language, c.base_language, c.known])

    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename=cards.csv'}
    )

@app.route('/import/csv', methods=['POST'])
@login_required
def import_csv():
    user = current_user()
    file = request.files.get('file')
    if not file or not file.filename:
        flash('Please choose a CSV file.', 'error')
        return redirect(url_for('index'))

    try:
        content = file.stream.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(content))
        count = 0
        for row in reader:
            if not row.get('word') or not row.get('translation'):
                continue
            lang = row.get('language', 'en').strip() or 'en'
            base = row.get('base_language', 'ru').strip() or 'ru'
            exists = Card.query.filter_by(
                user_id=user.id, word=row['word'],
                language=lang, base_language=base
            ).first()
            if exists:
                continue
            db.session.add(Card(
                user_id=user.id,
                word=row['word'].strip(),
                translation=row['translation'].strip(),
                language=lang, base_language=base,
                known=row.get('known', '').lower() in ('1', 'true', 'yes'),
            ))
            count += 1
        db.session.commit()
        flash(f'Imported {count} cards.', 'success')
    except Exception as e:
        flash(f'Import failed: {e}', 'error')

    return redirect(url_for('index'))

# ============================================================
# JSON API
# ============================================================
@app.route('/api/words')
def api_words():
    """
    Public JSON API.
    GET /api/words                       -> all courses' words
    GET /api/words?course=hsk1           -> words of one course
    GET /api/words?learn=fr&base=en      -> custom language pair
    """
    course_id = request.args.get('course')
    learn = request.args.get('learn', 'en')
    base  = request.args.get('base', 'ru')

    if course_id:
        c = find_course(course_id)
        courses = [c] if c else []
    else:
        courses = COURSES

    words = []
    for course in courses:
        if not course:
            continue
        for topic in course['topics']:
            for w in topic['words']:
                words.append({
                    'course': course['id'],
                    'topic': topic['topic'].get('en', ''),
                    'word': w.get(learn, ''),
                    'translation': w.get(base, ''),
                    'language': learn,
                    'base_language': base,
                })

    return jsonify({
        'count': len(words),
        'learn': learn,
        'base': base,
        'words': words,
    })

# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)