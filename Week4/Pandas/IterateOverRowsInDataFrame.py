import pandas as pd

exam_data = [{'name': 'Anastasia', 'score': 12.5}, {'name': 'Dima', 'score': 9}, {'name': 'Katherine', 'score': 16.5}]
df = pd.DataFrame(exam_data)
print(df)
for index, row in df.iterrows():
    print(row['name'], row['score'])
