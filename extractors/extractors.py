import re
import ner
import datetime
import dateutil
import pandas as pd
from itertools import groupby
from operator import itemgetter
from itertools import chain
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger
from .keywords import ESTROGEN_POSITIVE, ESTROGEN_NEGATIVE, \
    PROGESTERONE_POSITIVE, PROGESTERONE_NEGATIVE, \
    ESTROGEN_PERCENT, PROGESTERONE_PERCENT, HER2_PERCENT, \
    DATE_RELATED, DATE_OF_BIRTH, AGE
from .utils import *

__all__ = ['tag',
           'split',
           'group_tag',
           'group_tag_ner',
           'extract_time',
           'extract_time_str',
           'tag_estrogen',
           'extract_estrogen',
           'tag_progesterone',
           'tag_estrogen_percent',
           'tag_progesterone_percent',
           'str_to_date',
           'extract_dob']

taggers = ['english.all.3class.distsim.crf.ser.gz',
           'english.muc.7class.distsim.crf.ser.gz',
           'english.conll.4class.distsim.crf.ser.gz']
st = StanfordNERTagger(taggers[0]) # nltk tagger
ner_tagger = ner.SocketNER(host='localhost', port=8080) # pyner tagger


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
    ner_group = list()
    for key, group in groupby(ner_tag, itemgetter(1)):
        entity = ' '.join([g[0] for g in group])
        ner_group.append(tuple((key, entity)))
    ner_group_sorted = sorted(ner_group, key=lambda x: x[0]) # sort key

    # merge by key
    groups = dict()
    for key, group in groupby(ner_group_sorted, lambda x: x[0]):
        g_ = list(g[1] for g in group)
        groups[key] = g_
    groups.pop("O", None)
    return groups

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
    Extract date time from report string where we
    consider that it contains date

    Parameters
    ----------
    s: str, input string that we want to extract time

    Returns
    -------
    dates: list: list of dates found
    """
    s = s.lower()
    dates = list()
    patterns = [r'(\d+/\d+/\d+)', r'(\d+-\d+-\d+)', r'(\d+/\d+)']
    if any(d in s for d in DATE_RELATED):
        for pattern in patterns:
            match = re.findall(pattern, s)
            dates.append(match)
    # extend tagger using Stanford NER
    tag = group_tag_ner(s)
    if 'DATE' in tag.keys():
        dates.append(tag['DATE'])
    return list(chain(*dates))

def extract_time_str(s):
    """
    Extract date time date of birth pattern string

    Parameters
    ----------
    s: str, input string that we want to extract time

    Returns
    -------
    dt: date time format output of given string
    """
    s = s.lower()
    dates = list()
    patterns = [r'(\d+/\d+/\d+)', r'(\d+-\d+-\d+)']
    for pattern in patterns:
        match = re.findall(pattern, s)
        dates.append(match)
    dates = list(chain(*dates))
    dt = str_to_date(dates[0]) # date-time format
    return dt

def extract_dob(s):
    """
    Extract date of birth from given string
    """
    dob = None
    s = s.lower()
    for pattern in DATE_OF_BIRTH:
        match = re.findall(pattern, s)
        if match:
            dob = match[0]
    if dob is not None:
        dob_dt = extract_time_str(dob)
    else:
        dob_dt = None
    return dob_dt

def extract_dob_report(r):
    """
    Give full report, return potential date of birth of
    the patient

    Parameters
    ----------
    r: str, full report

    Returns
    -------
    dob: datetime, date of birth in datetime format
    """
    sentences = split(r)
    d = [extractors.extract_dob(s) for s in sentences]
    dob_list = list()
    for s in sentences:
        dob = extractors.extract_dob(s)
        if dob is not None:
            dob_list.append(dob)
    if len(dob_list) < 1:
        date_of_birth = None
    else:
        date_of_birth = most_common(dob_list)
    return date_of_birth

def extract_age(s):
    """
    Extract age from given string, s
    if found nothing, we will return None
    """
    age = None
    for pattern in AGE:
        match = re.findall(pattern, s)
        if match:
            age = match[0]
    return age

def extract_age_report(r):
    """
    Give full report, return potential date of birth of
    the patient

    Parameters
    ----------
    r: str, full report

    Returns
    -------
    age: int, age of patient
    """
    sentences = extractors.split(r)
    ages = [extract_age(s) for s in sentences]
    ages_list = [age for age in ages if age is not None]
    if ages_list:
        age_ = most_common(ages_list)
        age_int = re.findall('\d+', age_)
        if age_int:
            age_int = int(age_int[0])
    else:
        age_int = None
    return age_int

def str_to_date(date):
    """
    Interpret datetime string into datetime format

    Parameters
    ----------
    s: str, input date time string to interpret

    """
    d = date.split('/')
    if len(d) == 3:
        month = int(d[0])
        date = int(d[1])
        year = int(d[2])
        dt = datetime.datetime(year, month, date)
    elif len(d) == 2:
        if int(d[-1]) <= 12:
            year = datetime.datetime.now().year
            month = int(d[0])
            date = int(d[1])
        else:
            month = int(d[0])
            year = int(d[1])
            date = 15 # pick up random date
        dt = datetime.datetime(year, month, date)
    else:
        import dateutil
        try:
            dt = dateutil.parser.parse(date)
        except:
            dt = None
    return dt

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

def tag_progesterone(s):
    """
    Extract estrogen related sentence
    dictionary contains if estrogen receptor is positive or negative
    and sentence
    """
    s_lower = s.lower()
    pr_positive = False
    pr_negative = False
    for p in PROGESTERONE_POSITIVE:
        if p in s_lower:
            pr_positive = True
    for p in PROGESTERONE_NEGATIVE:
        if p in s_lower:
            pr_negative = True
    if pr_positive or pr_negative is True:
        dict_out = {'pr_positive': pr_positive,
                    'pr_negative': pr_negative,
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

def tag_estrogen_percent(s):
    """
    Find what percentage of estrogen receptor

    Parameters
    ----------
    s: str, input string

    Returns
    -------
    percent: str, output percent string
    """
    s = s.lower()
    percent = None
    for ep in ESTROGEN_PERCENT:
        percent_str = re.findall(ep, s)
        if percent_str:
            tag = ner_tagger.get_entities(percent_str[0])
            if 'PERCENT' in tag.keys():
                percent = tag['PERCENT'][0]
    return percent

def tag_progesterone_percent(s):
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
    for pp in PROGESTERONE_PERCENT:
        percent_str = re.findall(pp, s)
        if percent_str:
            tag = ner_tagger.get_entities(percent_str[0])
            if 'PERCENT' in tag.keys():
                percent = tag['PERCENT'][0]
    return percent

def tag_her_percent(s):
    """
    Find what percentage of HER2 receptor

    Parameters
    ----------
    s: str, input string

    Returns
    -------
    percent: str, output percent string
    """
    s = s.lower()
    percent = None
    for pp in PROGESTERONE_PERCENT:
        percent_str = re.findall(pp, s)
        if percent_str:
            tag = ner_tagger.get_entities(percent_str[0])
            if 'PERCENT' in tag.keys():
                percent = tag['PERCENT'][0]
    return percent
