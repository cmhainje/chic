import matplotlib as mpl

from .tol import schemes as tol_schemes


schemes = dict()
schemes.update(tol_schemes)


def set_default(scheme):
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', schemes[scheme])


def make_colormap_from_scheme(scheme, N=None, bad=None):
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(schemes[scheme], name=scheme, N=N)
    if bad is None:
        bad = '#DDDDDD' if scheme == 'tol_muted' else '#FFFFFF'
    cmap.set_bad(bad)
    cmap.set_under(bad)
    cmap.set_over(bad)
    return cmap
