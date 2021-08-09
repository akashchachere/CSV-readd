import pandas as pd

a = r'*.xlsx'

df = pd.read_excel(a, 0)
c = pd.ExcelFile(a)
list = []
for sheet in c.sheet_names:

    list.append(c.parse(sheet))

    d = pd.concat((list))


    d.to_csv('*.csv', encoding='utf-8', index=True, header=True)
    print(d)
