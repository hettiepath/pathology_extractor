# Pathology Extractor

this is a general repository to extract information and combine
information from given pathology progress notes and pathology report. 


### Run Stanford Core NLP

Before using the code, we have to run and parse out the output.
You can follow this [post](http://titipata.github.io/2016/03/02/stanford-nlp.html)
on how to install and run Stanford which will be served on `http://localhost:9000/`.
Download CoreNLP [here](http://stanfordnlp.github.io/CoreNLP/index.html).

```bash
screen # start screen
export CLASSPATH="`find . -name '*.jar'`"
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer [port?] # run server
```

To read out the result we use [py-corenlp](https://github.com/smilli/py-corenlp)
to read output. `py-corenlp` provides a very intuitive way to use in Python.
See example below:

```python
from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')
text = 'Paradropp is the best player in League of Legend'
output = nlp.annotate(text,
    properties={
      'annotators': 'ner,openie',
      'outputFormat': 'json'}
    )
```

### Dependencies

- [pandas](http://pandas.pydata.org/)
- [pyner](https://github.com/dat/pyner)
- [nltk](http://www.nltk.org/)
