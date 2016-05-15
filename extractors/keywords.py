# set of words that typically show up in the report

ESTROGEN_POSITIVE = frozenset(['er/pr+', 'er/pr +', 'er/pr was positive',
    'er/pr is positive', 'er/pr/her-2 positive', 'er/pr/her-2 +',
    'estrogen receptor positive'])

PROGESTERONE_POSITIVE = frozenset(['er/pr+', 'er/pr +', 'er/pr was positive',
    'er/pr is positive', 'er/pr/her-2 positive', 'er/pr/her-2 +',
    'estrogen receptor positive'])

ESTROGEN_NEGATIVE = frozenset(['er/pr -', 'er/pr -', 'er/pr was negative',
    'er/pr is negative', 'er/pr/her-2 negative', 'er/pr/her-2 -',
    'er/pr/her2 negative', 'er/pr her-2 negative'])

PROGESTERONE_NEGATIVE = frozenset(['er/pr -', 'er/pr -', 'er/pr was negative',
    'er/pr is negative', 'er/pr/her-2 negative', 'er/pr/her-2 -',
    'er/pr/her2 negative', 'er/pr her-2 negative'])

HER2_POSITIVE = frozenset(['er/pr/her-2 positive', 'er/pr/her-2 +',
    'er/pr her-2 positive'])

HER2_NEGATIVE = frozenset(['er/pr/her-2 negative', 'er/pr/her-2 -',
    'er/pr her-2 negative'])
