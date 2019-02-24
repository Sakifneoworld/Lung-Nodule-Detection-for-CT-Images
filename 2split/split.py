import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

template = cv2.imread('zzz.jpg',0)
ww, hh = template.shape[::-1]

def split(cancer):  
            #file_name, file_ext = os.path.splitext(f)
            img_rgb = cancer
            img_gray = cancer
            res = cv2.matchTemplate(cancer,template,cv2.TM_CCOEFF_NORMED)
            aa = np.max(res)
            print(aa)
            loc = np.where( res >= aa)
            a=0
            b=0
            for pt in zip(*loc[::-1]):
                #print(pt[0],pt[1])
                cv2.rectangle(img_rgb, pt, (pt[0] + ww, pt[1] + hh), (255), 2)
                a = pt[0]
                b = pt[1]
            cv2.imshow("template",template)
            cv2.imshow("Maching",img_rgb)
            x = int(ww/2)
            y = int(hh)
            print(x,y)
            print(a,b)
            crop1 = img_gray[ int(b-10):int (b+20 +y),int(a):int(a+x +10)]
            crop2 = img_gray[ int(b-10):int (b+20 +y),int(a+x+5):int(a+2*x +10)]

            cv2.imshow("crop",crop1)
            cv2.imshow("crop2",crop2)
            cv2.waitKey(0)
            
            new_name1 = '{}{}{}'.format('x',file_name,file_ext)
            os.rename(f, new_name1)
            cv2.imwrite(f,crop1)
            new_name1 = '{}{}{}'.format('y',file_name,file_ext)
            os.rename(f, new_name1)
            cv2.imwrite(f,crop2)
            return cancer

            




for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    w=0
    h=0
    if ( file_ext == ".jpg"):
        file_name = file_name.strip().zfill(4)

        #new_name = '{}{}'.format(file_name,file_ext)

        cancer = cv2.imread(f,0)

        thresh = split(cancer)

        #os.rename(f, new_name)

        

        #cv2.imwrite(f,thresh)




        



        
