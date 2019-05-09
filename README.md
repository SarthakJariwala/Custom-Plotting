# Custom-Plotting
[![PyPI version](https://badge.fury.io/py/customplotting.svg)](https://badge.fury.io/py/customplotting)

Custom-plotting is a Python package with the aim of producing publication quality fluorescence microscopy data. The functions wrap around ```matplotlib``` library for plotting with the option to add a scalebar directly to the image using ```matplotlib_scalebar```. The images can customized (colorbar, axis, etc) using the same key word arguments as in ```matplotlib```. See function docstring for more information about customization.

The primary users for this Python package are Ginger Lab members at the University of Washington, Seattle but is licensed under MIT License and open for everyone to use.

## Install
```
pip install customplotting==0.1.4.dev0
```
Version 0.1.4.dev0 is the most stable release with all the functionalities.

## Usage
```
import customplotting.mscope as cpm

cpm.plot_confocal(data, figsize = (10,10), origin = 'lower', cmap = 'inferno', vmin = 0, vmax = 1000)
```
## What's New?
* Scalebar can be added to the plot using a new dependency ```matplotlib_scalebar```
* For widefield (pixera) plots, scale can automatically be selected by choosing the objective used
* Colorbar can be customized with labels (and also removed if needed)
* X-axis and Y-axis ticks can be added/removed now

## Dependencies
* ```matplotlib```
* ```matplotlib_scalebar```
* ```opencv-python```
* ```numpy```
