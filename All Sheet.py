import pandas as pd

a = r'C:\\Users\\sony\\Desktop\\Excel Sheet\\Example.xlsx'

df = pd.read_excel(a, 0)
c = pd.ExcelFile(a)
list = []
for sheet in c.sheet_names:

    list.append(c.parse(sheet))

    d = pd.concat((list))


    d.to_csv('C:\\Users\\sony\\Desktop\\Excel Sheet\\AllSheet.csv', encoding='utf-8', index=True, header=True)
    print(d)
