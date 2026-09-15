# ============================================================
# LESSONS — grouped by category.
# Each lesson references a course + topic by index.
# Language auto-switches when the lesson is opened,
# based on the course's target_lang.
# ============================================================

LESSON_CATEGORIES = [

    # --------------------------------------------------------
    # EVERYDAY LIFE
    # --------------------------------------------------------
    {
        "id": "everyday",
        "name": {"en": "Everyday Life", "ru": "Повседневная жизнь",
                 "ro": "Viața de zi cu zi", "uk": "Повсякденне життя",
                 "zh": "日常生活", "es": "Vida cotidiana",
                 "fr": "Vie quotidienne", "de": "Alltag",
                 "it": "Vita quotidiana", "ja": "日常生活"},
        "lessons": [
            {"id": "l_greet", "course_id": "general", "topic_index": 0, "level": "A1",
             "title": {"en": "Greetings", "ru": "Приветствия", "ro": "Saluturi",
                       "uk": "Привітання", "zh": "问候", "es": "Saludos",
                       "fr": "Salutations", "de": "Begrüßungen",
                       "it": "Saluti", "ja": "挨拶"}},
            {"id": "l_colors", "course_id": "general", "topic_index": 1, "level": "A1",
             "title": {"en": "Colors", "ru": "Цвета", "ro": "Culori",
                       "uk": "Кольори", "zh": "颜色", "es": "Colores",
                       "fr": "Couleurs", "de": "Farben",
                       "it": "Colori", "ja": "色"}},
            {"id": "l_numbers", "course_id": "general", "topic_index": 2, "level": "A1",
             "title": {"en": "Numbers", "ru": "Числа", "ro": "Numere",
                       "uk": "Числа", "zh": "数字", "es": "Números",
                       "fr": "Nombres", "de": "Zahlen",
                       "it": "Numeri", "ja": "数字"}},
        ],
    },

    # --------------------------------------------------------
    # ENGLISH EXAM PREP
    # --------------------------------------------------------
    {
        "id": "exam_prep",
        "name": {"en": "Exam Preparation", "ru": "Подготовка к экзаменам",
                 "ro": "Pregătire pentru examen", "uk": "Підготовка до іспитів",
                 "zh": "考试准备", "es": "Preparación de exámenes",
                 "fr": "Préparation d'examen", "de": "Prüfungsvorbereitung",
                 "it": "Preparazione esame", "ja": "試験対策"},
        "lessons": [
            {"id": "l_ielts_edu", "course_id": "ielts", "topic_index": 0, "level": "B2",
             "title": {"en": "IELTS: Education", "ru": "IELTS: Образование",
                       "ro": "IELTS: Educație", "uk": "IELTS: Освіта",
                       "zh": "雅思：教育", "es": "IELTS: Educación",
                       "fr": "IELTS : Éducation", "de": "IELTS: Bildung",
                       "it": "IELTS: Istruzione", "ja": "IELTS: 教育"}},
            {"id": "l_ielts_env", "course_id": "ielts", "topic_index": 1, "level": "B2",
             "title": {"en": "IELTS: Environment", "ru": "IELTS: Окружающая среда",
                       "ro": "IELTS: Mediu", "uk": "IELTS: Довкілля",
                       "zh": "雅思：环境", "es": "IELTS: Medio ambiente",
                       "fr": "IELTS : Environnement", "de": "IELTS: Umwelt",
                       "it": "IELTS: Ambiente", "ja": "IELTS: 環境"}},
            {"id": "l_ielts_tech", "course_id": "ielts", "topic_index": 2, "level": "B2",
             "title": {"en": "IELTS: Technology", "ru": "IELTS: Технологии",
                       "ro": "IELTS: Tehnologie", "uk": "IELTS: Технології",
                       "zh": "雅思：技术", "es": "IELTS: Tecnología",
                       "fr": "IELTS : Technologie", "de": "IELTS: Technologie",
                       "it": "IELTS: Tecnologia", "ja": "IELTS: 技術"}},
            {"id": "l_toefl_writ", "course_id": "toefl", "topic_index": 0, "level": "C1",
             "title": {"en": "TOEFL: Academic Writing", "ru": "TOEFL: Академическое письмо",
                       "ro": "TOEFL: Scriere academică", "uk": "TOEFL: Академічне письмо",
                       "zh": "托福：学术写作", "es": "TOEFL: Escritura académica",
                       "fr": "TOEFL : Écriture académique", "de": "TOEFL: Akademisches Schreiben",
                       "it": "TOEFL: Scrittura accademica", "ja": "TOEFL: アカデミック・ライティング"}},
            {"id": "l_toefl_sci", "course_id": "toefl", "topic_index": 1, "level": "C1",
             "title": {"en": "TOEFL: Science", "ru": "TOEFL: Наука",
                       "ro": "TOEFL: Știință", "uk": "TOEFL: Наука",
                       "zh": "托福：科学", "es": "TOEFL: Ciencia",
                       "fr": "TOEFL : Science", "de": "TOEFL: Wissenschaft",
                       "it": "TOEFL: Scienza", "ja": "TOEFL: 科学"}},
            {"id": "l_fce_life", "course_id": "cambridge_b2", "topic_index": 0, "level": "B2",
             "title": {"en": "FCE: Everyday Life", "ru": "FCE: Повседневная жизнь",
                       "ro": "FCE: Viața zilnică", "uk": "FCE: Повсякденне життя",
                       "zh": "FCE：日常生活", "es": "FCE: Vida cotidiana",
                       "fr": "FCE : Vie quotidienne", "de": "FCE: Alltag",
                       "it": "FCE: Vita quotidiana", "ja": "FCE: 日常生活"}},
            {"id": "l_fce_work", "course_id": "cambridge_b2", "topic_index": 1, "level": "B2",
             "title": {"en": "FCE: Work", "ru": "FCE: Работа",
                       "ro": "FCE: Muncă", "uk": "FCE: Робота",
                       "zh": "FCE：工作", "es": "FCE: Trabajo",
                       "fr": "FCE : Travail", "de": "FCE: Arbeit",
                       "it": "FCE: Lavoro", "ja": "FCE: 仕事"}},
            {"id": "l_cae_vocab", "course_id": "cambridge_c1", "topic_index": 0, "level": "C1",
             "title": {"en": "CAE: Advanced Vocabulary", "ru": "CAE: Продвинутая лексика",
                       "ro": "CAE: Vocabular avansat", "uk": "CAE: Просунута лексика",
                       "zh": "CAE：高级词汇", "es": "CAE: Vocabulario avanzado",
                       "fr": "CAE : Vocabulaire avancé", "de": "CAE: Fortgeschrittener Wortschatz",
                       "it": "CAE: Vocabolario avanzato", "ja": "CAE: 上級語彙"}},
        ],
    },

    # --------------------------------------------------------
    # CHINESE HSK
    # --------------------------------------------------------
    {
        "id": "chinese",
        "name": {"en": "Chinese HSK", "ru": "Китайский HSK", "ro": "Chineză HSK",
                 "uk": "Китайська HSK", "zh": "汉语 HSK", "es": "Chino HSK",
                 "fr": "Chinois HSK", "de": "Chinesisch HSK",
                 "it": "Cinese HSK", "ja": "中国語 HSK"},
        "lessons": [
            {"id": "l_hsk1_basic", "course_id": "hsk1", "topic_index": 0, "level": "HSK1",
             "title": {"en": "HSK 1: Basic Words", "ru": "HSK 1: Базовые слова",
                       "ro": "HSK 1: Cuvinte de bază", "uk": "HSK 1: Базові слова",
                       "zh": "HSK 1：基础词汇", "es": "HSK 1: Palabras básicas",
                       "fr": "HSK 1 : Mots de base", "de": "HSK 1: Grundwörter",
                       "it": "HSK 1: Parole di base", "ja": "HSK 1: 基本単語"}},
            {"id": "l_hsk2_actions", "course_id": "hsk2", "topic_index": 0, "level": "HSK2",
             "title": {"en": "HSK 2: Daily Actions", "ru": "HSK 2: Ежедневные действия",
                       "ro": "HSK 2: Acțiuni zilnice", "uk": "HSK 2: Щоденні дії",
                       "zh": "HSK 2：日常动作", "es": "HSK 2: Acciones diarias",
                       "fr": "HSK 2 : Actions quotidiennes", "de": "HSK 2: Tägliche Handlungen",
                       "it": "HSK 2: Azioni quotidiane", "ja": "HSK 2: 毎日の動作"}},
            {"id": "l_hsk3_feel", "course_id": "hsk3", "topic_index": 0, "level": "HSK3",
             "title": {"en": "HSK 3: Feelings", "ru": "HSK 3: Чувства",
                       "ro": "HSK 3: Sentimente", "uk": "HSK 3: Почуття",
                       "zh": "HSK 3：感觉", "es": "HSK 3: Sentimientos",
                       "fr": "HSK 3 : Sentiments", "de": "HSK 3: Gefühle",
                       "it": "HSK 3: Sentimenti", "ja": "HSK 3: 感情"}},
            {"id": "l_hsk4_soc", "course_id": "hsk4", "topic_index": 0, "level": "HSK4",
             "title": {"en": "HSK 4: Society", "ru": "HSK 4: Общество",
                       "ro": "HSK 4: Societate", "uk": "HSK 4: Суспільство",
                       "zh": "HSK 4：社会", "es": "HSK 4: Sociedad",
                       "fr": "HSK 4 : Société", "de": "HSK 4: Gesellschaft",
                       "it": "HSK 4: Società", "ja": "HSK 4: 社会"}},
            {"id": "l_hsk5_abs", "course_id": "hsk5", "topic_index": 0, "level": "HSK5",
             "title": {"en": "HSK 5: Abstract Concepts", "ru": "HSK 5: Абстрактные понятия",
                       "ro": "HSK 5: Concepte abstracte", "uk": "HSK 5: Абстрактні поняття",
                       "zh": "HSK 5：抽象概念", "es": "HSK 5: Conceptos abstractos",
                       "fr": "HSK 5 : Concepts abstraits", "de": "HSK 5: Abstrakte Konzepte",
                       "it": "HSK 5: Concetti astratti", "ja": "HSK 5: 抽象概念"}},
            {"id": "l_hsk6_adv", "course_id": "hsk6", "topic_index": 0, "level": "HSK6",
             "title": {"en": "HSK 6: Advanced Vocabulary", "ru": "HSK 6: Продвинутая лексика",
                       "ro": "HSK 6: Vocabular avansat", "uk": "HSK 6: Просунута лексика",
                       "zh": "HSK 6：高级词汇", "es": "HSK 6: Vocabulario avanzado",
                       "fr": "HSK 6 : Vocabulaire avancé", "de": "HSK 6: Fortgeschrittener Wortschatz",
                       "it": "HSK 6: Vocabolario avanzato", "ja": "HSK 6: 上級語彙"}},
        ],
    },

    # --------------------------------------------------------
    # FRENCH DELF
    # --------------------------------------------------------
    {
        "id": "french",
        "name": {"en": "French DELF", "ru": "Французский DELF", "ro": "Franceză DELF",
                 "uk": "Французька DELF", "zh": "法语 DELF", "es": "Francés DELF",
                 "fr": "Français DELF", "de": "Französisch DELF",
                 "it": "Francese DELF", "ja": "フランス語 DELF"},
        "lessons": [
            {"id": "l_delf_a1", "course_id": "delf_a1", "topic_index": 0, "level": "A1",
             "title": {"en": "DELF A1: Salutations", "ru": "DELF A1: Приветствия",
                       "ro": "DELF A1: Saluturi", "uk": "DELF A1: Привітання",
                       "zh": "DELF A1：问候", "es": "DELF A1: Saludos",
                       "fr": "DELF A1 : Salutations", "de": "DELF A1: Begrüßungen",
                       "it": "DELF A1: Saluti", "ja": "DELF A1: 挨拶"}},
            {"id": "l_delf_a2", "course_id": "delf_a2", "topic_index": 0, "level": "A2",
             "title": {"en": "DELF A2: Everyday Life", "ru": "DELF A2: Повседневная жизнь",
                       "ro": "DELF A2: Viața zilnică", "uk": "DELF A2: Повсякденне життя",
                       "zh": "DELF A2：日常生活", "es": "DELF A2: Vida cotidiana",
                       "fr": "DELF A2 : Vie quotidienne", "de": "DELF A2: Alltag",
                       "it": "DELF A2: Vita quotidiana", "ja": "DELF A2: 日常生活"}},
            {"id": "l_delf_b1", "course_id": "delf_b1", "topic_index": 0, "level": "B1",
             "title": {"en": "DELF B1: Opinions", "ru": "DELF B1: Мнения",
                       "ro": "DELF B1: Opinii", "uk": "DELF B1: Думки",
                       "zh": "DELF B1：观点", "es": "DELF B1: Opiniones",
                       "fr": "DELF B1 : Opinions", "de": "DELF B1: Meinungen",
                       "it": "DELF B1: Opinioni", "ja": "DELF B1: 意見"}},
        ],
    },

    # --------------------------------------------------------
    # GERMAN GOETHE
    # --------------------------------------------------------
    {
        "id": "german",
        "name": {"en": "German Goethe", "ru": "Немецкий Goethe", "ro": "Germană Goethe",
                 "uk": "Німецька Goethe", "zh": "德语 Goethe", "es": "Alemán Goethe",
                 "fr": "Allemand Goethe", "de": "Deutsch Goethe",
                 "it": "Tedesco Goethe", "ja": "ドイツ語 Goethe"},
        "lessons": [
            {"id": "l_goethe_a1", "course_id": "goethe_a1", "topic_index": 0, "level": "A1",
             "title": {"en": "Goethe A1: Greetings", "ru": "Goethe A1: Приветствия",
                       "ro": "Goethe A1: Saluturi", "uk": "Goethe A1: Привітання",
                       "zh": "Goethe A1：问候", "es": "Goethe A1: Saludos",
                       "fr": "Goethe A1 : Salutations", "de": "Goethe A1: Begrüßungen",
                       "it": "Goethe A1: Saluti", "ja": "Goethe A1: 挨拶"}},
            {"id": "l_goethe_a2", "course_id": "goethe_a2", "topic_index": 0, "level": "A2",
             "title": {"en": "Goethe A2: Daily Life", "ru": "Goethe A2: Повседневная жизнь",
                       "ro": "Goethe A2: Viața zilnică", "uk": "Goethe A2: Повсякденне життя",
                       "zh": "Goethe A2：日常生活", "es": "Goethe A2: Vida diaria",
                       "fr": "Goethe A2 : Vie quotidienne", "de": "Goethe A2: Alltagsleben",
                       "it": "Goethe A2: Vita quotidiana", "ja": "Goethe A2: 日常生活"}},
        ],
    },

    # --------------------------------------------------------
    # SPANISH DELE
    # --------------------------------------------------------
    {
        "id": "spanish",
        "name": {"en": "Spanish DELE", "ru": "Испанский DELE", "ro": "Spaniolă DELE",
                 "uk": "Іспанська DELE", "zh": "西班牙语 DELE", "es": "Español DELE",
                 "fr": "Espagnol DELE", "de": "Spanisch DELE",
                 "it": "Spagnolo DELE", "ja": "スペイン語 DELE"},
        "lessons": [
            {"id": "l_dele_a1", "course_id": "dele_a1", "topic_index": 0, "level": "A1",
             "title": {"en": "DELE A1: Greetings", "ru": "DELE A1: Приветствия",
                       "ro": "DELE A1: Saluturi", "uk": "DELE A1: Привітання",
                       "zh": "DELE A1：问候", "es": "DELE A1: Saludos",
                       "fr": "DELE A1 : Salutations", "de": "DELE A1: Begrüßungen",
                       "it": "DELE A1: Saluti", "ja": "DELE A1: 挨拶"}},
            {"id": "l_dele_a2", "course_id": "dele_a2", "topic_index": 0, "level": "A2",
             "title": {"en": "DELE A2: Everyday Verbs", "ru": "DELE A2: Повседневные глаголы",
                       "ro": "DELE A2: Verbe zilnice", "uk": "DELE A2: Щоденні дієслова",
                       "zh": "DELE A2：日常动词", "es": "DELE A2: Verbos cotidianos",
                       "fr": "DELE A2 : Verbes quotidiens", "de": "DELE A2: Alltagsverben",
                       "it": "DELE A2: Verbi quotidiani", "ja": "DELE A2: 日常動詞"}},
        ],
    },

    # --------------------------------------------------------
    # JAPANESE JLPT
    # --------------------------------------------------------
    {
        "id": "japanese",
        "name": {"en": "Japanese JLPT", "ru": "Японский JLPT", "ro": "Japoneză JLPT",
                 "uk": "Японська JLPT", "zh": "日语 JLPT", "es": "Japonés JLPT",
                 "fr": "Japonais JLPT", "de": "Japanisch JLPT",
                 "it": "Giapponese JLPT", "ja": "日本語 JLPT"},
        "lessons": [
            {"id": "l_jlpt_n5", "course_id": "jlpt_n5", "topic_index": 0, "level": "N5",
             "title": {"en": "JLPT N5: Greetings", "ru": "JLPT N5: Приветствия",
                       "ro": "JLPT N5: Saluturi", "uk": "JLPT N5: Привітання",
                       "zh": "JLPT N5：问候", "es": "JLPT N5: Saludos",
                       "fr": "JLPT N5 : Salutations", "de": "JLPT N5: Begrüßungen",
                       "it": "JLPT N5: Saluti", "ja": "JLPT N5: 挨拶"}},
            {"id": "l_jlpt_n4", "course_id": "jlpt_n4", "topic_index": 0, "level": "N4",
             "title": {"en": "JLPT N4: Common Expressions", "ru": "JLPT N4: Частые выражения",
                       "ro": "JLPT N4: Expresii comune", "uk": "JLPT N4: Часті вирази",
                       "zh": "JLPT N4：常用表达", "es": "JLPT N4: Expresiones comunes",
                       "fr": "JLPT N4 : Expressions courantes", "de": "JLPT N4: Häufige Ausdrücke",
                       "it": "JLPT N4: Espressioni comuni", "ja": "JLPT N4: よく使う表現"}},
        ],
    },

    # --------------------------------------------------------
    # ITALIAN CILS
    # --------------------------------------------------------
    {
        "id": "italian",
        "name": {"en": "Italian CILS", "ru": "Итальянский CILS", "ro": "Italiană CILS",
                 "uk": "Італійська CILS", "zh": "意大利语 CILS", "es": "Italiano CILS",
                 "fr": "Italien CILS", "de": "Italienisch CILS",
                 "it": "Italiano CILS", "ja": "イタリア語 CILS"},
        "lessons": [
            {"id": "l_cils_a1", "course_id": "cils_a1", "topic_index": 0, "level": "A1",
             "title": {"en": "CILS A1: First Words", "ru": "CILS A1: Первые слова",
                       "ro": "CILS A1: Primele cuvinte", "uk": "CILS A1: Перші слова",
                       "zh": "CILS A1：第一批单词", "es": "CILS A1: Primeras palabras",
                       "fr": "CILS A1 : Premiers mots", "de": "CILS A1: Erste Wörter",
                       "it": "CILS A1: Prime parole", "ja": "CILS A1: 最初の単語"}},
        ],
    },

    # --------------------------------------------------------
    # ROMANIAN / UKRAINIAN / RUSSIAN — Basics
    # --------------------------------------------------------
    {
        "id": "slavic_romance",
        "name": {"en": "Romanian / Ukrainian / Russian",
                 "ru": "Румынский / Украинский / Русский",
                 "ro": "Română / Ucraineană / Rusă",
                 "uk": "Румунська / Українська / Російська",
                 "zh": "罗马尼亚语 / 乌克兰语 / 俄语",
                 "es": "Rumano / Ucraniano / Ruso",
                 "fr": "Roumain / Ukrainien / Russe",
                 "de": "Rumänisch / Ukrainisch / Russisch",
                 "it": "Rumeno / Ucraino / Russo",
                 "ja": "ルーマニア語 / ウクライナ語 / ロシア語"},
        "lessons": [
            {"id": "l_rom_basic", "course_id": "romanian_basics", "topic_index": 0, "level": "A1",
             "title": {"en": "Romanian: Basics", "ru": "Румынский: Основы",
                       "ro": "Română: Noțiuni de bază", "uk": "Румунська: Основи",
                       "zh": "罗马尼亚语：基础", "es": "Rumano: Fundamentos",
                       "fr": "Roumain : Bases", "de": "Rumänisch: Grundlagen",
                       "it": "Rumeno: Nozioni di base", "ja": "ルーマニア語: 基本"}},
            {"id": "l_ukr_basic", "course_id": "ukrainian_basics", "topic_index": 0, "level": "A1",
             "title": {"en": "Ukrainian: Basics", "ru": "Украинский: Основы",
                       "ro": "Ucraineană: Noțiuni de bază", "uk": "Українська: Основи",
                       "zh": "乌克兰语：基础", "es": "Ucraniano: Fundamentos",
                       "fr": "Ukrainien : Bases", "de": "Ukrainisch: Grundlagen",
                       "it": "Ucraino: Nozioni di base", "ja": "ウクライナ語: 基本"}},
            {"id": "l_rus_basic", "course_id": "russian_basics", "topic_index": 0, "level": "A1",
             "title": {"en": "Russian: Basics", "ru": "Русский: Основы",
                       "ro": "Rusă: Noțiuni de bază", "uk": "Російська: Основи",
                       "zh": "俄语：基础", "es": "Ruso: Fundamentos",
                       "fr": "Russe : Bases", "de": "Russisch: Grundlagen",
                       "it": "Russo: Nozioni di base", "ja": "ロシア語: 基本"}},
        ],
    },
]