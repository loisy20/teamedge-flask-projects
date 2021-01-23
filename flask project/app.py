from flask import Flask, render_template, request, json, jsonify, current_app as app 
import os
import requests 
app = Flask(__name__) 

@app.route('/')
def about():
    #return '<p>Hello Flask</p>' 
    return render_template('index.html')


@app.route('/lois')   
def Lois():
    return '<p>Hi my name is Lois</p>'


if __name__=='__main__':
    app.run(debug = True, host='127.0.0.1')

