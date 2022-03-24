from requests import post, get

'''print(get('http://localhost:8080/api/v2/users').json())
print(get('http://localhost:8080/api/v2/users/1').json())
print(delete('http://localhost:8080/api/v2/users/5').json())
print(get('http://localhost:8080/api/v2/users/145454').json())
print(get('http://localhost:8080/api/v2/users/jhfjkhfhj').json())
print(post('http://localhost:8080/api/v2/users',
    json={'surname': 'Иванов',
          'name': 'Иван',
          'age': 22,
          'position': 'comander',
          'speciality': 'biologist',
          'address': 'Скобелевская д5',
          'email': 'lohornos@lost.con',
          'hashed_password': '880bhjbkjb05553535'}).json())'''
'''print(get('http://localhost:8080/api/v2/jobs').json())
print(get('http://localhost:8080/api/v2/jobs/1').json())
print(delete('http://localhost:8080/api/v2/jobs/5').json())
print(get('http://localhost:8080/api/v2/jobs/145454').json())
print(get('http://localhost:8080/api/v2/jobs/jhfjkhfhj').json())'''
print(post('http://localhost:8080/api/jobs',
           json={'id': 3, 'job': 'Стройка', 'work_size': 10, 'collaborators': '1 2 3',
                 'is_finished': False,
                 'team_leader': 1, }).json())

print(get('http://localhost:8080/api/jobs', ).json())
