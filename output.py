import requests
from flask import Flask, request, jsonify

url = 'http://localhost:5000/spellCorrect/'
data = {'word':'123goodluck#-'}

output = requests.post(url, json=data)
out_data = output.json()
print('Word: ',out_data['word'],' | Sub words: ', out_data['sub_words'])