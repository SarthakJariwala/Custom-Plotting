import matplotlib.pyplot as plt

font = {'family' : 'arial',
        'weight' : 'bold',
        'size'   : 20}

"""Recylce params for plotting"""
plt.rc('xtick', labelsize=20)
plt.rc('xtick.major', pad=3)
plt.rc('ytick', labelsize=20)
plt.rc('ytick.major', pad=3)
plt.rc('lines', lw=1.5, markersize=7.5)
plt.rc('legend', fontsize=20)
plt.rc('axes', linewidth=3.5)
plt.rc('font', **font)


def join_doc_style(parent_doc, child_doc):
        return "\n      -----".join([parent_doc, child_doc])