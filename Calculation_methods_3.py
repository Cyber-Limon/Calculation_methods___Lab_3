from decimal import  Decimal

print("n\t\t\tz_n - z_точн\t\t\t\t\tz_n - z_1\t\t\t\t\t\tz_1 - z_точн\t\t\t\t\td_n\t\t\t\t\t\t\t\t\t\tz_2 - z_точн\t\t\t\t\td_1")
print("-" * 220)



z_precise = Decimal("10.5844484649508098")

a = Decimal("1.1")
Q = 2

z_n_old = 1 / (1 ** a)
z_1_old = Decimal("0")



n = 2
while n < 132000:
    z_n = z_1 = z_2 = Decimal("0")

    i = 1
    while i <= n:
        z_n += 1 / (i ** a)
        i += 1

    z_1 = z_n + ((z_n - z_n_old) / (Q ** (a - 1) - 1))

    if z_1_old != 0:
        z_2 = z_1 + ((z_1 - z_1_old) / (Q ** a - 1))

    z_n_old = z_n
    z_1_old = z_1



    z_n_precise = z_n - z_precise
    z_n_1 = z_n - z_1
    z_1_precise = z_1 - z_precise
    z_2_precise = z_2 - z_precise



    if n <= 100:
        print(n, "\t\t\t", end='')
    else:
        print(n, "\t\t", end='')

    print(z_n_precise, "\t", end='')
    print(z_n_1, "\t", end='')
    print(z_1_precise, "\t", end='')

    if n <= 5:
        print(z_1_precise / z_n_precise, "\t\t\t", end='')
    elif n <= 100000:
        print(z_1_precise / z_n_precise, "\t\t", end='')
    else:
        print(z_1_precise / z_n_precise, "\t", end='')

    if n <= 2:
        print("-", "\t\t\t\t\t\t\t\t", end='')
    elif n <= 1024:
        print(z_2_precise, "\t", end='')
    else:
        print(z_2_precise, "\t\t", end='')

    if n != 2:
        print(z_2_precise / z_1_precise)
    else:
        print("-")



    n *= 2
