import matplotlib as mpl
from matplotlib.colors import ListedColormap

from ..colormaps import make_and_register_smooth, make_and_register_discrete


# *** Diverging ***

make_and_register_smooth('tol_sunset', [
    '#364B9A',
    '#4A7BB7',
    '#6EA6CD',
    '#98CAE1',
    '#C2E4EF',
    '#EAECCC',
    '#FEDA8B',
    '#FDB366',
    '#F67E4B',
    '#DD3D2D',
    '#A50026',
], bad='#FFFFFF')

make_and_register_smooth('tol_nightfall', [
    '#125A56',
    '#00767B',
    '#238F9D',
    '#42A7C6',
    '#60BCE9',
    '#9DCCEF',
    '#C6DBED',
    '#DEE6E7',
    '#ECEADA',
    '#F0E6B2',
    '#F9D576',
    '#FFB954',
    '#FD9A44',
    '#F57634',
    '#E94C1F',
    '#D11807',
    '#A01813'
], bad='#FFFFFF')

make_and_register_smooth('tol_BuRd', [
    '#2166AC',
    '#4393C3',
    '#92C5DE',
    '#D1E5F0',
    '#F7F7F7',
    '#FDDBC7',
    '#F4A582',
    '#D6604D',
    '#B2182B',
], bad='#FFEE99')

make_and_register_smooth('tol_PRGn', [
    '#762A83',
    '#9970AB',
    '#C2A5CF',
    '#E7D4E8',
    '#F7F7F7',
    '#D9F0D3',
    '#ACD39E',
    '#5AAE61',
    '#1B7837',
], bad='#FFEE99')


# *** Sequential ***

make_and_register_smooth('tol_YlOrBr', [
    '#FFFFE5',
    '#FFF7BC',
    '#FEE391',
    '#FEC44F',
    '#FB9A29',
    '#EC7014',
    '#CC4C02',
    '#993404',
    '#662506',
], bad='#888888')

make_and_register_smooth('tol_iridescent', [
    '#FEFBE9',
    '#FCF7D5',
    '#F5F3C1',
    '#EAF0B5',
    '#DDECBF',
    '#D0E7CA',
    '#C2E3D2',
    '#B5DDD8',
    '#A8D8DC',
    '#9BD2E1',
    '#8DCBE4',
    '#81C4E7',
    '#7BBCE7',
    '#7EB2E4',
    '#88A5DD',
    '#9398D2',
    '#9B8AC4',
    '#9D7DB2',
    '#9A709E',
    '#906388',
    '#805770',
    '#684957',
    '#46353A',
], bad='#999999')

make_and_register_smooth('tol_incandescent', [
    '#CEFFFF',
    '#C6F7D6',
    '#A2F49B',
    '#BBE453',
    '#D5CE04',
    '#E7B503',
    '#F19903',
    '#F6790B',
    '#F94902',
    '#E40515',
    '#A80003',
], bad='#888888')


# *** Rainbows ***

# smooth

smooth_rainbow_colors = [
    '#E8ECFB',  # off-white [0]
    '#DDD8EF',
    '#D1C1E1',
    '#C3A8D1',
    '#B58FC2',
    '#A778B4',
    '#9B62A7',
    '#8C4E99',
    '#6F4C9B',  # purple [8]
    '#6059A9',
    '#5568B8',
    '#4E79C5',
    '#4D8AC6',
    '#4E96BC',
    '#549EB3',
    '#59A5A9',
    '#60AB9E',
    '#69B190',
    '#77B77D',
    '#8CBC68',
    '#A6BE54',
    '#BEBC48',
    '#D1B541',
    '#DDAA3C',
    '#E49C39',
    '#E78C35',
    '#E67932',
    '#E4632D',
    '#DF4828',
    '#DA2222',  # red [-5]
    '#B8221E',
    '#95211B',
    '#721E17',
    '#521A13',  # brown [-1]
]

