import matplotlib.pyplot as plt


def plot_xy(
    x, y,
    new_fig=True,
    **kwargs
):
    """
    Plot X-Y data.

    Input:
        x: x data
        y: y data
        new_fig: if True, it will create a new figure to plot data
        figsize: figure size
        xlabel: X-axis label
        ylabel: Y-axis label
        axis_label_fontsize: Fontsize for X and Y-axis labels
        axis_label_fontweight: Fontweight for X and Y-axis labels
        title: plot title
        **kwargs: all matplotlib "plot" kwargs
    """

    xlabel = kwargs.get('xlabel', None)
    ylabel = kwargs.get('ylabel', None)
    axis_label_fontsize = kwargs.get('axis_label_fontsize', 30)
    axis_label_fontweight = kwargs.get('axis_label_fontweight', 'bold')
    figsize = kwargs.get('figsize', None)
    title = kwargs.get('title', None)

    label = kwargs.get('label', None)

    if new_fig:
        plt.figure(figsize=figsize)
        plt.tick_params(direction='out', length=8, width=3.5)

    plt.plot(x, y, **kwargs)

    if xlabel is not None:
        plt.xlabel(
            xlabel,
            fontsize=axis_label_fontsize,
            fontweight=axis_label_fontweight)
    
    if ylabel is not None:
        plt.ylabel(
            ylabel,
            fontsize=axis_label_fontsize,
            fontweight=axis_label_fontweight)
    
    if label is not None:
        plt.legend()
    
    if title is not None:
        plt.title(
            title,
            fontsize=axis_label_fontsize,
            fontweight=axis_label_fontweight)
    plt.tight_layout()

def save_fig(filename, dpi=300):
    """Save figure

    Input:
        filename: filename with path where the figure will be saved
        dpi: default 300
    """
    plt.savefig(filename, bbox_inches='tight', dpi=dpi)