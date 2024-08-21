import pandas as pd
import random

from Ru_alphabet import Ru_alphabet
from compendium_ru import compendium_RU


def typo_generator(medlist):
    typolist = []
    c = ["add", "drop", "swap"]
    for i in range(0, len(medlist)):
        if medlist[i] != "":
            k = 0
            while k <= 2:
                target = medlist[i]
                a = len(target)
                error = random.randint(0, 2)
                numbererrors = random.randint(1, 3)
                t = target
                for j in range(1, numbererrors):
                    b = random.randint(0, a - 1)
                    if error == 2:
                        typo = t[:b - 1] + random.choice(Ru_alphabet) + t[b:]
                    if error == 1:
                        typo = t[:b - 1] + t[b:]
                    if error == 0:
                        typo = t[:b] + random.choice(Ru_alphabet) + t[b:]
                    t = typo
                    a = len(typo)
                    j += 1
                    typolist.append([typo, target])
                k += 1
    return (typolist)


russian_test = random.sample(compendium_RU, 400)
testdata = typo_generator(russian_test)
df = pd.DataFrame(testdata)
print(df)
from pathlib import Path

filepath = Path('testdatarussian.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
