import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)

df = pd.read_csv('medical_examination.csv')

df['overweight'] = (df['weight'] / ((df["height"] / 100) ** 2)).apply(lambda x : 1 if x > 25 else 0)

df['cholesterol'] = df['cholesterol'].apply(lambda x : 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x : 0 if x == 1 else 1)


def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index = False).count()

    fig = sns.catplot(x='variable',y='total',data=df_cat,hue='value',kind='bar',col='cardio').figure
    fig.savefig('catplot.png')
    return fig


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def draw_heat_map():

    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975)) 
    ]

    corr = df_heat.corr(method='pearson')
    mask = np.triu(corr)
    fig, ax = plt.subplots(figsize=(12, 12))

    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=1, square=True, cbar_kws={'shrink': 0.5}, center=0.08, ax=ax)
    fig.savefig('heatmap.png')

    return fig

