def calculate_discount(original_price, discount_percent):
    """
    Calculate the discounted price.
    
    Args:
        original_price (float): The original price
        discount_percent (float): The discount percentage (0-100)
    
    Returns:
        dict: Contains original_price, discount_amount, and final_price
    """
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    
    return {
        "original_price": original_price,
        "discount_percent": discount_percent,
        "discount_amount": round(discount_amount, 2),
        "final_price": round(final_price, 2)
    }


if __name__ == "__main__":
    price = 100
    discount = 20
    result = calculate_discount(price, discount)
    
    print(f"Original Price: ${result['original_price']}")
    print(f"Discount: {result['discount_percent']}%")
    print(f"Discount Amount: ${result['discount_amount']}")
    print(f"Final Price: ${result['final_price']}")