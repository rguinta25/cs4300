import math
def check_num(num):
    result = ""
    if num > 0:
        result = "positive"
    elif num < 0:
        result = "negative"
    elif num == 0:
        result = "zero"
    else:
        result == "not a number"
    return result

def print_prime_nums():
    prime = []
    num = 2 
    while len(prime) < 10:
        for i in range(2, int(num ** 0.5) +1):
            if num % i == 0:
                break
        else: 
            prime.append(num)
        num += 1
    return prime

def get_sum():
    num = 0
    result = 0
    while num <= 100:
        result += num
        num += 1
    return result

if __name__ == "__main__":
    print("The number is ", check_num(3))
    print("The number is ", check_num(-3))
    print("The number is ", check_num(0))
    print(print_prime_nums())
    print(get_sum())