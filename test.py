from requests import get, post

# пустой запрос
print(post('http://localhost:5000/api/jobs').json())
# некоректный запрос
print(post('http://localhost:5000/api/jobs', json={
               'id': '8',
               'team_leader': '1',
               'job': 'rere',
               'work_size': 2,}).json())

# уже есть индекст
print(post('http://localhost:5000/api/jobs',
           json={
               'id': '1',
               'team_leader': '1',
               'job': 'rere',
               'work_size': 2,
               'collaborators': '2, 1',
               'is_finished': True}).json())

# корректно
print(post('http://localhost:5000/api/jobs',
           json={
               'id': '13',
               'team_leader': '1',
               'job': 'rere',
               'work_size': 2,
               'collaborators': '2, 1',
               'is_finished': True}).json())