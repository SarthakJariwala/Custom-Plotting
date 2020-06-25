"""
@author: Sarthak
"""

import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
from customplotting.general import _check_dict


def _setup_figure(new_fig=True, figsize=None, title=None,
                  fontdict=None):
    """Wrapper to setup image with the desired parameters"""
    if new_fig:
        plt.figure(figsize=figsize)

    if fontdict is None:
        fontdict = {}

    _check_dict(fontdict)

    fontdict.setdefault('fontsize', 30)
    fontdict.setdefault('fontweight', 'bold')

    if title is not None:
        plt.title(
            title,
            fontdict=fontdict)


def _setup_scalebar(stepsize=0.1, units='um', scalebar_params=None):

    # default is 100 nm stepsize
    if scalebar_params is None:
        scalebar_params = {}

    scalebar_params.setdefault('color', 'white')
    scalebar_params.setdefault('height_fraction', 0.05)
    scalebar_params.setdefault('length_fraction', 0.3)
    scalebar_params.setdefault('scale_loc', "top")
    scalebar_params.setdefault('location', "lower right")
    scalebar_params.setdefault('box_alpha', 0)

    _check_dict(scalebar_params)

    color = scalebar_params.get('color')
    height_fraction = scalebar_params.get('height_fraction')
    length_fraction = scalebar_params.get('length_fraction')
    scale_loc = scalebar_params.get('scale_loc')
    location = scalebar_params.get('location')
    box_alpha = scalebar_params.get('box_alpha')

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


def plot_image(
        data,
        *args,
        new_fig=True,
        figsize=None,
        scalebar=True,
        stepsize=0.1,
        units='um',
        scalebar_params=None,
        colorbar=True,
        cbar_label=None,
        cbar_fontdict=None,
        ticks_visible=False,
        title=None,
        title_fontdict=None,
        **kwargs):
    """
    Plot image data.

    Parameters
    ----------
    data: array-like or PIL image
        Image data.

        Supported array shapes are all `matplotlib.pyplot.imshow` array shapes:

        From `matplotlib.pyplot.imshow`:
            - (M, N): an image with scalar data. The values are mapped to
                colors using normalization and a colormap. See parameters *norm*,
                *cmap*, *vmin*, *vmax*.
            - (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
            - (M, N, 4): an image with RGBA values (0-1 float or 0-255 int),
                i.e. including transparency.

        The first two dimensions (M, N) define the rows and columns of
        the image.

    new_fig : bool, default: True
        Create a new matplotlib figure. Default is True

    figsize: iterable, optional
        Figure size

    scalebar: bool, default: True
        Add a scale bar to the image.
        scalebar parameters can be changed using the following arguments:

        stepsize: what is 1 pixel equal to? (default: 0.1 um)

        units: units according to SI system (default: 'um')

        scalebar_params: dict, optional
            scalebar parameters that can be used to change the look of the scalebar

            color: color of scale bar (default: 'white')

            height_fraction: height fraction of scale bar as a fraction of axes' height (default: 0.05)

            length_fraction: length fraction of scale bar as a fraction of the axes' width (default: 0.3)

            scale_loc: location of the scale (default: 'top')

            location: location of scalebar w.r.t. image (default: 'lower right')

            box_alpha: transparency of box (default: 0)

            Refer to https://github.com/ppinard/matplotlib-scalebar for more details

    colorbar: bool, default: True
        Plot colorbar for the image.

    cbar_label: str, optional
        Label for colorbar

    cbar_fontdict: dict, optional
        Font dictionary for colorbar
        defaults: {'fontsize':25, 'fontweight':'bold'}

    Other Paramters
    ---------------
    **kwargs: optional
        All `matplotlib.pyplot.imshow` kwargs to set colormap,
        min-max ranges (vmin, vmax), alpha, etc.
    """

    _setup_figure(
        new_fig=new_fig,
        figsize=figsize,
        title=title,
        fontdict=title_fontdict)

    plt.imshow(data, *args, **kwargs)

    if scalebar:
        _setup_scalebar(stepsize, units, scalebar_params=scalebar_params)

    if colorbar:

        cb = plt.colorbar()

        if cbar_fontdict is None:
            cbar_fontdict = {}

        _check_dict(cbar_fontdict)

        cbar_fontdict.setdefault('fontsize', 25)
        cbar_fontdict.setdefault('fontweight', 'bold')

        if cbar_label is not None:
            cb.set_label(cbar_label, fontdict=cbar_fontdict)

    if not ticks_visible:
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.gca().axes.get_xaxis().set_visible(False)
