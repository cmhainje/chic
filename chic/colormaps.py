import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap


def make_and_register_smooth(name, colors, bad='#ffffff'):
    """Create a LinearSegmentedColormap from the list of colors and register
    both it and its reverse with matplotlib."""
    cmap = LinearSegmentedColormap.from_list(name, colors)
    cmap.set_bad(bad)
    mpl.colormaps.register(cmap=cmap)
    mpl.colormaps.register(cmap=cmap.reversed(), name=name + '_r')


def make_and_register_discrete(name, colors, bad='#ffffff'):
    """Create a ListedColormap from the list of colors and register
    both it and its reverse with matplotlib."""
    cmap = ListedColormap(colors, name=name)
    cmap.set_bad(bad)
    cmap.set_under(bad)
    cmap.set_over(bad)
    mpl.colormaps.register(cmap=cmap)
    mpl.colormaps.register(cmap=cmap.reversed(), name=name + '_r')
