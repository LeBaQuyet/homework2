n = int(input("Nhập một số nguyên dương: "))

steps = 0

while True:
    n_str = str(n)
    if n_str == n_str[::-1]:
        print(f"Số palindrome là: {n}")
        print(f"Số bước thực hiện: {steps}")
        break
    reversed_n = int(n_str[::-1])
    print(f"{n} + {reversed_n} = {n + reversed_n}")
    n = n + reversed_n
    steps += 1
