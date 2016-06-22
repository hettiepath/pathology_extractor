def split(s):
    """
    Simple split sentence
    """
    s_split = sent_tokenize(unidecode(s), language='english')
    return s_split

def most_common(lst):
    """
    return most common element from given list, lst
    """
    return max(set(lst), key=lst.count)
