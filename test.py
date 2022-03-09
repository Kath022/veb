from requests import get, post, delete

# получаем по id
print(get('http://localhost:5000/api/v2/jobs/1').json())
# получаем все
print(get('http://localhost:5000/api/v2/jobs').json())

# несуществующий индекс
print(get('http://localhost:5000/api/v2/jobs/14').json())


# добаляем
print(post('http://localhost:5000/api/v2/jobs',
           json={
            'id': '14',
            'team_leader': 2,
            'job': 'doing',
            'work_size': 12,
            'collaborators': '1, 2, 3',
            'is_finished': False,
           }).json())
# смотрим результат
print(get('http://localhost:5000/api/v2/jobs/14').json())

# удаляем 14
print(delete('http://localhost:5000/api/v2/jobs/14').json())

# удаляем уже не существующий индекс
print(delete('http://localhost:5000/api/v2/jobs/14').json())






# # ТЕСТИРОВАНИЕ КЛАССОВ РЕСУРСА USERS
#
# # получаем по id
# print(get('http://localhost:5000/api/v2/users/1').json())
# # получаем все
# print(get('http://localhost:5000/api/v2/users').json())
#
# # несуществующий индекс
# print(get('http://localhost:5000/api/v2/users/14').json())
#
# # добаляем
# print(post('http://localhost:5000/api/v2/users',
#            json={
#             'id': '14',
#             'name': 'my',
#             'surname': 'my2',
#             'age': 12,
#             'position': 'wow',
#             'speciality': 'WoW',
#             'address': 'vb@mail.ru'
#            }).json())
# # смотрим результат
# print(get('http://localhost:5000/api/v2/users/14').json())
#
# # удаляем 14
# print(delete('http://localhost:5000/api/v2/users/14').json())
#
# # удаляем уже не существующий индекс
# print(delete('http://localhost:5000/api/v2/users/14').json())



# # ТЕСТИРОВАНИЕ РЕДАКТИРОВАНИЯ
# # получаем по id
# print(get('http://localhost:5000/api/v2/users/1').json())
# # получаем все
# print(get('http://localhost:5000/api/v2/users').json())
#
# # несуществующий индекс
# print(get('http://localhost:5000/api/v2/users/14').json())
#
# # добаляем
# print(post('http://localhost:5000/api/v2/users',
#            json={
#             'id': '14',
#             'name': 'my',
#             'surname': 'my2',
#             'age': 12,
#             'position': 'wow',
#             'speciality': 'WoW',
#             'address': 'vb@mail.ru'
#            }).json())
# # смотрим результат
# print(get('http://localhost:5000/api/v2/users/14').json())
#
# # удаляем 14
# print(delete('http://localhost:5000/api/v2/users/14').json())
#
# # удаляем уже не существующий индекс
# print(delete('http://localhost:5000/api/v2/users/14').json())
#
#
# # ТЕСТИРОВАНИЕ УДАЛЕНИЯ
# # получаем по id
# print(get('http://localhost:5000/api/v2/users/1').json())
# # получаем все
# print(get('http://localhost:5000/api/v2/users').json())
#
# # несуществующий индекс
# print(get('http://localhost:5000/api/v2/users/14').json())
#
# # добаляем
# print(post('http://localhost:5000/api/v2/users',
#            json={
#             'id': '14',
#             'name': 'my',
#             'surname': 'my2',
#             'age': 12,
#             'position': 'wow',
#             'speciality': 'WoW',
#             'address': 'vb@mail.ru'
#            }).json())
# # смотрим результат
# print(get('http://localhost:5000/api/v2/users/14').json())
#
# # удаляем 14
# print(delete('http://localhost:5000/api/v2/users/14').json())
#
# # удаляем уже не существующий индекс
# print(delete('http://localhost:5000/api/v2/users/14').json())
#
#
#
# # ТЕСТИРОВАНИЕ РЕДАКТИРОВАНИЯ
# # получаем по id
# print(get('http://localhost:5000/api/v2/users/1').json())
# # получаем все
# print(get('http://localhost:5000/api/v2/users').json())
#
# # несуществующий индекс
# print(get('http://localhost:5000/api/v2/users/14').json())
#
# # добаляем
# print(post('http://localhost:5000/api/v2/users',
#            json={
#             'id': '14',
#             'name': 'my',
#             'surname': 'my2',
#             'age': 12,
#             'position': 'wow',
#             'speciality': 'WoW',
#             'address': 'vb@mail.ru'
#            }).json())
# # смотрим результат
# print(get('http://localhost:5000/api/v2/users/14').json())
#
# # удаляем 14
# print(delete('http://localhost:5000/api/v2/users/14').json())
#
# # удаляем уже не существующий индекс
# print(delete('http://localhost:5000/api/v2/users/14').json())




