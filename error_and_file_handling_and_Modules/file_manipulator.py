import os


while True:
    line = input()
    if line == "End":
        break


    line_list = line.split("-")
    command = line_list[0]
    file_name = line_list[1]

    if command == "Create":
        open(file_name, "w").close()

    elif command == "Add":
        content = line_list[2]
        with open(file_name,"a") as file:
            file.write(content + "\n")

    elif command == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print(f"An error occurred")

    elif command == "Replace":
        old_string = line_list[2]
        new_string = line_list[3]

        try:
            with open(file_name,"r+") as file:
                new_file_content = file.read().replace(old_string,new_string)
                file.seek(0)
                file.truncate()
                file.write(new_file_content)

        except FileNotFoundError:
            print(f"An error occurred")
