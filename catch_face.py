#将猫脸识别出来供后面训练模型使用
import cv2
import os

from PIL import Image

#读取opencv官方的猫脸识别模型
catface_cascade=cv2.CascadeClassifier('catface_detector.xml')

#数据集目录
ori_dirpath=os.getcwd()+'\dataset'
new_dirpath=os.getcwd()+'\dataset_face'

dim=(600,600)

def catch_face(img,path,name):
    
    img_resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
    #识别猫脸
    cat_faces=catface_cascade.detectMultiScale(img_resized,scaleFactor=1.3,minNeighbors=3,minSize=(75,75))
    for(x,y,w,h) in cat_faces:
        file=cv2.resize(img_resized[y:(y+h),x:(x+w)],(200,200))
        print(name+' was caught face successful!')
        cv2.imwrite(str(path)+'\\'+name+'.jpg',file)#保存

for root,dirs,files in os.walk(ori_dirpath):
    for _dir in dirs:

        temp_oridir=os.path.join(ori_dirpath,_dir)
        temp_newdir=os.path.join(new_dirpath,_dir)
        #判断是否存在相应文件夹，如果不存在则创建
        folder=os.path.exists(os.path.join(new_dirpath,_dir))

        if not folder:
            os.makedirs(os.path.join(new_dirpath,_dir))

        cnt=1
        for file in os.listdir(temp_oridir):
            img=cv2.imread(os.path.join(temp_oridir,file))
            name=str(_dir)+str(cnt)
            catch_face(img,temp_newdir,name)
            cnt+=1


path=os.getcwd()+'\dataset_face'
img=cv2.imread('test.jpg')
catch_face(img,path,'file')

