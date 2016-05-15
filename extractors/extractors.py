import re
from nltk.tag import StanfordNERTagger
from nltk.tokenize import WhitespaceTokenizer
taggers = ['english.all.3class.distsim.crf.ser.gz',
           'english.muc.7class.distsim.crf.ser.gz',
           'english.conll.4class.distsim.crf.ser.gz']
st = StanfordNERTagger(taggers[0])
w_tokenizer = WhitespaceTokenizer()

def tag(s):
    """
    Tokenize and apply name entity recognition to tag input string
    """
    s_tokenize = w_tokenizer.tokenize(s)
    return st.tag(s_tokenize)

def group_tag(s)
    ner_tag = st.tag(s)
    # group same tag together
    return None
