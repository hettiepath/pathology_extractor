# set of words that typically show up in the report

ESTROGEN_POSITIVE = frozenset(['er/pr+', 'er/pr +', 'er/pr was positive',
    'er/pr is positive', 'er/pr/her-2 positive', 'er/pr/her-2 +',
    'estrogen receptor positive', 'er/pr 70% positive',
    'er weakly positive', 'er/pr-positive'])

PROGESTERONE_POSITIVE = frozenset(['er/pr+', 'er/pr +', 'er/pr was positive',
    'er/pr is positive', 'er/pr/her-2 positive', 'er/pr/her-2 +',
    'estrogen receptor positive', 'er/pr 70% positive',
    'pr weakly positive', 'er/pr-positive'])

ESTROGEN_NEGATIVE = frozenset(['er/pr -', 'er/pr -', 'er/pr was negative',
    'er/pr is negative', 'er/pr/her-2 negative', 'er/pr/her-2 -',
    'er/pr/her2 negative', 'er/pr her-2 negative',
    'er weakly positive', 'er/pr-negative'])

PROGESTERONE_NEGATIVE = frozenset(['er/pr -', 'er/pr -', 'er/pr was negative',
    'er/pr is negative', 'er/pr/her-2 negative', 'er/pr/her-2 -',
    'er/pr/her2 negative', 'er/pr her-2 negative',
    'pr weakly negative', 'er/pr-negative'])

HER2_POSITIVE = frozenset(['er/pr/her-2 positive', 'er/pr/her-2 +',
    'er/pr her-2 positive', 'her2neu pos', 'her2neu positive',
    'her 2 3+ positive', 'her 2-positive', 'her2 3+'])

HER2_NEGATIVE = frozenset(['er/pr/her-2 negative', 'er/pr/her-2 -',
    'er/pr her-2 negative', 'her2neu neg', 'her2neu negative',
    'her 2 2- negative', 'her 2-positive'])

SURGICAL = frozenset(['s/p mastectomy', 's/p hysterectomy'])

ER/PR-positive HER 2-positive
