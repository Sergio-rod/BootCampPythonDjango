#
#
# """with open('weather_data.csv', 'r') as data:
#     arr = data.readlines()"""
# """import csv
#
# with open('weather_data.csv', 'r') as data:
#     data = csv.reader(data)
#     temperature = []
#     for i in data:
#         if data.line_num == 1:
#             continue
#         temperature.append(int(i[1]))
#
#     print(temperature)
#
# """
#
# import pandas as pd
#
# data = pd.read_csv('weather_data.csv')
# """
# data_dict = data.to_dict()
#
# temp_list = data['temp'].to_list()
#
# print(data['temp'].max())
#
# print(data.temp)
# """
#
# #select a row, where the temperature is the maximum
# #print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
#
# print(monday.temp * 9/5 + 32)
#
#
#
#
# #create a datagrame
#
# data_dict = {
#     'Students' : [
#         'Amy', 'Edith', 'Sergio'
#     ],
#     'Notes' : [
#         1,2,3
# ]
# }
#
# students = pd.DataFrame(data_dict)
#
# print(students)

import pandas as pd



data = pd.read_csv('Squirrel_data.csv')

gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])

dict = {

    'Fur color' : [
        'grey', 'red', 'black'
    ],
    'Count' : [
        gray_squirrels,red_squirrels,black_squirrels
    ]

}

dict2 = {'Gray': gray_squirrels, 'Red': red_squirrels, 'Black':black_squirrels}

df_squirrels_colors = pd.DataFrame(dict)

df_squirrels_colors.to_csv('Squirrels_colors')
