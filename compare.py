import pandas as pd

old = pd.read_excel('employees_old.xlsx')
new = pd.read_excel('employees_new.xlsx')

print(old.head())