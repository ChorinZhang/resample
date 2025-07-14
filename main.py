# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 09:46:13 2025
downsampling by matrix transformation
@author: YC Zhang
"""

import cv2
import downsampling as ds
import numpy as np
from PIL import Image


if __name__=="__main__":
    
    in_data=np.zeros((180,360))+1
    #img = Image.open("data/images.jpg").convert("L")
    #in_data = np.array(img)  
    out_data=ds.downsampling(in_data,72,144)
    #cv2.imwrite('data/output.png', out_data) 