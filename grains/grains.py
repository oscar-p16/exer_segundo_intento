def square(number):
    
    if number not in range(1, 65):
        raise ValueError("Squares on chessboard must be integers between 1 and 64.")
    return 2 ** (number - 1)
def total():
    return 2**64 - 1
