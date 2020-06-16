# Custom-Plotting
[![PyPI version](https://badge.fury.io/py/customplotting.svg)](https://badge.fury.io/py/customplotting)

Make pretty plots and images for scientific publishing.

### Check out the jupyter notebook for examples

## Why use?
`Matplotlib` is an **AMAZING** package but if you are like me and are tired of typing 5-7 lines of code everytime to get a good publishable quality figure using matplotlib everytime you want to plot, then `customplotting` is the answer.

`Customplotting` basically wraps the matplotlib functions to allow you to quickly plot commonly used plots like x-y, images with scalebars, etc with only one line of code.

## What's New?
* Plot X-Y with custom settings (from v0.1.4)
* Scalebar can be added to the plot using a new dependency ```matplotlib_scalebar``` (from v0.1.3)
* For widefield (pixera) plots, scale can automatically be selected by choosing the objective used
* Colorbar can be customized with labels (and also removed if needed)
* X-axis and Y-axis ticks can be added/removed now

## Dependencies
* ```matplotlib```
* ```matplotlib_scalar```
* ```numpy```
