import cv2
import os
import imghdr
data_dir=os.getcwd()

file=os.walk(data_dir)

############重命名，不知道为啥opencv读不出来奇怪的名字#######
for path,dir_list,file_list in file:
    for folder in dir_list:
        sub_folder=os.path.join(data_dir,folder)
        cnt=0
        for sub_path,sub_dir_list,sub_file_list in os.walk(sub_folder):
            for image in sub_file_list:

                oldname=sub_folder+'\\'+image
                newname=sub_folder+'\\_'+folder+'_'+str(cnt)+'.jpg'
                os.rename(oldname,newname)
                print(oldname,'======>',newname)
                cnt+=1