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
    s_split = sent_tokenize(unidecode(s), language='english')
    return s_split

def tag(s):
    """
    Tokenize and apply name entity recognition to tag input string
    """
    s_tokenize = word_tokenize(s)
    return st.tag(s_tokenize)

def group_tag(s):
    ner_tag = st.tag(s)
    # group same tag together
    return None
