from plotly.offline import enable_mpl_offline, plot_mpl

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import plotly.plotly as py

py.sign_in(username="bhishanpdl", api_key="amq1tpxuig")

n = 50
x, y, z, s, ew = np.random.rand(5, n)
c, ec = np.random.rand(2, n, 4)
area_scale, width_scale = 500, 5

fig, ax = plt.subplots()
sc = ax.scatter(x, y, c=c,
            s=np.square(s)*area_scale,
            edgecolor=ec,
            linewidth=ew*width_scale)
ax.grid()

plot_url = plot_mpl(fig)
