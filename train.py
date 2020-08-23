import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import os,PIL,cv2,imghdr,h5py

from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow import keras
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import ReduceLROnPlateau

import pathlib

#显存比较小的话请开启按需申请显存
'''
gpu = tf.config.experimental.list_physical_devices(device_type='GPU')
assert len(gpu) == 1
tf.config.experimental.set_memory_growth(gpu[0], True)
'''

data_dir=os.getcwd()+'\dataset_face'#设置路径为数据集的路径
data_dir=pathlib.Path(data_dir)#转换成pathlib的格式方便后面调用

image_count=len(list(data_dir.glob('*/*.jpg')))
print(image_count)

#########################定义基本参数###########################
batch_size=128
img_height=200
img_width=200

#########################建立训练集##############################
train_ds=tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2, #保留验证数据占比
    subset="training",
    seed=19260817, #随机排列种子
    image_size=(img_height,img_width),
    batch_size=batch_size #批量数据大小
)

########################建立验证集###############################
val_ds=tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=19260817,
    image_size=(img_height,img_width),
    batch_size=batch_size
)

class_names=train_ds.class_names
print(class_names)

#########################增强数据##################################

data_augmentation=keras.Sequential([
    layers.experimental.preprocessing.RandomFlip("horizontal",input_shape=(img_height,img_width,3)),#镜像
    layers.experimental.preprocessing.RandomRotation(0.1),#旋转
    layers.experimental.preprocessing.RandomZoom(0.1)#缩放
])

#########################创建模型##################################

num_classes=len(class_names)
model=Sequential([
    data_augmentation,
    layers.experimental.preprocessing.Rescaling(1./255),
    layers.Conv2D(16,(3,3),activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(32,(3,3),activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dropout(0.2),
    layers.Dense(128,activation='relu'),
    layers.Dense(num_classes)
])

############################编译模型###############################

model.compile(
    optimizer='adam',
    loss=losses.SparseCategoricalCrossentropy(from_logits=True),
    #loss=losses.binary_crossentropy,
    metrics=['accuracy']
)

model.summary()#显示模型

############################训练模型################################
epochs=25 #训练次数
model_path="model_face.h5"

checkpoint=ModelCheckpoint(
    model_path,
    monitor='val_accuracy',
    verbose=1,save_best_only=True,
    mode='max',
    period=1
)

#不再进步之后降低学习率
_reduce=ReduceLROnPlateau(
    monitor='val_loss', 
    factor=0.1, 
    patience=10, 
    verbose=0, 
    mode='min', 
    epsilon=0.0001,
    cooldown=0, 
    min_lr=0
)

callbacks_list=[checkpoint,_reduce]

history=model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs,
  callbacks=callbacks_list
)


######################可视化培训过程##################################

acc=history.history['accuracy']
val_acc=history.history['val_accuracy']

loss=history.history['loss']
val_loss=history.history['val_loss']

epochs_range=range(epochs)

plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.plot(epochs_range,acc,label='Training Accuracy')
plt.plot(epochs_range,val_acc,label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accurancy')

plt.subplot(1,2,2)
plt.plot(epochs_range,loss,label='Training Loss')
plt.plot(epochs_range,val_loss,label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()