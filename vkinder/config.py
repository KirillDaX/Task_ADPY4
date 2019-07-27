
# часть данных VK
target_id = int(input('введите ID: '))
age_range = 1
count_find = 50

APP_ID = 6984843
# BASE_URL = 'https://oauth.vk.com/authorize'
# https://oauth.vk.com/authorize?client_id=6984843&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&v=5.101&scope=wall+friends+pages+groups
TOKEN = input('для ТОКЕНА: https://oauth.vk.com/authorize?client_id=6984843&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&v=5.101&scope=wall+friends+pages+groups \n Введите токен: ')

simbol_pattern = r'[!@#$%^&*()№±_=\\\|\'\"\-\+\}\{\[\]\<\>\?\/]'

# points system
friends_points = 2
group_points = 1
interests_point = 2
music_points = 1
movies_points = 1
