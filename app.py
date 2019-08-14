""" python script to create API endpoints for spell check"""
__author__ = "Anshul Gautam"
__company__ = "HaikuJAM"
__email__ = "anshul.gautam@pivotchain.com", 
__status__ = "Assignment"


# import all required libraries
import requests, subprocess
from flask import Flask, request, jsonify
import re
import itertools
import string
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
nltk.download('stopwords')
from nltk.corpus import stopwords


#App to create endpoints
app = Flask('app')

# Function to check if the string is english word or not (except stopwords)
def check_if_word(word):
  if wordnet.synsets(word) or word in stopwords.words('english'):
    return word
  else:
    return False

		
#Endpoint to check flask app running properly
@app.route('/ping/', methods=['POST'])
def ping():
	return jsonify({'ping':'pong'})

	
#Endpoint for spell check
@app.route('/spellCorrect/', methods=['POST'])
def spellCorrect():
	data = request.get_json()
	data['sub_words'] = []
	word = data['word']

	word = ''.join(word.translate(str.maketrans({key: ' ' for key in string.punctuation})).split())
	word = ''.join((re.sub("\d", " ", word)).split())
	word = word.lower()

	permuts = [[''.join(word[:n]),''.join(word[n:])] for n in range(2,len(word)-1)]
	for sub_word in permuts:
		if check_if_word(sub_word[0]) and check_if_word(sub_word[1]):
			data['sub_words'] = sub_word
			break
	if not data['sub_words']:
		data['sub_words'] = [''.join(word)]
	return jsonify(data)


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)