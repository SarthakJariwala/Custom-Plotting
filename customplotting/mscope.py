# -*- coding: utf-8 -*-
"""
@author: Sarthak
"""

import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
from customplotting.images import plot_image
from customplotting import join_doc_style
from custom_inherit import doc_inherit
import warnings


@doc_inherit(plot_image, style=join_doc_style)
def plot_confocal(
        data,
        *args,
        new_fig=True,
        figsize=None,
        scalebar=True,
        stepsize=0.1,
        units='um',
        scalebar_params=None,
        colorbar=True,
        cbar_label="PL Intensity (a.u.)",
        cbar_fontdict=None,
        ticks_visible=False,
        title=None,
        title_fontdict=None,
        FLIM_adjust=False,
        **kwargs):
    """
    FLIM_adjust: (Deprecated)
    """

    if FLIM_adjust:
        warnings.simplefilter('always', DeprecationWarning)
        warnings.warn(
            "FLIM_adjust has been deprecated starting v0.1.5. Enter transformed data as input instead",
            DeprecationWarning)

    plot_image(
        data,
        *args,
        new_fig=new_fig,
        figsize=figsize,
        scalebar=scalebar,
        stepsize=stepsize,
        units=units,
        scalebar_params=scalebar_params,
        colorbar=colorbar,
        cbar_label=cbar_label,
        cbar_fontdict=cbar_fontdict,
        ticks_visible=ticks_visible,
        **kwargs
    )


@doc_inherit(plot_image, style=join_doc_style)
def plot_pixera(
        data,
        *args,
        new_fig=True,
        figsize=None,
        scalebar=True,
        obj=None,
        size_per_pixel=None,
        units='um',
        scalebar_params=None,
        colorbar=True,
        cbar_label="PL Intensity (a.u.)",
        cbar_fontdict=None,
        ticks_visible=False,
        title=None,
        title_fontdict=None,
        flip_pixera_to_FLIM=False,
        **kwargs):
    """
    Plot images taken with pixera camera

    size_per_pixel: float, optional
        Physical size per camera pixel

    flip_pixera_to_FLIM: (Deprecated)
        Transformations can be performed outside using:
        >>> plt.gca().invert_xaxis()
        >>> plt.gca().invert_yaxis()
    """

    if scalebar:
        if obj == "100x":
            size_per_pixel = 0.02  # 1 pixel = 0.02 um for pixera (100x)
        elif obj == "50x":
            size_per_pixel = 0.04  # 1 pixel = 0.04 um for pixera (50x)
        elif obj is None:
            if size_per_pixel is None:
                warnings.warn(
                    "size_per_pixel was not set. Using default value of 0.1"
                )
                size_per_pixel = 0.1  # using default

    plot_image(
        data,
        *args,
        new_fig=new_fig,
        figsize=figsize,
        scalebar=scalebar,
        stepsize=size_per_pixel,
        units=units,
        scalebar_params=scalebar_params,
        colorbar=colorbar,
        cbar_label=cbar_label,
        cbar_fontdict=cbar_fontdict,
        ticks_visible=ticks_visible,
        **kwargs
    )

    if flip_pixera_to_FLIM:
        warnings.simplefilter('always', DeprecationWarning)
        warnings.warn(
            """flip_pixera_to_FLIM has been deprecated starting v0.1.5.
Transformations can be performed outside using :
>>> plt.gca().invert_xaxis()
>>> plt.gca().invert_yaxis()
""",
            DeprecationWarning
        )
