import re
import ner
from itertools import groupby
from operator import itemgetter
from unidecode import unidecode
from itertools import chain
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import StanfordNERTagger
from .keywords import ESTROGEN_POSITIVE, ESTROGEN_NEGATIVE, \
    PROGESTERONE_POSITIVE, PROGESTERONE_NEGATIVE, \
    DATE_RELATED

__all__ = ['split',
           'tag',
           'group_tag',
           'group_tag_ner',
           'extract_time',
           'extract_estrogen',
           'extract_estrogen']

taggers = ['english.all.3class.distsim.crf.ser.gz',
           'english.muc.7class.distsim.crf.ser.gz',
           'english.conll.4class.distsim.crf.ser.gz']
st = StanfordNERTagger(taggers[0]) # nltk tagger
ner_tagger = ner.SocketNER(host='localhost', port=8080) # pyner tagger


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

    TO DO: return same format as group_tag_ner i.e. {'key': [, ,], 'key': [, ]}
    """
    ner_tag = tag(s)
    # group by consecutive key
    ner_tag_group = list()
    for key, group in groupby(ner_tag, itemgetter(1)):
        entity = ' '.join([g[0] for g in group])
        ner_tag_group.append(tuple((key, entity)))
    return ner_tag_group

def group_tag_ner(s):
    """
    Group consecutive out tuple from NER with key (second element of tuple)

    Parameters
    ----------
    s: str, input string

    Returns
    -------
    ner_tag_group: dictionary of NER tagged
    """
    return ner_tagger.get_entities(s)


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
        for pattern in patterns:
            match = re.findall(pattern, s)
            dates.append(match)
    # extend tagger using Stanford NER
    tag = group_tag_ner(s)
    if 'DATE' in tag.keys():
        dates.extend(tag['DATE'])
    return list(chain(*dates))


def tag_estrogen(s):
    """
    Extract estrogen related sentence
    dictionary contains if estrogen receptor is positive or negative
    and sentence
    """
    s_lower = s.lower()
    er_positive = False
    er_negative = False
    for e in ESTROGEN_POSITIVE:
        if e in s_lower:
            er_positive = True
    for e in ESTROGEN_NEGATIVE:
        if e in s_lower:
            er_negative = True
    if er_positive or er_negative is True:
        dict_out = {'er_positive': er_positive,
                    'er_negative': er_negative,
                    'sentence': s}
    else:
        dict_out = None
    return dict_out


def extract_estrogen(report):
    """
    Extract Estrogen Receptors feature and sentences related

    Parameters
    ----------
    report: str, input string of report or progress notes

    Returns
    -------
    s_collect: list of dictionary contains status of estrogen receptor,
        sentences related to estrogen receptor
    """
    sentences = split(report)
    s_collect = list() # list of collect sentences
    for s in sentences:
        dict_out = tag_estrogen(s)
        if dict_out is not None:
            s_collect.append(dict_out)
    return s_collect
