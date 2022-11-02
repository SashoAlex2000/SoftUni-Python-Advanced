

with open("text.txt") as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            # print(row, line.strip())
            current_line_list = line.strip().split(" ")
            for pos in range(len(current_line_list)):
                word = list(current_line_list[pos])
                for char in range(len(word)):
                    if word[char] in ("-", ",", ".", "!", "?"):
                        word[char] = "@"
                word = "".join(word)
                current_line_list[pos] = word

            print(" ".join(current_line_list[::-1]))

#END
