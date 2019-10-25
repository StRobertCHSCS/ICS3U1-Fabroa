def foo(arg1: int, arg2:float) -> float:
    """A summary of the function, keep it to online
 
    Arguments:
        arg1 {int} -- description of the first parameter
        arg2 {float} -- description of the second parameter
    
    Returns:
        float -- description of the return value
    """

    return 5.0

def get_total_price(price, tax_rate):
    total_price = (price * tax_rate) + price
    return total_price

print(get_total_price(5.99, 0.13))
    



