# set of words that typically show up in the report

AGE = frozenset(['\d+ yo female', '\d+ yo woman',
    '\d+yo female', '\d+yo woman',
    '\d+ y/o female', '\d+ y/o woman',
    '\d+y/o female', '\d+y/o woman',
    '\d+ year old female', '\d+ year old woman',
    '\d+-year-old woman', '\d+yo f'])

DATE_RELATED = frozenset(['date:', 'date', 'on '])

DATE_OF_BIRTH = frozenset(['birth date: \d+/\d+/\d+',
    'date of birth: \d+/\d+/\d+',
    'birth date: \d+-\d+-\d+',
    'date of birth: \d+-\d+-\d+',
    'dob: \d+/\d+/\d+',
    'dob: \d+-\d+-\d+'])

ESTROGEN_POSITIVE = frozenset(['er/pr+', 'er/pr +', 'er/pr was positive',
    'er/pr is positive', 'er/pr/her-2 positive', 'er/pr/her-2 +',
    'estrogen receptor positive', 'er/pr 70% positive',
    'er weakly positive', 'er/pr-positive',
    'er: +', 'er/pr: +', 'er/pr/her-2: +',
    'er positive', 'er: positive'])

PROGESTERONE_POSITIVE = frozenset(['er/pr+', 'er/pr +', 'er/pr was positive',
    'er/pr is positive', 'er/pr/her-2 positive', 'er/pr/her-2 +',
    'estrogen receptor positive', 'er/pr 70% positive',
    'pr weakly positive', 'er/pr-positive',
    'pr: +', 'er/pr: +', 'er/pr/her-2: +',
    'pr positive', 'pr: positive'])

ESTROGEN_NEGATIVE = frozenset(['er/pr -', 'er/pr -', 'er/pr was negative',
    'er/pr is negative', 'er/pr/her-2 negative', 'er/pr/her-2 -',
    'er/pr/her2 negative', 'er/pr her-2 negative',
    'er weakly negative', 'er/pr-negative',
    'er: -', 'er/pr: -', 'er/pr/her-2: -',
    'er negative', 'er: negative'])

PROGESTERONE_NEGATIVE = frozenset(['er/pr -', 'er/pr -', 'er/pr was negative',
    'er/pr is negative', 'er/pr/her-2 negative', 'er/pr/her-2 -',
    'er/pr/her2 negative', 'er/pr her-2 negative',
    'pr weakly negative', 'er/pr-negative',
    'pr: -', 'er/pr: -', 'er/pr/her-2: -',
    'pr negative', 'pr: negative'])

HER2_POSITIVE = frozenset(['er/pr/her-2 positive', 'er/pr/her-2 +',
    'er/pr her-2 positive', 'her2neu pos', 'her2neu positive',
    'her 2 3+ positive', 'her 2-positive', 'her2 3+',
    'er/pr/her-2: +', 'her-2/neu positive'])

HER2_NEGATIVE = frozenset(['er/pr/her-2 negative', 'er/pr/her-2 -',
    'er/pr her-2 negative', 'her2neu neg', 'her2neu negative',
    'her 2 2- negative', 'her 2-positive',
    'er/pr/her-2: -', 'her-2/neu negative'])

SURGICAL = frozenset(['s/p mastectomy', 's/p hysterectomy',
    'lumpectomy', 'biopsy'])

ESTROGEN_PERCENT = frozenset(['er \w+ \(\d+%\)', 'er \(\d+%\)',
    'er \w+ \d+%', 'estrogen receptor \w+ \(\d+%\)',
    'estrogen receptor \w+ \d+%', 'estrogen receptor \(\d+%\)',
    '\d+% er', '\d+ percent er',
    'er \w+ \d+ percent', 'er \d+ percent'])

PROGESTERONE_PERCENT = frozenset(['pr \w+ \(\d+%\)', 'pr \(\d+%\)',
    'pr \w+ \d+%', 'progesterone receptor \w+ \(\d+%\)',
    'progesterone receptor \w+ \d+%', 'progesterone receptor \(\d+%\)',
    '\d+% pr', '\d+ percent pr',
    'pr \w+ \d+ percent', 'pr \d+ percent'])

HER2_PERCENT = frozenset(['her-2 \w+ \(\d+%\)', 'her-2 \(\d+%\)',
    'her-2 \w+ \d+%', 'her-2 receptor \w+ \(\d+%\)',
    'her-2 receptor \w+ \d+%', 'her-2 receptor \(\d+%\)',
    '\d+% her-2', '\d+ percent her-2',
    'her2 \w+ \(\d+%\)', 'her2/neu \w+ \(\d+%\)'])
