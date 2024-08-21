import pandas as pd
import numpy as np

from compendium_ru import compendium_RU
from pathlib import Path
from fuzzywuzzy import fuzz

testdata = pd.read_csv("testdatarussian.csv")

x = testdata.shape[0]
y = len(compendium_RU)

results = []
for i in range(0, x):
    k = []
    for j in range(0, y):
        k.append(fuzz.WRatio(testdata.iloc[i, 1], compendium_RU[j]))

    top_3_idx = np.argsort(k)[-3:]
    top_3_values = [compendium_RU[z] for z in top_3_idx]
    results.append([testdata.iloc[i, 1], testdata.iloc[i, 2], top_3_values[2], top_3_values[1], top_3_values[0]])
print(results)

df = pd.DataFrame(results)
print(df)

filepath = Path('russianWRatio.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
