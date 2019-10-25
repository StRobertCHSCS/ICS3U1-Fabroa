def squirrel_play(temp: float, is_Summmer: bool) -> bool:
    """Determine if squirrels should play outside
    
    Arguments:
        temp {float} -- outside temperature
        is_Summmer {bool} -- whether it is summer
    
    Returns:
        bool -- do the squirrels play
    """

    if is_Summmer:
        upper_limit = 100
    else:
        upper_limit = 90

    if 60 <= temp <= upper_limit:
        return True 
    else:
        return False


# verify functionality
assert squirrel_play(70, False)
assert not squirrel_play(95, False)
assert squirrel_play(95, True)
