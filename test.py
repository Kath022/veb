from requests import get, post, delete

# получаем по id
print(get('http://localhost:5000/api/v2/users/1').json())
# получаем все
print(get('http://localhost:5000/api/v2/users').json())

# несуществующий индекс
print(get('http://localhost:5000/api/v2/users/14').json())

# добаляем
print(post('http://localhost:5000/api/v2/users',
           json={
            'id': '14',
            'name': 'my',
            'surname': 'my2',
            'age': 12,
            'position': 'wow',
            'speciality': 'WoW',
            'address': 'vb@mail.ru'
           }).json())
# смотрим результат
print(get('http://localhost:5000/api/v2/users/14').json())

# удаляем 14
print(delete('http://localhost:5000/api/v2/users/14').json())

# удаляем уже не существующий индекс
print(delete('http://localhost:5000/api/v2/users/14').json())






# # редактируем
# print(post('http://localhost:5000/api/jobs/9',
#            json={
#                'team_leader': 1,
#                'job': 'zzzzzzzzzzzz',
#                'work_size': 2,
#                'collaborators': '2, 1, 3, 9',
#                'is_finished': True}).json())
# #  смотрим результат
# print(get('http://localhost:5000/api/jobs/9').json())
#
# # пустой запрос
# print(post('http://localhost:5000/api/jobs/9').json())
#
# #  нет индекса такого
# print(post('http://localhost:5000/api/jobs/9999',
#            json={
#                'team_leader': 1,
#                'job': 'zzzzzzzzzzzz',
#                'work_size': 2,
#                'collaborators': '2, 1',
#                'is_finished': True}).json())