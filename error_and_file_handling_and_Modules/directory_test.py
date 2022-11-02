from os import listdir, path


def traverse_dir(curr_path,files_by_ext):
    for element in listdir(curr_path):
        if path.isdir(path.join(curr_path, element)):
            traverse_dir(path.join(curr_path, element),files_by_ext)
        else:
            # print('file', element)
            extension = element.split(".")[-1]
            if extension not in files_by_extension:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


files_by_extension= {}

traverse_dir('.',files_by_extension)
for key,value in files_by_extension.items():
    print(f".{key}")
    for file in value:
        print(f"- - - {file}")
