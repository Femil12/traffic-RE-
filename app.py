from __future__ import division, print_function
#import sys
import os
import cv2
#import re
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import statistics as st


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")
    
    
@app.route('/camera', methods = ['GET', 'POST'])
def camera():
    cap=cv2.VideoCapture(0)
    while True:
    	success,frame=cap.read()
    	if success:
    		cv2.imshow('LIVE',frame)
    	if cv2.waitKey(1)& 0xFF==ord('e'):
    		break
    cap.release()
    cv2.destroyAllWindows()
    
@app.route('/templates/join_page', methods = ['GET', 'POST'])
def join():
    return render_template("join_page.html")
    
if __name__ == "__main__":
    app.run(debug=True)
