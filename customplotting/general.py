import matplotlib.pyplot as plt

def plot_xy(
    x, y,
    new_fig = True,
    **kwargs
    ):

    """
    Plot X-Y data.

    Input:
        x: x data
        y: y data
        new_fig: if True, it will create a new figure to plot data
        label: Legend for the X-Y data
        ls: linestyle (all matplotlib styles)
        lw: lineweight (all matplotlib weights)
        marker: marker type (all matplotlib markerstyles)
        ms: marker size (all matplotlib markersizes)
        figsize: figure size
        xlabel: X-axis label
        ylabel: Y-axis label
        axis_label_fontsize: Fontsize for X and Y-axis labels
        axis_label_fontweight: Fontweight for X and Y-axis labels
    """

    xlabel = kwargs.get('xlabel', None)
    ylabel = kwargs.get('ylabel', None)
    axis_label_fontsize = kwargs.get('axis_label_fontsize', 30)
    axis_label_fontweight = kwargs.get('axis_label_fontweight', 'bold')
    figsize = kwargs.get('figsize', None)

    label = kwargs.get('label', None)
    ls = kwargs.get('ls', '-')
    lw = kwargs.get('lw', 1.5)
    marker = kwargs.get('marker', None)
    ms = kwargs.get('ms', 7)

    if new_fig:
        plt.figure(figsize=figsize)  
        plt.tick_params(direction='out', length=8, width=3.5)
    
    plt.plot(x,y, ls=ls, lw=lw, marker=marker, ms=ms, label=label)
    
    if xlabel is not None:
        plt.xlabel(xlabel, fontsize=axis_label_fontsize, fontweight=axis_label_fontweight)
    if ylabel is not None:
        plt.ylabel(ylabel, fontsize=axis_label_fontsize, fontweight=axis_label_fontweight)
    if label is not None:
        plt.legend()
    plt.tight_layout()