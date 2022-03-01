dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictionary):
    keys = dictionary.keys()
    for key in keys:
        print(str(len(dictionary.get(key))),key.upper())
        for value in dictionary.get(key):
            print(value)

printInfo(dojo)