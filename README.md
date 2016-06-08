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


### Run Name Entity Recognition

Download NER model (here)[http://nlp.stanford.edu/software/CRF-NER.shtml#Download].
We use `nltk` for NER, POS taggers. See related [issue](https://github.com/nltk/nltk/issues/1239))
and [Stack Overflow post](http://stackoverflow.com/questions/13883277/stanford-parser-and-nltk/34112695#34112695)
on how to install. First, download NER model that works

```bash
wget http://nlp.stanford.edu/software/stanford-ner-2015-04-20.zip
```

Add environment to `.bash_profile`,

```bash
export STANFORD_MODELS=<PATH_TO>/stanford-ner-2015-04-20/classifiers
export CLASSPATH=<PATH_TO>/stanford-ner-2015-04-20/stanford-ner.jar
```

Try tagging the sentence. Here I use example from `nltk`

```python
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
st.tag('Rami Eid is studying at Stony Brook University in NY'.split())
```

### Run Name Entity Recognition using PyNER

More details can be found in Stack Overflow  [post](http://stackoverflow.com/questions/15722802/how-do-i-use-python-interface-of-stanford-nernamed-entity-recogniser).
First, run `NERServer`, in this case in port 8080,

```bash
java -mx1000m -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer -loadClassifier classifiers/english.muc.7class.distsim.crf.ser.gz -port 8080 -outputFormat inlineXML
```

Then in Python, we can use `ner` provided by [pyner](https://github.com/dat/pyner)
in order to tag entity,

```python
import ner
tagger = ner.SocketNER(host='localhost', port=8080)
tagger.get_entities("University of California is located in California, United States")
```


### Dependencies

- [pandas](http://pandas.pydata.org/)
- [nltk](http://www.nltk.org/)
- [pyner](https://github.com/dat/pyner)
- [pycorenlp](https://github.com/smilli/py-corenlp)
- [unidecode](https://pypi.python.org/pypi/Unidecode)
