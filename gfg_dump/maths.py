def is_palin(n):
    rev = 0
    temp = n

    while temp != 0:
        ld = temp % 10
        rev = rev*10+ld
        temp = temp//10

    return rev == n

if __name__ == '__main__':
    num = int(input("Enter the number:"))
    print(is_palin(num))