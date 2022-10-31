

def kwargs_length(**kwargs):
    total_length = 0
    for kvpt in kwargs:
        total_length += 1
    return total_length

dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))


dictionary = {}

print(kwargs_length(**dictionary))
