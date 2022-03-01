estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for estudiante in list:
        first_name = estudiante['first_name']
        last_name = estudiante['last_name']
        print(f'first_name - {first_name}, last_name - {last_name}')


iterateDictionary(estudiantes)