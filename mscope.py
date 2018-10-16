# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:16:26 2018

@author: Sarthak
"""

import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import cv2

def plot_confocal(data, FLIM_adjust = True, **kwargs):
    """
    Plot confocal PL intensity image.
    
    Input:
        data: numpy array of PL intensities
        FLIM_adjust: if True, this will plot the image as you see in the FLIM Labview program
        size: figure size
        ori: origin of the plot, customisable through matplotlib options
        color_map: matplotlib colormap
        min_int: minimum intensity on the colorscale
        max_int: maximum intensity on the colorscale
        
    """
    
    color_map = kwargs.get('color_map', None)
    min_int = kwargs.get('min_int', None)
    max_int = kwargs.get('max_int', None)
    ori = kwargs.get('ori', None)
    size = kwargs.get('size', None)
    
    if FLIM_adjust == True:    
        data = np.transpose(data)
        
    plt.figure(figsize=size)
    plt.imshow(data, origin = ori, cmap = color_map, vmin = min_int, vmax=max_int)
    plt.colorbar()

def plot_pixera(data, flip_pixera_to_FLIM = True, **kwargs):
    """
    Plot pixera images, with the option to adjust the orientation to FLIM image.
    
    Input:
        data: numpy array of PL intensities
        flip_pixera_to_FLIM: if True, this will plot the image aligned in the same way as the image in FLIM Labview program
        size: figure size
        ori: origin of the plot, customisable through matplotlib options
        color_map: matplotlib colormap
        min_int: minimum intensity on the colorscale
        max_int: maximum intensity on the colorscale
        
    """
    
    color_map = kwargs.get('color_map', None)
    min_int = kwargs.get('min_int', None)
    max_int = kwargs.get('max_int', None)
    ori = kwargs.get('ori', None)
    size = kwargs.get('size', None)
    
    plt.figure(figsize=size)
    plt.imshow(data, origin = ori, cmap = color_map, vmin = min_int, vmax=max_int)
    plt.colorbar()
    
    if flip_pixera_to_FLIM == True:
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()
    
def Diffusion_plotting(diff_img_path, total_grains, save = False, norm = False):
    
    assert type(total_grains) == int, ('Must be integer') 
    
    filelist = glob.glob(diff_img_path+'/*.tif')
    
    if norm == False:
        intensity = 255
    
    i = 1
    for filename in filelist:
        
        img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
        img = img[590:740, 280:430]
        
        plot_pixera(img, flip_pixera_to_FLIM=True, color_map = 'inferno', max_int = intensity)
        plt.title('Grain #'+filename[-6]+filename[-5], fontsize = 25)
        
        if save == True:
            directory = diff_img_path + '/GrainDiffusion_plotted'
            if not os.path.exists(directory):
                os.makedirs(directory)
            #plt.savefig(directory + '/' +'Grain_%.f.tiff' %(i), bbox_inches = 'tight', dpi = 300)
            plt.savefig(directory + '/' +'Grain_'+filename[-6]+filename[-5]+'.tiff', bbox_inches = 'tight', dpi = 300)
            plt.close()
        i +=1
        
        if i == total_grains + 1:
            break
        else: 
            continue
    
    return