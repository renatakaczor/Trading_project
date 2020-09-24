from flask import Flask, render_template, request, Response, jsonify
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

import spacy
# Chargement du modele français
#nlp = spacy.load('fr_core_news_sm')
#from flaskext.markdown import Markdown

#app initialization
app = Flask(__name__, template_folder='templates')
# main index page route
@app.route('/')
def home():
 return render_template('index.html', title='Home')

@app.route('/result_html',methods=['POST'])
def extract():
    user_text = request.form.get('input_text')
    print(user_text)
    #return render_template('index.html', title='Home')
    return render_template('result.html', title='Home')


if __name__ == "__main__":
 app.run(debug=True)


