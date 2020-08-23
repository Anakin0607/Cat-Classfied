import tensorflow as tf
import os
import numpy as np

from tensorflow import keras

##################载入新数据###################
file_path=os.getcwd()+'\\test.jpg'

img_height=400
img_width=400

data_path=os.getcwd()+'\dataset'
class_names=[]
for root,dirs,files in os.walk(data_path):
    for _dir in dirs:
        class_names.append(_dir)

img=keras.preprocessing.image.load_img(
    file_path,
    target_size=(img_height,img_width)
)

img_array=keras.preprocessing.image.img_to_array(img)
img_array=tf.expand_dims(img_array,0)

###############预测############################
model=tf.keras.models.load_model('model.h5')
predictions=model.predict(img_array)
score=tf.nn.softmax(predictions[0])#softmax输出

print("This image most likely belongs to %s with %.2lf percent " %(class_names[np.argmax(score)],100*np.max(score)))