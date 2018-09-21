def convert(string):
    """ Converts passed in str to int.
    :param string: str.
    :return: string converted to int.
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55")
print(c)

# if u put peas instead of 55.0 it'llprint the error
