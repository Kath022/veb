from requests import get, post, delete

# до
print(get('http://localhost:5000/api/jobs/9').json())

# редактируем
print(post('http://localhost:5000/api/jobs/9',
           json={
               'team_leader': 1,
               'job': 'zzzzzzzzzzzz',
               'work_size': 2,
               'collaborators': '2, 1, 3, 9',
               'is_finished': True}).json())
#  смотрим результат
print(get('http://localhost:5000/api/jobs/9').json())

# пустой запрос
print(post('http://localhost:5000/api/jobs/9').json())

#  нет индекса такого
print(post('http://localhost:5000/api/jobs/9999',
           json={
               'team_leader': 1,
               'job': 'zzzzzzzzzzzz',
               'work_size': 2,
               'collaborators': '2, 1',
               'is_finished': True}).json())