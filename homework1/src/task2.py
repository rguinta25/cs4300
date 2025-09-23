def add_int(x, y):
    # Return sum of two integers
    return x + y

def mult_float(x, y):
    # Return the product of two floats 
    return x * y

def check_str(name):
    # Greetings to string provided
    return f"Hi, {name}! How are you?"

def check_bool(num):
    # Return True if number is even, if odd return False
   return num % 2 == 0

if __name__ == "__main__":
    print("Sum of integers: ", add_int(6, 7))
    print("Multiplication of floats:", mult_float(5.5, 4.5))
    print(check_str("Rayne"))
    print("Number is even: ", check_bool(4))