


import os

absolute_path = os.path.dirname(os.path.abspath(__file__))


file_path = os.path.join(absolute_path,"custom_files","test.txt")
print(file_path)
file = open(file_path,"a")
print(file.writelines("\ndupe"))

example_dict = {"a":1,"b":2}
print(file.writelines(example_dict))

file.close()