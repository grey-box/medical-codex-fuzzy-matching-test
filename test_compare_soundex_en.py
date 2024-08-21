import pandas as pd
import numpy as np
from fonetika.soundex import EnglishSoundex
from fonetika.distance import PhoneticsInnerLanguageDistance

from essential_english import essential_english
from pathlib import Path

testdata = pd.read_csv("testdata.csv")

x = testdata.shape[0]
y = len(essential_english)

results = []
for i in range(0, x):
    k = []
    for j in range(0, y):
        k.append(PhoneticsInnerLanguageDistance(EnglishSoundex()).distance(testdata.iloc[i, 1], essential_english[j]))

    bot_3_idx = np.argsort(k)[:3]
    bot_3_values = [essential_english[z] for z in bot_3_idx]
    results.append([testdata.iloc[i, 1], testdata.iloc[i, 2], bot_3_values[0], bot_3_values[1], bot_3_values[2]])
print(results)

df = pd.DataFrame(results)
print(df)


filepath = Path('englishsoundex.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
