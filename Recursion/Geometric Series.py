x =  float(input("Enter the value of x: "))
n =  int(input("Enter the value power limit (n): "))

if x == 0: 
    print("Error: x can't be 0 because division by zero is undefined.")
else:
    total_sum = 0.0
    total_sum_int = 0

    for i in range(n + 1):
        total_sum += 1/(x**i)
        total_sum_int += 1/(x**i)
        print(f"1/{x} ^ {i} | added -> Current Sum | {total_sum}")

        total_sum_int = int(total_sum)

print(f"\nTotal Sum = {total_sum}")
print(f"Total Sum in Int = {total_sum_int}\n")