# Custom-Plotting
[![PyPI version](https://badge.fury.io/py/customplotting.svg)](https://badge.fury.io/py/customplotting) [![Downloads](https://pepy.tech/badge/customplotting)](https://pepy.tech/project/customplotting)

Custom-plotting is a python package written with the aim of producing scientific publication quality figures as quickly as possible with as little code as possible [(checkout examples)](https://github.com/SarthakJariwala/Custom-Plotting/tree/master/examples). 

So instead of typing **8 lines of code** in matplotlib everytime:
```python
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar

"""Plot image"""
plt.figure()
plt.imshow(img_data)
cb = plt.colorbar()
cb.set_label("Height (nm)", fontsize=20, fontweight='bold')
plt.gca().axes.get_yaxis().set_visible(False)
plt.gca().axes.get_xaxis().set_visible(False)
"""Add scalebar"""
scalebar = ScaleBar(dx=0.5, units='nm') # 1 pixel = 0.5 nm
plt.gca().add_artist(scalebar)
```
You only need **1 line of code** to get the same plot: 
```python
from customplotting.mscope import plot_confocal

"""Plot image with scalebar"""
plot_confocal(img_data, stepsize=0.5, units='nm', cbar_label="Height (nm)")
```
**It saves you from a lot of unnecessary typing (if you often plot data)**

The functions wrap around ```matplotlib``` library for plotting with the customizable options. For instance, you can directly add a scalebar to your image without additional code. The figures can customized (colorbar, axis, linewidth, labels, etc) using the same key word arguments as in ```matplotlib```. See function docstrings for more information about customization.

## Install
```
pip install customplotting
```

## Example Usage
```python
"""Make a publishable image with scalebar"""
from customplotting.mscope import plot_confocal
plot_confocal(img_data, stepsize=0.5, units='nm', cbar_label="Height (nm)")
```
![Sample Image](https://github.com/SarthakJariwala/Custom-Plotting/blob/master/examples/MyImage.png)
```python
"""Make a publishable X-Y plot"""
from customplotting.general import plot_xy
plot_xy([1,2,3], [4,5,6], xlabel="Random X", ylabel="Random Y")
```
### Check out the [jupyter notebook for more examples](https://github.com/SarthakJariwala/Custom-Plotting/tree/master/examples)

## Why use?
`Matplotlib` is an **AMAZING** package but if you are like me and are tired of typing 5-7 lines of code everytime you want a good publishable quality figure, then `customplotting` is the answer.

`Customplotting` basically wraps the matplotlib functions to allow you to quickly plot commonly used plots like x-y, images with scalebars, etc with only one line of code.

## What's New?
* Plot X-Y with custom settings (from v0.1.4)
* Scalebar can be added to the plot using a new dependency ```matplotlib_scalebar``` (from v0.1.3)
* For widefield (pixera) plots, scale can automatically be selected by choosing the objective used
* Colorbar can be customized with labels (and also removed if needed)
* X-axis and Y-axis ticks can be added/removed now

## Contribute
Contributions are always welcome! See [CONTRIBUTING.md](https://github.com/SarthakJariwala/Custom-Plotting/tree/master/CONTRIBUTING.md)

## Issues
Open an issue if you come across any!

## License
[MIT License](https://github.com/SarthakJariwala/Custom-Plotting/tree/master/LICENSE)

## Dependencies
* ```matplotlib```
* ```matplotlib_scalar```
* ```numpy```
