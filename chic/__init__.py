from .schemes import (
    schemes,
    set_default,
    make_colormap_from_scheme
)
from .defaults import params

import matplotlib as mpl

mpl.rcParams.update(params)
set_default('tol_bright')
