
def create_sequence(n):
    seq = [0,1]
    for _ in range(n-2):
        curr_number = seq[-1] + seq[-2]
        seq.append(curr_number)

    return seq


data = input()
sequence = []

while not data == "Stop":
    split_data = data.split()

    if split_data[0] == "Create":
        number = int(split_data[-1])
        sequence = create_sequence(number)
        print(*sequence, sep =" ")

    elif split_data[0] == "Locate":
        number = int(split_data[-1])

        if number in sequence:
            print(f"The number {number} is at index {sequence.index(number)}")
        else:
            print(f"The number {number} is not in the sequence!")
    data = input()