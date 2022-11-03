
import os

file = open("custom_files/inner.txt")
file1 = open("example.txt")
print(file.name)

print(file.readlines())  # <--- puts each line as an element in a list
print(file1.readlines())  # <--- puts each line as an element in a list

# absolute_path = os.path.abspath(__file__)
absolute_path = os.path.dirname(os.path.abspath(__file__))


# print(os.path.abspath(__file__))

# print(absolute_path + "/custom_files/" + "inner.txt")
file_path = os.path.join(absolute_path,"custom_files","inner.txt")
print(file_path)
file = open(file_path)
print(file.readlines())

file.close()



