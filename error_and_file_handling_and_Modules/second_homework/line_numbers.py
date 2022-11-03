import re

with open('text.txt','r') as input_file, open('output.txt','w') as output_file:
    for row, line in enumerate(input_file, start=1):
        letters_count = len(re.findall(r"[A-za-z]", line))
        punctuation_marks_count = len(re.findall("[,.\'\-\":?!]", line))

        output_file.write(f"Line {row}: {line.strip()} ({letters_count})({punctuation_marks_count})\n")
