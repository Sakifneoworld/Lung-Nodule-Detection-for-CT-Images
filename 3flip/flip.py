import os
import cv2
import numpy as np
from matplotlib import pyplot as plt       

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if ( file_ext == ".png"):
        file_name = file_name.strip().zfill(4)
        cancer = cv2.imread(f,0)
        cv2.imshow( "input", cancer)
        cancer = cv2.flip( cancer, 1 )
        cv2.imshow( "Flip", cancer)
        cv2.imwrite(f, cancer)




        



        