make_and_register_smooth('tol_rainbow', smooth_rainbow_colors, bad='#666666')
make_and_register_smooth('tol_rainbow_WhBr', smooth_rainbow_colors, bad='#666666')
make_and_register_smooth('tol_rainbow_WhRd', smooth_rainbow_colors[:-4], bad='#666666')
make_and_register_smooth('tol_rainbow_PuBr', smooth_rainbow_colors[8:], bad='#FFFFFF')
make_and_register_smooth('tol_rainbow_PuRd', smooth_rainbow_colors[8:-4], bad='#FFFFFF')


# discrete

discrete_rainbow_colors = [
    '#E8ECFB',
    '#D9CCE3',
    '#D1BBD7',
    '#CAACCB',
    '#BA8DB4',
    '#AE76A3',
    '#AA6F9E',
    '#994F88',
    '#882E72',
    '#1965B0',
    '#437DBF',
    '#5289C7',
    '#6195CF',
    '#7BAFDE',
    '#4EB265',
    '#90C987',
    '#CAE0AB',
    '#F7F056',
    '#F7CB45',
    '#F6C141',
    '#F4A736',
    '#F1932D',
    '#EE8026',
    '#E8601C',
    '#E65518',
    '#DC050C',
    '#A5170E',
    '#72190E',
    '#42150A',
]

def make_discrete_rainbow_colormap(n: int):
    if n <= 0:
        raise ValueError('n must be positive')
    if n > 29:
        raise ValueError('n must be <= 29')

    indices = {
        1: [10],
        2: [10, 26],
        3: [10, 18, 26],
        4: [10, 15, 18, 26],
        5: [10, 14, 15, 18, 26],
        6: [10, 14, 15, 17, 18, 26],
        7: [9, 10, 14, 15, 17, 18, 26],
        8: [9, 10, 14, 15, 17, 18, 23, 26],
        9: [9, 10, 14, 15, 17, 18, 23, 26, 28],
        10: [9, 10, 14, 15, 17, 18, 21, 24, 26, 28],
        11: [9, 10, 12, 14, 15, 17, 18, 21, 24, 26, 28],
        12: [3, 6, 9, 10, 12, 14, 15, 17, 18, 21, 24, 26],
        13: [3, 6, 9, 10, 12, 14, 15, 16, 17, 18, 21, 24, 26],
        14: [3, 6, 9, 10, 12, 14, 15, 16, 17, 18, 20, 22, 24, 26],
        15: [3, 6, 9, 10, 12, 14, 15, 16, 17, 18, 20, 22, 24, 26, 28],
        16: [3, 5, 7, 9, 10, 12, 14, 15, 16, 17, 18, 20, 22, 24, 26, 28],
        17: [3, 5, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 20, 22, 24, 26, 28],
        18: [3, 5, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 20, 22, 24, 26, 27, 28],
        19: [2, 4, 5, 7, 8, 9, 10, 12, 14, 15, 16, 17, 18, 20, 22, 24, 26, 27, 28],
        20: [2, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 20, 22, 24, 26, 27, 28],
        21: [2, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 23, 25, 26, 27, 28],
        22: [2, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 23, 25, 26, 27, 28, 29],
        23: [1, 2, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 23, 25, 26, 27, 28, 29],
        24: [1, 2, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 26, 27, 28, 29],
        25: [1, 2, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29],
        26: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29],
        27: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29],
        28: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29],
        29: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    }

    cmap = ListedColormap(
        [discrete_rainbow_colors[i - 1] for i in indices[n]],
        name=f'tol_rainbow_{n}'
    )
    bad = '#FFFFFF' if n <= 11 else '#777777'
    cmap.set_bad(bad)
    cmap.set_under(bad)
    cmap.set_over(bad)
    return cmap

_14 = make_discrete_rainbow_colormap(14)
mpl.colormaps.register(cmap=_14)
mpl.colormaps.register(cmap=_14.reversed(), name=_14.name + '_r')

_23 = make_discrete_rainbow_colormap(23)
mpl.colormaps.register(cmap=_23)
mpl.colormaps.register(cmap=_23.reversed(), name=_23.name + '_r')

make_and_register_discrete('tol_rainbow_discrete', discrete_rainbow_colors, bad='#777777')
