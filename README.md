# Custom-Plotting
[![PyPI version](https://badge.fury.io/py/customplotting.svg)](https://badge.fury.io/py/customplotting)

Custom-plotting is a Python package with the aim of producing publication quality fluorescence microscopy data. The functions wrap around ```matplotlib``` library for plotting with the option to add a scalebar directly to the image using ```matplotlib_scalebar```. The images can customized (colorbar, axis, etc) using the same key word arguments as in ```matplotlib```. See function docstring for more information about customization.

The primary users for this Python package are Ginger Lab members at the University of Washington, Seattle but is licensed under MIT License and open for everyone to use.

## Install
```
pip install customplotting
```

### Check out the jupyter notebook for examples

## Why use?
`Matplotlib` is an **AMAZING** package but if you are like me and are tired of typing 5-7 lines of code everytime you want a good publishable quality figure, then `customplotting` is the answer.

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
