# Random Problems Solved

This project has a set of random problems solved

## Installation

- Download the project: `git clone git@github.com:monciopeloncio/random-problems.git`
- Install requirements for Python: `pip install -r requirements.txt`
- This project is compatible with **python 3.6**.


### Shakespeare

It's possible to execute the word count using 2 methods:

- Normal processing
- NLTK processing

In order to use the nltk processing is neccessary to install nltk python package:

```bash
pip3 install -r requirements.txt
```

After install the requirements, executign the following python code we can download the rest of the neccesary packages:

```python3
import nltk.download
download()
```

A download manager will appear. The only package neccesary is "books"

```bash
cd shakespeare/src/
python3 word_count -n
```


