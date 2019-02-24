import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

print(os.getcwd())
def threshold(cancer):
            invcancer = cancer
            cv2.imshow("Input_Image",cancer)
            zzz = 22

            w,h = cancer.shape[::-1]
            #print(w,h)
            for j in range(w):
                for i in range ( h ):
                    a = cancer[i,j]
                    invcancer[i,j] = 255 -a 
                
            cv2.imshow("Negative_IMAGE",invcancer)

            plt.hist(invcancer.ravel(),256,[0,256]); plt.show()
            Gausecancer = cancer
            for x in range(zzz):
                Gausecancer = cv2.GaussianBlur(Gausecancer,(7,7),0)
            cv2.imshow("Gause",Gausecancer)
            cv2.imwrite("gause.png",Gausecancer)
            plt.hist(Gausecancer.ravel(),256,[0,256]); plt.show()
            #ret,thresh = cv2.threshold(Gausecancer,160,255,cv2.THRESH_BINARY_INV)
            ret,thresh = cv2.threshold(Gausecancer,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            cv2.imshow("Threshhold",thresh)
            #cv2.imwrite("sss.jpg",thresh)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return thresh
       



for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    #print(file_name)
    #print(file_ext)
    w=0
    h=0
    if ( file_ext == ".jpg"):
        file_name = file_name.strip().zfill(4)
        file_ext = ".jpg"
        #new_name = '{}{}'.format(file_name,file_ext)
        cancer = cv2.imread(f,0)
        thresh = threshold(cancer)
        os.rename(f, new_name)
        #cv2.imwrite("sss.jpg",thresh)




        



        
