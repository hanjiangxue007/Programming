#!/usr/bin/env python

# Bhishan Poudel
# Feb 4, 2016
# first open ipython notebook
# then paste this
# we can see the plot with hover enabled
# for the original code, look at the bottom

from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.graph_objs import *
init_notebook_mode()

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(
        size=[40, 60, 80, 100],
    )
)
data = [trace0]
layout = Layout(
    showlegend=False,
    height=600,
    width=600,
)

fig = dict( data=data, layout=layout )

iplot(fig)

##################################################################################
#import plotly.plotly as py
#import plotly.graph_objs as go

#trace0 = go.Scatter(
    #x=[1, 2, 3, 4],
    #y=[10, 11, 12, 13],
    #mode='markers',
    #marker=dict(
        #size=[40, 60, 80, 100],
    #)
#)
#data = [trace0]
#layout = go.Layout(
    #showlegend=False,
    #height=600,
    #width=600,
#)
#fig = go.Figure(data=data, layout=layout)

#
#
#plot_url = py.plot(fig, filename='bubblechart-size')