def calclulate_discount(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError("No valid discount provided")
    return price - (price * (discount * 0.01))
    

if __name__ == "__main__":
    print(f" Your discounted price is: ${calclulate_discount(100, 20):.2F}")
    print(f" Your discounted price is: ${calclulate_discount(59.99, 25):.2F}")