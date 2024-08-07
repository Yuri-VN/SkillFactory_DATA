import pandas as pd

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'area': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

countries_df.to_csv('project_1_Pandas/data/countries.csv', index=False, sep=';')

# По ссылке
# data = pd.read_csv('https://github.com/Yuri-VN/SkillFactory_DATA/blob/main/project_1_Pandas/data/countries.csv')
data = pd.read_csv('https://raw.githubusercontent.com/esabunor/MLWorkspace/master/melb_data.csv')
print (data)