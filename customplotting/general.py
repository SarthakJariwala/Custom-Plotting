import matplotlib.pyplot as plt

def _check_dict(dictionary):
    if not isinstance(dictionary, dict):
        raise ValueError(f"{dictionary} must be a dictionary")


def _setup_figure(new_fig=True, figsize=None, title=None,
                  fontdict=None, tick_parameters=None):
    """Wrapper to setup figure with the desired parameters"""
    if new_fig:
        plt.figure(figsize=figsize)
        if tick_parameters is None: # setup some defaults
            tick_parameters = {}
        
        _check_dict(tick_parameters)
        
        tick_parameters.setdefault('direction', 'out')
        tick_parameters.setdefault('length', 8)
        tick_parameters.setdefault('width', 3.5)
        
        plt.tick_params(**tick_parameters)
    
    if fontdict is None:
        fontdict={}
    
    _check_dict(fontdict)
    
    fontdict.setdefault('fontsize', 30)
    fontdict.setdefault('fontweight', 'bold')

    if title is not None:
        plt.title(
            title,
            fontdict=fontdict)


def _setup_labels(xlabel=None, ylabel=None, label=None, fontdict=None):

    if fontdict is None:
        fontdict={}
    
    _check_dict(fontdict)

    fontdict.setdefault('fontsize', 25)
    fontdict.setdefault('fontweight', 'bold')

    if xlabel is not None:
        plt.xlabel(
            xlabel, fontdict=fontdict)

    if ylabel is not None:
        plt.ylabel(
            ylabel, fontdict=fontdict)

    if label is not None:
        plt.legend()


def plot_xy(
    *args,
    new_fig=True,
    figsize=None,
    tick_parameters=None,
    xlabel=None,
    ylabel=None,
    ax_fontdict=None,
    title=None,
    title_fontdict=None,
    **kwargs
):
    """
    Plot x-y data with specified parameters.

    Parameters
    ----------
    x, y : array-like or scalar
            The horizontal / vertical coordinates of the data points.
            *x* values are optional and default to `range(len(y))`.

            Commonly, these parameters are 1D arrays.

            They can also be scalars, or two-dimensional (in that case, the
            columns represent separate data sets).

            These arguments cannot be passed as keywords.
    
    new_fig : bool
        Create a new matplotlib figure. Default is True
    
    figsize: iterable, optional
        Figure size
    
    xlabel, ylabel: str, optional
        X-axis and Y-axis label
    
    ax_fontdict: dict, optional
        Font dictionary for X and Y axis labels
        
    title: str, optional
        Title for the plot
    
    title_fontdict: dict, optional
        Font dictionary for plot title

    Other Paramters
    ---------------
    **kwargs: optional
        All `matplotlib.pyplot.plot` kwargs used to specify line label (for
        auto legends), linewidth, antialiasing, marker face color.
    """

    label = kwargs.get('label', None)

    _setup_figure(
        new_fig=new_fig,
        figsize=figsize,
        title=title,
        fontdict=title_fontdict,
        tick_parameters=tick_parameters)

    plt.plot(*args, **kwargs)

    _setup_labels(xlabel, ylabel, label, fontdict=ax_fontdict)

    plt.tight_layout()


def save_fig(filename, dpi=300):
    """Save figure

    Input:
        filename: filename with path where the figure will be saved
        dpi: default 300
    """
    plt.savefig(filename, bbox_inches='tight', dpi=dpi)
