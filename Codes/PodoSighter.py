# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:55:39 2021

@author: Darshana Govind (d8@buffalo.edu)
"""

import os


'''User-defined inputs'''
'''=================='''


# %%
'''Files'''
inputImageFile = '../Data/PAS_WSI/JPH12.svs' #Image file to be analyzed
inputAnnotationFile1= '../Data/Glomxml/JPH12.xml'#Glomerulus annotation
outputAnnotationFile='out.xml'#Output podocyte xml name
tempfolder = '/hdd/d8/newtemp/tmp/' #Specify a temporary folder where the images will be cropped to and tested. This folder will be automatically created and deleted during analysis

if not os.path.exists(tempfolder):
    os.makedirs(tempfolder)


# %%
'''Trained models for Pix2pix'''
#TrainedGeneratorModel = '../Data/Trained_models/pix2pix/human_p57/hum_p57_net_G.pth'
#TrainedDiscriminatorModel = '../Data/Trained_models/pix2pix/human_p57/hum_p57_net_D.pth'
'''OR'''
#'''Trained models for CNN'''
Model = '../Data/Trained_models/cnn/human_p57/hum_p57_model.ckpt-50000.data-00000-of-00001'
Modelchkpt = '../Data/Trained_models/cnn/human_p57/hum_p57_checkpoint'
Modelidx = '../Data/Trained_models/cnn/human_p57/hum_p57_model.ckpt-50000.index'



# %%
'''Parameters'''
PASnucleiThreshold = 0.4
gauss_filt_size = 5
Disc_size = 6
species='human'
gpu_id=0
resolution=0
size_thre=400
watershed_thre=0.2




# %%
'''Method'''
METHOD = 'CNN' # 'CNN' or 'pix2pix'



# %%


'''RUNNING...'''
'''=========='''

if METHOD == 'pix2pix':
    cmd = "python3 ./PodoSighter_pix2pix_folder/Complete_Pix2pix_Prediction.py -A0 '{}' -A1 '{}' -A2 '{}' -A3 '{}' -A4 '{}' -A5 {} -A6 {} -A7 {} -A8 '{}' -A9 {} -A10 {} -A11 {} -A12 {} -A13 '{}'".format(tempfolder,inputImageFile,inputAnnotationFile1, TrainedGeneratorModel ,TrainedDiscriminatorModel, PASnucleiThreshold,gauss_filt_size, Disc_size ,species,gpu_id,resolution,size_thre,watershed_thre,outputAnnotationFile)
    os.system(cmd)
elif METHOD == 'CNN':
    cmd = "python3 ./PodoSighter_cnn_folder/Complete_CNN_Prediction.py -A0 '{}' -A1 '{}' -A2 '{}' -A3 '{}' -A4 '{}' -A5 '{}' -A6 '{}' -A7 {} -A8 {} -A9 {} -A10 {} -A11 {} -A12 {} -A13 '{}'".format(tempfolder,inputImageFile,inputAnnotationFile1, Model,Modelchkpt,Modelidx, species, PASnucleiThreshold,gauss_filt_size, Disc_size,resolution,size_thre,watershed_thre,outputAnnotationFile)
    os.system(cmd)    
