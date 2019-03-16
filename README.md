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
* Colorbar can be customized with labels
* X-axis and Y-axis ticks can be added/removed now (in dev version)
