import numpy as np
import glob
import imageio
import os
from skimage import io
import shutil
from skimage.transform import resize
from skimage.util import img_as_ubyte

def augmentImgs(src,dst,endstyle,charsToremove):
    
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for filename in glob.glob(src + endstyle): 
        
        '''Read image'''
        im = io.imread(filename)

        '''Resize to 256 to save speed'''
        im = resize(im,(256,256))
        im=img_as_ubyte(im) 
        
        '''patchname'''
        imname = os.path.basename(filename)
        patchname = imname[:-charsToremove]
        print(patchname)
        
        '''Augment'''
        im2 = np.fliplr(im)
        im3 = np.flipud(im)
        im4 = np.flipud(im2)
        im5 = np.rot90(im)
        im6 = np.fliplr(im5)
        im7 = np.flipud(im5)
        im8 = np.flipud(im6)
    
        '''save'''   
        imageio.imwrite(dst +str(1)+'_'+str(patchname)+'.png',im)
        imageio.imwrite(dst +str(2)+'_'+str(patchname)+'.png',np.uint8(im2))
        imageio.imwrite(dst +str(3)+'_'+str(patchname)+'.png',np.uint8(im3))
        imageio.imwrite(dst +str(4)+'_'+str(patchname)+'.png',np.uint8(im4))
        imageio.imwrite(dst +str(5)+'_'+str(patchname)+'.png',np.uint8(im5))
        imageio.imwrite(dst +str(6)+'_'+str(patchname)+'.png',np.uint8(im6))
        imageio.imwrite(dst +str(7)+'_'+str(patchname)+'.png',np.uint8(im7))
        imageio.imwrite(dst +str(8)+'_'+str(patchname)+'.png',np.uint8(im8))


