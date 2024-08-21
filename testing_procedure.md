---
Author: Dominique Dupont-Jillings
---

# Fuzzy matching algorithm testing procedure & results

Algorithms tested:
* Soundex
* WRatio (Levenshtein variation)

## Idea

* Create a list of typos and corresponding medications. 
* Test the fuzzy matching algorithms on the typos, and check if one of the top 3 matches is the correct corresponding medication.

## Typo generator

The typo generator has an English and Russian version. These versions can be edited to include other languages. Every word entered into the algorithm has 1-3 typos added. These typos can be an extra letter, a swapped letter or a missing letter and occur at random locations.

* English typo generator: [typo_generator.py](typo_generator.py)
* Russian typo generator: [typo_generator_Ru.py](typo_generator_Ru.py)
* English typo list: [testdata.csv](testdata.csv)
* Russian typo list: [testdatarussian.csv](testdatarussian.csv)

## Comparing fuzzy algorithms

Simple algorithms are used to go through the list of typos. 

For each language and algorithm, the program finds the top three matches for every typo. 

This algorithms then produce a csv file where the first column is the type, the second column is the correct medication, the third column is the top match, the fourth column is the second match, and the fifth column is the third match.

* English test: [test_compare.py](test_compare_soundex_en.py)
* Russian test: [test_compare_Ru.py](test_compare_soundex_ru.py)
* English Soundex results: [englishsoundex.csv](englishsoundex.csv)
* English WRatio results: [englishWRatio.csv](englishWRatio.csv)
* Russian Soundex results: [russiansoundex.csv](russiansoundex.csv)
* Russian WRatio results: [russianWRatio.csv](russianWRatio.csv)

These csv files were then combined into an excel document and basic data analysis was done giving the following results.

* Combined excel file: Results.xlsx

### English Soundex

1478 typos tested

| Statistics            | Number | Percentage |
|-----------------------|--------|------------|
| Top result correct    | 1274   | 86.1976%   |
| Second result correct | 60     | 4.0595%    |
| Third result correct  | 26     | 1.7591%    |
| Total correct         | 1360   | 92.0785%   |

### Russian Soundex

1202 typos tested

| Statistics            | Number | Percentage |
|-----------------------|--------|------------|
| Top result correct    | 981    | 81.614%    |
| Second result correct | 69     | 5.7404%    |
| Third result correct  | 23     | 1.9135%    |
| Total correct         | 1073   | 89.2679%   |

### English WRatio

1478 typos tested

| Statistics            | Number | Percentage |
|-----------------------|--------|------------|
| Top result correct    | 1464   | 99.0528%   |
| Second result correct | 7      | 0.4736%    |
| Third result correct  | 2      | 0.1353%    |
| Total correct         | 1473   | 99.6617%   |

### Russian WRatio

1201 typos tested

| Statistics            | Number | Percentage |
|-----------------------|--------|------------|
| Top result correct    | 1193   | 99.2512%   |
| Second result correct | 6      | 0.4992%    |
| Third result correct  | 1      | 0.0832%    |
| Total correct         | 1200   | 99.8336%   |

### Conclusion

From these results we can conclude that WRatio is the best algorithm
based on our testing procedure.

It is worth noting that the testing procedure does favor Levenshtein
based algorithms due to how the typos are generated. If a future group
finds a way to generate typos by sound, it would be worth repeating this
testing procedure.

All files can be found in the Google Drive, in a folder titled "Fuzzy
algorithm tests".
