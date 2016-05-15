from itertools import groupby
from operator import itemgetter
import re
from unidecode import unidecode
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger

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

    Example
    -------
    >> group_tag('Rami Eid is studying at Stony Brook University in NY')
    """
    ner_tag = tag(s)
    # group by consecutive key
    ner_tag_group = list()
    for key, group in groupby(ner_tag, itemgetter(1)):
        entity = ' '.join([g[0] for g in group])
        ner_tag_group.append(tuple((entity, key)))
    return ner_tag_group
