import pandas as pd

scores = pd.Series([90, 80, 70, 60, 50])

subjects = pd.Series(["국어", "영어", "수학", "과학", "사회"])

scoreSeries = pd.Series(data=scores.values, index=subjects.values)
print(scoreSeries)
print()
print(scoreSeries["과학"])
print()
print(scoreSeries.index)
print()
print(scoreSeries.values)
