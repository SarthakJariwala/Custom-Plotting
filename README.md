# Custom-Plotting
[![PyPI version](https://badge.fury.io/py/customplotting.svg)](https://badge.fury.io/py/customplotting)

Custom plotting wrapper functions for scientific plotting

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
* ```matplotlib_scalar```
* ```opencv-python```
* ```numpy```
