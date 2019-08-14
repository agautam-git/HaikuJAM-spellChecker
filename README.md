# SpellChecker
RestFUL API which should take in single-word and return a list of correct words.
E.g.:
  - Input: "123goodluck#-"
  - Output: ["good","luck"]

## Feature
  - Basic preprocessing of word (Numbers/symbol removal)
  - Different word letters combination vocab check and filter

## Technique
- Punctuation/symbols removal using string function
- Numbers removal using regex
- Word check using NLTK's wordnet and stopword coprpus
- API development using FLASK framework

## Execution
Git clone the repository.
```sh
$ git clone https://github.com/agautam-git/HaikuJAM-spellChecker.git
$ cd HaikuJAM-spellChecker/
```

Install the dependencies and libraries.

```sh
$ pip install requirements.txt
```

For App run export app and run flask

```sh
$ export FLASK_APP=app.py
$ flask run
```
For App test: run output.py with the keyword
```sh
$ python output.py -WORD '123goodluck#-'
Word: 123goodluck#- | Sub words: ['good', 'luck']
```