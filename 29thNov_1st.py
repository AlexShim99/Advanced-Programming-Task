#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys

# use list comprehension to create a list of rolls of a six-sided die
rolls = [random.randrange(1,4) for i in range(int(sys.argv[1]))]

#NumPy unique function returns unique faces and frequency of each face
values, frequencies = np.unique(rolls, return_counts=True)

title = f'Rolling a Six-Sided Dice {len(rolls):,} Times'
sns.set_style('whitegrid') #white background with gray grid lines
axes = sns.barplot(values, frequencies, palette='bright') #create bars
axes.set_title(title) #set graph title
axes.set(xlabel='Dice Value', ylable='Frequency') #label the axes

#scale y-axis by 10% to make room for text above bars
axes.set_ylin(top=max(frequencies * 1.10))

#display frequency & percentage above each patch (bar)
for bar, frequency in zip(axes.patches, frequencies):
	text_x = bar.get_x() + bar.get_width() / 2.0
	text_y = bar.get_height()
	text = f'{freqneucy:,}\n{frequency / len(rolls):.3%}'
	axes.text(text_x, text_y, text_y, fontsize=11, ha='center', va='bottom')

plt.show() #display graph
