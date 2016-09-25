# Author : Bhishan Poudel
# Date   : July 3, 2016
# Ref    : https://plot.ly/matplotlib/getting-started/

# Imports
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.tools as tls



# --> your matplotlib methods <--
x = np.arange(0,10,0.01)
y = np.exp(x)

mpl_fig = plt.figure()
plt.plot(x,y)

plt.title(r'$\sigma_i=15$')
#fig.suptitle('top title', fontsize=20)
plt.xlabel('xlabel', fontsize=18)
plt.ylabel('ylabel', fontsize=16)

#plt.show()
#fig.savefig('test.jpg')


##======================================================================
# convert mpl fig to plotly_figure
plotly_fig = tls.mpl_to_plotly(mpl_fig)
unique_url = py.plot(plotly_fig,filename="plotly version of an mpl figure")
