import pandas as pd

# тренировка
#countries_data = pd.read_csv('project_1_Pandas/data/countries.csv', sep=';')
#print (countries_data)

# По ссылке
#data = pd.read_csv('https://raw.githubusercontent.com/esabunor/MLWorkspace/master/melb_data.csv')
melb_data = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/melb_data.csv')
print (melb_data)

a = melb_data.iloc[3521, 14] / melb_data.iloc[1690, 14]
print(round(a))