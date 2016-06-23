# Breast Cancer Pathology Extractor

This is a repository to extract and structure information
from given Breast cancer pathology progress notes and
pathology report.


## Report text to csv file

The given dataset is separated by `|` and `||` symbol. We created `report2csv.py`
in order to turn the report into `csv` format.

```python
python report2csv.py -i input_report.txt -o output_report.csv
```


## Install and use extractors

Install using `setup.py`, running the following

```
$ python setup.py install
```

Here are few implemented functions available to extract information
from breast cancer reports/ progress notes

- `split` - split report into list of sentences
- `extract_time()` - return list of datetime for given string
- `extract_age_report()` - return approximate age of patient
- `extract_dob_report()` - return date of birth from report if existed


### Examples

Here is example on how to use `extractor` library

```python
import extractor
dob = extractor.extract_dob_report(report)
```


### Run StanfordCoreNLP backend

In order to use `extractor`, we also incorporate `pyner` in order to help
doing name entity recognition task. See this [page](docs/stanford_nlp.md) to
run `pyner` on the backend.


### Dependencies

- [pandas](http://pandas.pydata.org/)
- [nltk](http://www.nltk.org/)
- [pyner](https://github.com/dat/pyner)
- [pycorenlp](https://github.com/smilli/py-corenlp)
- [unidecode](https://pypi.python.org/pypi/Unidecode)
