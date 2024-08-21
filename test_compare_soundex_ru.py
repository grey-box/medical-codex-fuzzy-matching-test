import pandas as pd
import numpy as np
from fonetika.soundex import RussianSoundex
from fonetika.distance import PhoneticsInnerLanguageDistance

from compendium_ru import compendium_RU
from pathlib import Path
testdata = pd.read_csv("testdatarussian.csv")

x = testdata.shape[0]
y = len(compendium_RU)

results = []
for i in range(0, x):
    k = []
    for j in range(0, y):
        k.append(PhoneticsInnerLanguageDistance(RussianSoundex()).distance(testdata.iloc[i, 1], compendium_RU[j]))

    bot_3_idx = np.argsort(k)[:3]
    bot_3_values = [compendium_RU[z] for z in bot_3_idx]
    results.append([testdata.iloc[i, 1], testdata.iloc[i, 2], bot_3_values[0], bot_3_values[1], bot_3_values[2]])
print(results)

df = pd.DataFrame(results)
print(df)

filepath = Path('russiansoundex.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
