from re import template
from flask import Flask,render_template,request
from tensorflow.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import tensorflow as tf
from keras.applications.vgg19 import VGG19,preprocess_input,decode_predictions
from werkzeug.utils import HTMLBuilder, secure_filename
from test import predict

pre = predict()

# define the flask app
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('website.html')

@app.route('/index')
def kamal():
    return render_template('index.html')
@app.route('/service')
def jamal():
    return render_template('service.html')
@app.route('/contact')
def yamal():
    return render_template('contact.html')
@app.route('/why')
def damal():
    return render_template('why.html')
@app.route('/calculator')
def hamal():
    return render_template('calculator.html')


@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        # get the file from post request
        f=request.files['file']

        # save the file to uploads folder
        basepath=os.path.dirname(os.path.realpath('_file_'))
        file_path=os.path.join(basepath,'uploads',secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        test_imgae, result =pre.model_predict(file_path)
        



        categories = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Incorrect',
 'Peach___Bacterial_spot',
 'Peach___healthy']
        import io
        from base64 import b64encode
        from PIL import Image
        # process your result for human
        pred_class = result.argmax()
        
        print('p',pred_class)
        output=categories[pred_class]
        
        print('output',output)
        base64img = ''
        file_object = io.BytesIO()
        try:
            img= Image.fromarray(test_imgae.astype('uint8'))
            img.save(file_object, 'JPEG')
        except:
            print('error')
        base64img = "data:image/JPEG;base64,"+b64encode(file_object.getvalue()).decode('ascii')
        return {'img':str(base64img), "res":output}
        
       
                

    return None

if __name__=='__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)