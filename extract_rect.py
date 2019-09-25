# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:44:47 2019

@author: chxy + zwzhang
"""

import cv2
import os.path as osp

###########################################################################################

# read path and save path
save_path = './asserts'
read_path = './testset'

# utilized models name 
model_name = ['MSRResNetx4_res16', 'MSRGANx4_res1_pw0', 'MSRGANx4_res4', 'MSRGANx4_res8', 'MSRGANx4_res16', 'RRDB_ESRGAN_x4']
num_model = len(model_name)

# tested img
test_img = 'HR_test.png'

# The HR image of model 'MSRResNetx4_res16' is named 'MSRResNetx4_res16_test.png'.

###########################################################################################

# load imgs 
imgs = []
imgs.append(cv2.imread(osp.join(read_path, test_img)))
img_name = test_img.split('_')[1]
for i in range(num_model):
    imgs.append(cv2.imread(osp.join(read_path, model_name[i] + '_' + img_name)))

model_name.insert(0, 'HR')

def on_mouse(event, x, y, flags, param):
    
    global point1, point2
    img = imgs[0].copy()
    
    if event == cv2.EVENT_LBUTTONDOWN:    # 左键点击
        point1 = (x,y)    # 起点
        cv2.circle(img, point1, 10, (0,255,0), 5)
        cv2.imshow('image', img)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):    # 按住左键拖曳
        cv2.rectangle(img, point1, (x, y), (255,0,0), 5)
        cv2.imshow('image', img)
    elif event == cv2.EVENT_LBUTTONUP:    # 左键释放
        point2 = (x,y)    # 终点
        cv2.rectangle(img, point1, point2, (0,0,255), 3)
        cv2.imshow('image', img)
        for i in range(len(imgs)):
            img_result = imgs[i].copy()
            
            min_x = min(point1[0], point2[0])     
            min_y = min(point1[1], point2[1])
            width = abs(point1[0] - point2[0])
            height = abs(point1[1] -point2[1])
            
            # 将矩形截取的内容输出
            rect = img_result[min_y:min_y+height+1, min_x:min_x+width+1]
            cv2.imwrite(osp.join(save_path, model_name[i] + '_rect.png'), rect)
            
            # 将图片与矩形框同时输出
            cv2.rectangle(img_result, point1, point2, (0,0,255), 2) 
            cv2.imwrite(osp.join(save_path, model_name[i] + '_with_rect.png'), img_result)
            
            # 将矩形截取的特征放大scale倍置于图片右下角输出，未考虑重叠情况
            scale = 3
            img_result[img_result.shape[0] - scale * (1+height) : img_result.shape[0], 
            img_result.shape[1] - scale * (1+width) : img_result.shape[1]] = cv2.resize(rect, (0, 0), fx=scale, fy=scale)
            cv2.imwrite(osp.join(save_path, model_name[i] + '_with_fea.png'), img_result)
        		
def main():

	cv2.namedWindow('image')
	cv2.setMouseCallback('image', on_mouse)
	cv2.imshow('image', imgs[0])
	cv2.waitKey(0)

if __name__ == '__main__':
	main()