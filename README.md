# Cat-Classfied
基于python+Keras+OpenCV利用CNN实现猫种类分类

## 获取数据
利用dataset文件夹中的get.exe获取数据集，可以通过修改get.cpp来更改想要获取的关键字，~~你也可以手动运行getdata.py来指定关键字~~。关于爬虫getdata.py的更多功能请自行阅读代码。

## 处理数据
由于tensorflow中只能识别jpeg类型，此处利用Opencv进行更改文件类型，避免文件名无法被opencv读取，因此先利用rename.py重命名文件，之后运行clean.py处理数据

## 训练模型
处理完数据后，利用train.py训练模型，默认训练25次，可自行更改，如果显存较小请开启按需分配显存，训练结束后训练过程会以图形的方式展示

## 预测新数据
将test.jpg放到目录下，运行predict.py即可
