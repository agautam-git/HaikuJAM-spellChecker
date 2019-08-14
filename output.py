import requests, argparse
from flask import Flask, request, jsonify


parser = argparse.ArgumentParser(description='Enter the word: ')
parser.add_argument('-WORD','--word', help='input word', required=True)

def main(args):
	url = 'http://localhost:5000/spellCorrect/'
	data = {'word': args.word}
	output = requests.post(url, json=data)
	out_data = output.json()
	out_text = 'Word: '+str(out_data['word'])+' | Sub words: '+str(out_data['sub_words'])
	print(out_text)
	return out_text

if __name__ == '__main__':
	main(parser.parse_args())