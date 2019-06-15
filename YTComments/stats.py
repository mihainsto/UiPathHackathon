#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

TONES = [
    'Joy',
    'Confident',
    'Tentative',
    'Analytical',
    'Sad',
    'Fearful',
    'Angry',
]

GOOD_TONES = TONES[:3]
BAD_TONES = TONES[4:]

def reindex_tones(df):
    print(df.index)
    return df

if __name__ == '__main__':
    INPUT_CSV = 'SentimenteOutput.csv'

    df = pd.read_csv(INPUT_CSV)

    grouped = df.groupby(['Tone'], sort=False)

    summed = grouped.sum()
    counted = grouped.count()

    counted.plot.pie(y='Confidence')
    plt.title("YouTube Comment Sentiments")
    plt.show()
