#!/usr/bin/env python

# Bhishan Poudel
# Feb 4, 2016

import plotly.plotly as py
import cufflinks as cf
import pandas as pd

cf.set_config_file(offline=False, world_readable=True, theme='ggplot')

df = pd.read_csv('http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt', sep='\t')
df2007 = df[df.year==2007]
df1952 = df[df.year==1952]
df.head(2)

df2007.iplot(kind='scatter', mode='markers', x='gdpPercap', y='lifeExp', filename='cufflinks/simple-scatter')

