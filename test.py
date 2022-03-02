from requests import get, post, delete


print(get('http://localhost:5000/api/jobs').json())

# индекса нет
print(delete('http://localhost:5000/api/jobs/9').json())
# удалил верно
print(get('http://localhost:5000/api/jobs').json())

print(delete('http://localhost:5000/api/jobs/9').json())