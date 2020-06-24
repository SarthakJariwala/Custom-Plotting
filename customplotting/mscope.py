# -*- coding: utf-8 -*-
"""
@author: Sarthak
"""

import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import warnings

def plot_image(
        data,
        *args,
        new_fig=True,
        scalebar=True,
        colorbar=True,
        ticks_visible=False,
        **kwargs):
    """
    Plot image data.

    Input:
        data: numpy array of PL intensities
        new_fig: if True, it will create a new figure to plot data
        scalebar: if True, this will add a scale bar to the image. The default setting is for 0.1um stepsize, but can be changed using the following arguments:
            stepsize: what is 1 pixel equal to? (default: 0.1 um)
            units: units according to SI system (default: um)
            color: color of scale bar (default: white)
            height_fraction: height fraction of scale bar as a fraction of axes' height (default: 0.05)
            length_fraction: length fraction of scale bar as a fraction of the axes' width (default: 0.3)
            scale_loc: location of the scale (default: top)
            location: location of scalebar w.r.t. image (default: lower right)
            box_alpha: transparency of box (default: 0)
            Refer to https://github.com/ppinard/matplotlib-scalebar for more details
        colorbar: if True, this will plot colorbar for the image. Label can be set using:
            cbar_label: colorbar label, must be string. (default: "PL Intensity (a.u.)")
        figsize: figure size
        **kwargs: All matplotlib "imshow" kwargs

    """

    figsize = kwargs.get('figsize', None)

    if new_fig:
        plt.figure(figsize=figsize)
    plt.imshow(data, *args, **kwargs)

    if scalebar:
        stepsize = kwargs.get('stepsize', 0.1)  # default is 100 nm stepsize
        units = kwargs.get('units', 'um')
        color = kwargs.get('color', 'white')
        height_fraction = kwargs.get('height_fraction', 0.05)
        length_fraction = kwargs.get('length_fraction', 0.3)
        scale_loc = kwargs.get('scale_loc', "top")
        location = kwargs.get('location', "lower right")
        box_alpha = kwargs.get('box_alpha', 0)
        
        scalebar = ScaleBar(
            dx=stepsize,
            units=units,
            color=color,
            height_fraction=height_fraction,
            length_fraction=length_fraction,
            scale_loc=scale_loc,
            location=location,
            box_alpha=box_alpha,
            font_properties=dict(
                size='x-large',
                weight='bold'))
        plt.gca().add_artist(scalebar)

    if colorbar:
        cbar_label = kwargs.get('cbar_label', "PL Intensity (a.u.)")
        cb = plt.colorbar()
        cb.set_label(cbar_label, fontsize=20, fontweight='bold')

    if not ticks_visible:
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.gca().axes.get_xaxis().set_visible(False)


def plot_confocal(
        data,
        new_fig=True,
        FLIM_adjust=False,
        scalebar=True,
        colorbar=True,
        ticks_visible=False,
        **kwargs):
    """
    Plot confocal PL intensity image.

    Input:
        data: numpy array of PL intensities
        new_fig: if True, it will create a new figure to plot data
        FLIM_adjust: (Deprecated) if True, this will plot the image as you see in the FLIM Labview program
        scalebar: if True, this will add a scale bar to the image. The default setting is for 0.1um stepsize, but can be changed using the following arguments:
            stepsize: what is 1 pixel equal to? (default: 0.1 um)
            units: units according to SI system (default: um)
            color: color of scale bar (default: white)
            height_fraction: height fraction of scale bar as a fraction of axes' height (default: 0.05)
            length_fraction: length fraction of scale bar as a fraction of the axes' width (default: 0.3)
            scale_loc: location of the scale (default: top)
            location: location of scalebar w.r.t. image (default: lower right)
            box_alpha: transparency of box (default: 0)
            Refer to https://github.com/ppinard/matplotlib-scalebar for more details
        colorbar: if True, this will plot colorbar for the image. Label can be set using:
            cbar_label: colorbar label, must be string. (default: "PL Intensity (a.u.)")
        figsize: figure size
        **kwargs: All matplotlib "imshow" kwargs

    """

    figsize = kwargs.get('figsize', None)

    if FLIM_adjust:
        warnings.simplefilter('always', DeprecationWarning)
        warnings.warn(
            "FLIM_adjust has been deprecated starting v0.1.5. Enter transformed data as input instead", 
            DeprecationWarning
        )

    if new_fig:
        plt.figure(figsize=figsize)
    plt.imshow(data, **kwargs)

    if scalebar:
        stepsize = kwargs.get('stepsize', 0.1)  # default is 100 nm stepsize
        units = kwargs.get('units', 'um')
        color = kwargs.get('color', 'white')
        height_fraction = kwargs.get('height_fraction', 0.05)
        length_fraction = kwargs.get('length_fraction', 0.3)
        scale_loc = kwargs.get('scale_loc', "top")
        location = kwargs.get('location', "lower right")
        box_alpha = kwargs.get('box_alpha', 0)
        
        scalebar = ScaleBar(
            dx=stepsize,
            units=units,
            color=color,
            height_fraction=height_fraction,
            length_fraction=length_fraction,
            scale_loc=scale_loc,
            location=location,
            box_alpha=box_alpha,
            font_properties=dict(
                size='x-large',
                weight='bold'))
        plt.gca().add_artist(scalebar)

    if colorbar:
        cbar_label = kwargs.get('cbar_label', "PL Intensity (a.u.)")
        cb = plt.colorbar()
        cb.set_label(cbar_label, fontsize=20, fontweight='bold')

    if not ticks_visible:
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.gca().axes.get_xaxis().set_visible(False)


