#tensorflow无法识别非jpeg类型的图片，因此需要先进行处理
import cv2
import os
import imghdr
data_dir=os.getcwd()

file=os.walk(data_dir)

######################利用OpenCV更改文件类型################
for path,dir_list,file_list in file:
    for folder in dir_list:
        sub_folder=os.path.join(data_dir,folder)
        for sub_path,sub_dir_list,sub_file_list in os.walk(sub_folder):
            for image in sub_file_list:
                img=cv2.imread(str(sub_folder)+'\\'+image,cv2.IMREAD_UNCHANGED)
                file_type=imghdr.what(str(sub_folder)+'\\'+image)
                #print(file_type)
                if file_type!='jpeg':
                    print(str(image)+"-invalid-"+str(file_type))

                    if(file_type=='gif'or file_type=='None'):
                        os.remove(str(sub_folder)+'\\'+image) #gif和None没法保存，直接删除             
                    else:
                        cv2.imwrite(str(sub_folder)+'\\'+image,img) #转换成jpeg

print("Datas are cleaned Sucessful!")