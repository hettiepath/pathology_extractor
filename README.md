# Breast Cancer Pathology Extractor

this is a general repository to extract information and combine
information from given Breast cancer pathology progress notes and
pathology report.


## Report text to csv file

The given dataset is separated by `|` and `||` symbol. We created `report2csv.py`
in order to turn the report into `csv` format.

```python
python report2csv.py -i input_report.txt -o output_report.csv
```


## Extractors

Here are few implemented functions to extract information from breast cancer reports

- `extract_age_report()` - return approximate age of patient
- `extract_dob_report()` - return date of birth from report if existed


### Run StanfordCoreNLP backend

In order to use extractor, we also incorporate `pyner` in order to help
doing name entity recognition task. See this [page](docs/stanford_nlp.md) to
run `pyner` on the backend.


### Dependencies

- [pandas](http://pandas.pydata.org/)
- [nltk](http://www.nltk.org/)
- [pyner](https://github.com/dat/pyner)
- [pycorenlp](https://github.com/smilli/py-corenlp)
- [unidecode](https://pypi.python.org/pypi/Unidecode)
