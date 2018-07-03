import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import pandas as pd
import numpy as np

def plot_timeseries_df(df, linewidth=5):
    '''Function created a time series visualisation for 
    a number of countries given as input in a dataframe'''

    if 'cluster' in df.columns:
        df = df.drop('cluster', axis=1)

    df = df.T
    df.index = pd.to_datetime(df.index.values, format='%Y')
    ax = df.plot(figsize=(16, 8), linewidth=linewidth, fontsize=20)
    ax.set_xlabel("Year", fontsize=20)
    ax.set_ylabel("Under 5 child mortality", fontsize=20)
    ax.legend(bbox_to_anchor=(1.1, 1.05))


def timeseries_for_clusters_mean(cluster_df):
    conc_df = []
    for name, group in cluster_df.groupby('cluster'):
        conc_df.append(pd.DataFrame(group.apply(np.mean, axis=0).T.rename("Cluser " + str(name))))

    final_df = pd.concat(conc_df, axis=1)
    final_df = final_df.drop(['cluster'])

    final_df.index = pd.to_datetime(final_df.index.values, format='%Y')
    ax = final_df.plot(figsize=(16, 8), linewidth=5, fontsize=20)
    ax.set_xlabel("Year", fontsize=20)
    ax.set_ylabel("Under 5 child mortality", fontsize=20)
    ax.legend(bbox_to_anchor=(1.1, 1.05))