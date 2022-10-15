age = int(input())
alcohol = ""

if age < 14:
    alcohol = "toddy"
elif age <18:
    alcohol = "coke"
elif age < 21:
    alcohol = "beer"
else:
    alcohol = "whisky"

print(f"drink {alcohol}")