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

"""Recylce params for plotting"""
plt.rc('xtick', labelsize = 20)
plt.rc('xtick.major', pad = 3)
plt.rc('ytick', labelsize = 20)
plt.rc('ytick.major', pad = 3)
plt.rc('lines', lw = 1.5, markersize = 7.5)
plt.rc('legend', fontsize = 20)

def plot_confocal(data, FLIM_adjust = True, **kwargs):
    """
    Plot confocal PL intensity image.
    
    Input:
        data: numpy array of PL intensities
        FLIM_adjust: if True, this will plot the image as you see in the FLIM Labview program
        figsize: figure size
        origin: origin of the plot, customisable through matplotlib options
        cmap: matplotlib colormap
        vmin: minimum intensity on the colorscale
        vmax: maximum intensity on the colorscale
        
    """
    
    cmap = kwargs.get('cmap', None)
    vmin = kwargs.get('vmin', None)
    vmax = kwargs.get('vmax', None)
    origin = kwargs.get('origin', None)
    figsize = kwargs.get('figsize', None)
    
    if FLIM_adjust == True:    
        data = np.transpose(data)
        
    plt.figure(figsize=figsize)
    plt.imshow(data, origin = origin, cmap = cmap, vmin = vmin, vmax = vmax)
    plt.colorbar()

def plot_pixera(data, flip_pixera_to_FLIM = True, **kwargs):
    """
    Plot pixera images, with the option to adjust the orientation to FLIM image.
    
    Input:
        data: numpy array of PL intensities
        flip_pixera_to_FLIM: if True, this will plot the image aligned in the same way as the image in FLIM Labview program
        figsize: figure size
        origin: origin of the plot, customisable through matplotlib options
        cmap: matplotlib colormap
        vmin: minimum intensity on the colorscale
        vmax: maximum intensity on the colorscale
        
    """
    
    cmap = kwargs.get('cmap', None)
    vmin = kwargs.get('vmin', None)
    vmax = kwargs.get('vmax', None)
    origin = kwargs.get('origin', None)
    figsize = kwargs.get('figsize', None)
    
    plt.figure(figsize=figsize)
    plt.imshow(data, origin = origin, cmap = cmap, vmin = vmin, vmax=vmax)
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