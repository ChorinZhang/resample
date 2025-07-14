# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 16:35:37 2025
downsampling by matrix transformation
@author: YC Zhang
"""

import cv2
import numpy as np
from PIL import Image


"""
in_data's spatial resolution higher than out_data's spatial resolution
"""
def downsampling(in_data, out_row, out_col):
    in_row=in_data.shape[0]
    in_col=in_data.shape[1]
    
    times_row=in_row/out_row
    times_col=in_col/out_col
    
    #row transformation matrix
    mtx_l=np.zeros((out_row,in_row))
    start_float=0
    lastEndC_int=0
    end_float=times_row-int(times_row)
    for i in range(out_row): 
        if start_float==0:
            lastEndC_int=lastEndC_int-1
        else:
            mtx_l[i,lastEndC_int]=start_float
        
        int_col_num=int(times_row-start_float)
        if int_col_num==0:
            mtx_l[i,lastEndC_int+1]=end_float
        else:
            mtx_l[i,lastEndC_int+1:lastEndC_int+int_col_num+1]=1
        
        end_float=times_row-start_float-int_col_num
        if lastEndC_int+int_col_num+1<in_row:
            mtx_l[i,lastEndC_int+int_col_num+1]=end_float
        
        #update for next round
        lastEndC_int=lastEndC_int+int_col_num+1
        start_float=1-end_float
    
    #colum transformation matrix
    mtx_r=np.zeros((in_col,out_col))
    start_float=0
    lastEndR_int=0
    end_float=times_col-int(times_col)
    for i in range(out_col):  
        if start_float==0:
            lastEndR_int=lastEndR_int-1
        else:
            mtx_r[lastEndR_int,i]=start_float
        
        int_row_num=int(times_col-start_float)
        if int_row_num==0:
            mtx_r[lastEndR_int+1,i]=end_float
        else:
            mtx_r[lastEndR_int+1:lastEndR_int+int_row_num+1,i]=1
        
        end_float=times_col-start_float-int_row_num
        if lastEndR_int+int_row_num+1<in_col:
            mtx_r[lastEndR_int+int_row_num+1,i]=end_float
        
        #update for next round
        lastEndR_int=lastEndR_int+int_row_num+1
        start_float=1-end_float
    
    out_data=np.dot(mtx_l,in_data)
    out_data=np.dot(out_data,mtx_r)
    out_data=out_data/(times_row*times_col)
    
    return out_data
    

if __name__=="__main__":
    #test
    #in_data=np.zeros((5,5))+1
    img = Image.open("images.jpg").convert("L")
    in_data = np.array(img)  
    out_data=downsampling(in_data,72,144)
    
    cv2.imwrite('output.png', out_data) 
        
    

