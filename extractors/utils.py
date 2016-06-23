import datetime
from unidecode import unidecode
from nltk.tokenize import sent_tokenize

def split(s):
    """
    Split string into list of sentences
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
    year = int(year)
    if year >= 20 and year <= 99:
        year = int('19' + str(year))
    elif year <= 20:
        year = int('20' + str(year))
    else:
        year = year
    return year
