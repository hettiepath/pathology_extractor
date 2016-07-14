import re
import datetime
from unidecode import unidecode
from nltk.tokenize import sent_tokenize
from .keywords import ESTROGEN_PERCENT, PROGESTERONE_PERCENT, HER2_PERCENT, \
    DCIS_PERCENT
import ner

ner_tagger = ner.SocketNER(host='localhost', port=8080) # pyner tagger

def split(s):
    """
    Split string into list of sentences

    Parameters
    ----------
    s: str, input string

    Returns
    -------
    s_split: list of split sentences
    """
    s_split = sent_tokenize(unidecode(s), language='english')
    return s_split

def most_common(lst):
    """
    return most common element from given list, lst
    """
    return max(set(lst), key=lst.count)

def remove_int(ls):
    """
    remove plain integer element from list, ls
    """
    ls_rm = list()
    for s in ls:
        try:
            s = int(s)
            if isinstance(s, int):
                continue
        except:
            ls_rm.append(s)
    return ls_rm

def remove_duplicate(seq):
    """
    remove duplicate string in list while preserving order
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def remove_partial_duplicate(ls):
    """
    Remove partial duplicate string from list

    reference:
        http://stackoverflow.com/questions/37981029/remove-element-from-list-if-part-of-string-is-duplicate
    """
    ls = remove_duplicate(ls) # merge duplicate string in list first
    ls = remove_int(ls)
    ls_out = list()
    for x in ls:
        if x not in ls_out and (not any([x in item for item in ls_out])):
            ls_out.append(x)
    return ls_out

def check_year(year):
    """
    Utility function to check if year is in right format
    """
    year = str(year)
    if len(year.split(' ')) >= 2:
        year = year.split(' ')[0]
    year = int(year)
    if year >= 16 and year <= 99:
        year = int('19' + str(year))
    elif year <= 9:
        year = int('200' + str(year))
    elif year > 9 and year <= 16:
        year = int('20' + str(year))
    else:
        year = year
    return year

def tag_percent(s, percent_pattern):
    """
    Find what percentage of progesterone receptor

    Parameters
    ----------
    s: str, input string

    Returns
    -------
    percent: str, output percent string
    """
    s = s.lower()
    percent = None
    for pp in percent_pattern:
        percent_str = re.findall(pp, s)
        if percent_str:
            tag = ner_tagger.get_entities(percent_str[0])
            if 'PERCENT' in tag.keys():
                percent = tag['PERCENT'][0]
    return percent
