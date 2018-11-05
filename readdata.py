# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:22:39 2018

@author: Eric
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv('data/train_sample.csv')
train.attributed_time = pd.to_datetime(train.attributed_time)
train.click_time = pd.to_datetime(train.click_time)

trainFraud = train.loc[train.is_attributed > 0.8]
trainNormal = train.loc[train.is_attributed < 0.8]

counts = train.ip.value_counts()
sorted_counts = np.sort(counts.values)
np.histogram(sorted_counts, bins=50)
fig = plt.figure(figsize=(15, 6))
plt.yscale('log', nonposy='clip')
counts.hist(bins=50)

