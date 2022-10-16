days = int(input())
total_price = 0
for i in range(1, days+ 1):
    price = float(input())
    days = int(input())
    capsules = int(input())
    current_price = price * days * capsules
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")

print(f"Total: ${total_price:.2f}")