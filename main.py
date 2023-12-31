import pandas as pd

df = pd.read_csv("filename.csv", engine='python', encoding='utf-8-sig')
with open("filename.md", 'w', encoding='utf-8-sig') as md:
    df.fillna('', inplace=True)
    df.to_markdown(buf=md, index=False)
