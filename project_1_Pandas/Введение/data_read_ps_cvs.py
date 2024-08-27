import pandas as pd

# Вариант 1
melb_data_ps = pd.read_csv('project_1_Pandas/data/melb_data_ps.csv', sep=',')
print (melb_data_ps.head())

# Вариант 2
#melb_data_ps = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/melb_data_ps.csv')
#print (melb_data_ps.head())

# Практика.
#citi_bike = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/citibike-tripdata.csv')
#print(citi_bike.head())