def plot_pixera(
        data,
        new_fig=True,
        obj=None,
        flip_pixera_to_FLIM=False,
        scalebar=True,
        colorbar=True,
        ticks_visible=False,
        **kwargs):
    """
    Plot pixera images, with the option to adjust the orientation to FLIM image.

    Input:
        data: numpy array of PL intensities
        new_fig: if True, it will create a new figure to plot data
        obj: objective used for the measurement, "100x" or "50x" (default: None). When default value is selected, size_per_pixel can be updated to the value of choice. If no value is provided when obj is set to default (None), the 100x objective scale will be implemented.
        flip_pixera_to_FLIM: (Deprecated) if True, this will plot the image aligned in the same way as the image in FLIM Labview program
        scalebar: if True, this will add a scale bar to the image. The default setting is for 100x, but can be changed using the following arguments:
            size_per_pixel: what is 1 pixel equal to? (default: 0.02, 100x obj value)
            units: units according to SI system (default: um)
            color: color of scale bar (default: white)
            height_fraction: height fraction of scale bar as a fraction of axes' height (default: 0.05)
            length_fraction: length fraction of scale bar as a fraction of the axes' width (default: 0.3)
            scale_loc: location of the scale (default: top)
            location: location of scalebar w.r.t. image (default: lower right)
            box_alpha: transparency of box (default: 0)
            Refer to https://github.com/ppinard/matplotlib-scalebar for more details
        colorbar: if True, this will plot colorbar for the image. Label can be set using:
            cbar_label: colorbar label, must be string. (default: "PL Intensity (a.u.)")
        ticks_visible: if False, it will remove xaxis and yaxis ticks
        figsize: figure size
        **kwargs: all matplotlib "imshow" kwargs

    """

    figsize = kwargs.get('figsize', None)

    if new_fig:
        plt.figure(figsize=figsize)
    plt.imshow(data, **kwargs)

    if scalebar:
        if obj == "100x":
            size_per_pixel = 0.02  # 1 pixel = 0.02 um for pixera (100x)
        elif obj == "50x":
            size_per_pixel = 0.04  # 1 pixel = 0.04 um for pixera (50x)
        elif obj is None:
            print(
                "Using 100x Objective defualt. Define size_per_pixel if you want to change it")
            size_per_pixel = kwargs.get(
                'size_per_pixel', 0.02)  # default is 100x objective value
        units = kwargs.get('units', 'um')
        color = kwargs.get('color', 'white')
        height_fraction = kwargs.get('height_fraction', 0.05)
        length_fraction = kwargs.get('length_fraction', 0.3)
        scale_loc = kwargs.get('scale_loc', "top")
        location = kwargs.get('location', "lower right")
        box_alpha = kwargs.get('box_alpha', 0)
        scalebar = ScaleBar(
            dx=size_per_pixel,
            units=units,
            color=color,
            height_fraction=height_fraction,
            length_fraction=length_fraction,
            scale_loc=scale_loc,
            location=location,
            box_alpha=box_alpha,
            font_properties=dict(
                size='x-large',
                weight='bold'))
        plt.gca().add_artist(scalebar)

    if colorbar:
        cbar_label = kwargs.get('cbar_label', "PL Intensity (a.u.)")
        cb = plt.colorbar()
        cb.set_label(cbar_label, fontsize=20, fontweight='bold')

    if flip_pixera_to_FLIM:
        warnings.simplefilter('always', DeprecationWarning)
        warnings.warn(
            """flip_pixera_to_FLIM has been deprecated starting v0.1.5. 
Transformations can be performed outside using :
>>> plt.gca().invert_xaxis()
>>> plt.gca().invert_yaxis()
""", 
            DeprecationWarning
        )
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()

    if not ticks_visible:
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.gca().axes.get_xaxis().set_visible(False)
