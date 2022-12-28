import imp
from pyexpat import model
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from re import template
from flask import Flask,render_template,request
from tensorflow.keras.models import load_model
from PIL import Image
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt



from tensorflow.keras.preprocessing import image
import numpy as np
import os

from PIL import Image
import tensorflow as tf
from keras.applications.vgg19 import VGG19,preprocess_input,decode_predictions
from werkzeug.utils import HTMLBuilder, secure_filename


class predict:

    def __init__(self):
        try:
            self.model = load_model("./trained model/Dis_Classifier.h5")
        except Exception as e:
            print(e)
    def model_predict(self,img_path):
        test_image = image.load_img(img_path, target_size=(256, 256))
        test_image = image.img_to_array(test_image)
        #test_image = test_image / 255
        test_image=image.img_to_array(test_image)
        test_image=preprocess_input(test_image)
        # plt.title('pre processing')
        # plt.imshow(test_image)
        # plt.show()
       
   
        
        test_imag = np.expand_dims(test_image, axis=0)
        
        
        
        result = self.model.predict(test_imag).astype("float64")
        #con=round (100*(np.max(result[0]))
        

        #print(con)
        re=(result[0][result.argmax()]*100)
        print(re-2)
        
        


        
        
        return np.array(test_image), result
        