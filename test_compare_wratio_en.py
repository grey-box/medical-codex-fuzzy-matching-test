import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

from essential_english import essential_english
from pathlib import Path

testdata = pd.read_csv("testdata.csv")

x = testdata.shape[0]
y = len(essential_english)

results = []
for i in range(0, x):
    k = []
    for j in range(0, y):
        k.append(fuzz.WRatio(testdata.iloc[i, 1], essential_english[j]))

    top_3_idx = np.argsort(k)[-3:]
    top_3_values = [essential_english[z] for z in top_3_idx]
    results.append([testdata.iloc[i, 1], testdata.iloc[i, 2], top_3_values[2], top_3_values[1], top_3_values[0]])
print(results)

df = pd.DataFrame(results)
print(df)

filepath = Path('englishWRatio.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
