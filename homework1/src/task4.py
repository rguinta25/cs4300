def calclulate_discount(price, discount):
    """
    Calculate the discounted price

    Parameters:
        price: Original price
        discount: Percentage 0-100

    Returns:
        Price after discount
    
    Raises:
        ValueError if discount is out of bounds
    """
    if discount < 0 or discount > 100:
        raise ValueError("No valid discount provided")
    return price - (price * (discount * 0.01))
    

if __name__ == "__main__":
    print(f" Your discounted price is: ${calclulate_discount(100, 20):.2F}")
    print(f" Your discounted price is: ${calclulate_discount(59.99, 25):.2F}")