import pandas as pd

# Вариант 1
#melb_data_ps = pd.read_csv('project_1_Pandas/data/melb_data_ps.csv', sep=',')
#print (melb_data_ps.head())

# Вариант 2
#melb_data_ps = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/melb_data_ps.csv')
#print (melb_data_ps.head())

# Практика 1.
#citi_bike = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/citibike-tripdata.csv')
#print(citi_bike.head())

# Практика 2.
#melb_data_fe = pd.read_csv('https://raw.githubusercontent.com/Yuri-VN/SkillFactory_DATA/main/project_1_Pandas/data/melb_data_fe.csv')
#print(melb_data_fe.head())

# Практика 3. Датасет MovieLens
MovieLens = pd.read_csv('project_1_Pandas/data/movies_data/movies.csv', sep=',')
print (MovieLens.head())