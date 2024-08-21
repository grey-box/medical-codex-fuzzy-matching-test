import pandas as pd
import random
import string

from essential_english import essential_english


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
                        typo = t[:b - 1] + random.choice(string.ascii_letters) + t[b:]
                    if error == 1:
                        typo = t[:b - 1] + t[b:]
                    if error == 0:
                        typo = t[:b] + random.choice(string.ascii_letters) + t[b:]
                    t = typo
                    a = len(typo)
                    j += 1
                    typolist.append([typo, target])
                k += 1
    return (typolist)


testdata = typo_generator(essential_english)
df = pd.DataFrame(testdata)
print(df)
from pathlib import Path

filepath = Path('testdata.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
