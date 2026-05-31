def print_table(num):
    print(f"Multiplication table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i:2} = {num * i}")

num = int(input("Enter a number: "))
print_table(num)