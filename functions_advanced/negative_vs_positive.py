

def find_sum(some_list):
    positive_sum = 0
    negative_sum = 0

    for number in some_list:
        if number > 0:
            positive_sum += number
        elif number < 0:
            negative_sum += number

    print(negative_sum)
    print(positive_sum)
    if positive_sum < abs(negative_sum):
        print("The negatives are stronger than the positives")
    elif abs(negative_sum) < abs(positive_sum):
        print("The positives are stronger than the negatives")

num_list = [int(x) for x in input().split(" ")]
find_sum(num_list)