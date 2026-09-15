# 🌍 Language Learning App

A full-stack web application for learning **10 languages** with structured courses, flashcards, pronunciation, and progress tracking. Built with **Flask** and deployed with **Docker**.

**🔗 Live Demo:** [language-learning-app-8svd.onrender.com](https://language-learning-app-8svd.onrender.com)

---

## 📸 Screenshots

> _Add your screenshots here. See "How to add screenshots" below._

| Home | Courses | Dictionary |
|:---:|:---:|:---:|
| ![Home](docs/screenshots/home.png) | ![Courses](docs/screenshots/courses.png) | ![Dictionary](docs/screenshots/dictionary.png) |

---

## ✨ Features

### 🎓 Learning content
- **10 languages**: English, Russian, Romanian, Ukrainian, Chinese, Spanish, French, German, Italian, Japanese
- **20+ structured courses**, including:
  - **Chinese**: HSK 1–6
  - **English**: IELTS, TOEFL, Cambridge B2/C1
  - **French**: DELF A1/A2/B1
  - **German**: Goethe A1/A2
  - **Spanish**: DELE A1/A2
  - **Japanese**: JLPT N5/N4
  - And more
- **Beginner lessons** grouped by category (Everyday Life, Exam Prep, Travel, Business, etc.)

### 🔊 Pronunciation & scripts
- **Text-to-speech** for every word via the browser's `speechSynthesis` API
- **Online TTS fallback** (Baidu + Google) for languages not installed locally
- **Pinyin** for Chinese words
- **Romaji** for Japanese words

### 🧠 Personal learning
- **User accounts** — register, log in, and keep your own flashcards
- **Flashcard system** — add words manually or from the built-in dictionary
- **Quiz mode** — practise translations with auto-marking
- **Statistics** — track how many words you've learned

### 🌐 Interface
- **Multilingual UI** — the whole interface can be switched between 10 languages
- **Auto-switch** — opening a course automatically sets the target and translation languages
- **Dark / light theme** with a single click
- **Responsive design** that works on desktop and mobile

### 📚 Dictionary & Videos
- **Search across all courses** — find words in any language
- **Topic-based YouTube search** — for every course topic, one click opens a curated YouTube search
- **Video playlist** support for courses with verified playlists

---

## 🛠 Tech Stack

### Backend
- **Python 3.11**
- **Flask 3.0** — web framework
- **Flask-SQLAlchemy 3.1** — ORM
- **Flask-Migrate 4.0** — database migrations
- **SQLite** — database
- **Werkzeug** — password hashing
- **Gunicorn** — production WSGI server

### Frontend
- **Jinja2** — templating
- **HTML5 / CSS3** — responsive layout, dark/light theme
- **Vanilla JavaScript** — TTS, search, dynamic UI

### DevOps
- **Docker** — containerisation
- **Docker Compose** — local orchestration
- **Render** — cloud deployment
- **GitHub** — version control

---

## 🚀 Run Locally

### With Docker (recommended)

```bash
git clone https://github.com/Hickmanda/language-learning-app.git
cd language-learning-app
docker compose up --build
```

Open **http://127.0.0.1:5000** in your browser.

### Without Docker

```bash
git clone https://github.com/Hickmanda/language-learning-app.git
cd language-learning-app

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
flask db upgrade
python app.py
```

Open **http://127.0.0.1:5000**.

---

## 📖 How to Use

1. **Register** a new account (or log in).
2. **Explore** the **Dictionary** and **Courses** to find words.
3. **Add words** to your personal collection with one click.
4. **Practice** with **Quiz mode**.
5. **Track progress** on the **Stats** page.
6. Switch the interface language at any time in the top-right corner.

---

## 📁 Project Structure

```
language-learning-app/
├── app.py                  # Main Flask application
├── data/                   # Static content
│   ├── ui_translations.py  # UI strings in 10 languages
│   ├── word_bank.py        # Courses and vocabulary
│   └── lessons.py          # Categorised lessons
├── templates/              # Jinja2 templates
├── static/                 # CSS, images
├── migrations/             # Database migrations
├── Dockerfile              # Container definition
├── docker-compose.yml      # Local orchestration
├── entrypoint.sh           # Container startup script
└── requirements.txt        # Python dependencies
```

---

## 💡 What I Learned

This project was my first full-stack application and taught me:

- **Flask routing and blueprints** — building a multi-page web app
- **ORM and migrations** — modelling data with SQLAlchemy, evolving the schema with Flask-Migrate
- **User authentication** — sessions, password hashing, login-required decorators
- **Frontend templating** — Jinja2 inheritance, dynamic content
- **Multilingual interfaces** — managing translations across 10 languages
- **Docker** — writing a Dockerfile, working with containers
- **Cloud deployment** — taking a local project to a live URL with Render
- **Third-party APIs** — integrating browser TTS and online fallbacks

---

## 📝 License

This project is open-source and available for educational use.

---

## 📬 Contact

**Author:** Hickmanda
**GitHub:** [@Hickmanda](https://github.com/Hickmanda)