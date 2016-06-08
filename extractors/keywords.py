# set of words that typically show up in the report

DATE_RELATED = frozenset(['date:', 'date', 'on '])

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

SURGICAL = frozenset(['s/p mastectomy', 's/p hysterectomy'])
