from itertools import groupby
from operator import itemgetter
import re
from unidecode import unidecode
from itertools import chain
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger
from .keywords import ESTROGEN_POSITIVE, ESTROGEN_NEGATIVE, \
    PROGESTERONE_POSITIVE, PROGESTERONE_NEGATIVE, \
    DATE_RELATED



taggers = ['english.all.3class.distsim.crf.ser.gz',
           'english.muc.7class.distsim.crf.ser.gz',
           'english.conll.4class.distsim.crf.ser.gz']
st = StanfordNERTagger(taggers[0])


def split(s):
    """
    Simple split sentence
    """
    s_split = sent_tokenize(unidecode(s), language='english')
    return s_split

def tag(s):
    """
    Tokenize and apply name entity recognition (NER) to tag input string

    Parameters
    ----------
    s: str, input string

    Returns
    -------
    ner_tag: list of tuple, NER tag output
    """
    s_tokenize = word_tokenize(s)
    ner_tag = st.tag(s_tokenize)
    return ner_tag

def group_tag(s):
    """
    Group consecutive out tuple from NER with key (second element of tuple)

    Parameters
    ----------
    s: str, input string

    Returns
    -------
    ner_tag_group: list of tuple, group NER tag output

    Examples
    --------
    >> group_tag('Rami Eid is studying at Stony Brook University in NY')
    """
    ner_tag = tag(s)
    # group by consecutive key
    ner_tag_group = list()
    for key, group in groupby(ner_tag, itemgetter(1)):
        entity = ' '.join([g[0] for g in group])
        ner_tag_group.append(tuple((entity, key)))
    return ner_tag_group

def extract_time(s):
    """
    Extract date time from report string

    Parameters
    ----------
    s: str, input string

    TO DO: use Stanford NLP to extract time
    """

    s = s.lower()
    dates = list()
    patterns = [r'(\d+/\d+/\d+)', r'(\d+/\d+)']
    if any(d in s for d in DATE_RELATED):
        try:
            for pattern in patterns:
                match = re.findall(pattern, s)
                dates.append(match)
        except:
            dates = list()
    return list(chain(*dates))


def estrogen_tagger(report):
    """
    Extract Estrogen Receptors feature and sentences related

    Parameters
    ----------
    report: str, input string of report or progress notes

    Returns
    -------
    dict_out: dictionary contains status of estrogen receptor,
        sentences related to estrogen receptor
    """
    sentences = split(report)
    er_positive = False
    er_negative = False
    s_collect = list() # list of collect sentences
    for s in sentences:
        s = s.lower()
        for e in ESTROGEN_POSITIVE:
            if e in s:
                er_positive = True
                s_collect.append(s)
        for e in ESTROGEN_NEGATIVE:
            if e in s:
                er_negative = True
                s_collect.append(s)
    dict_out = {'er_positive': er_positive,
                'er_negative': er_negative,
                'sentences': s_collect}
    return dict_out
