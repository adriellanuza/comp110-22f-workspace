"""List functions :o"""
__author__: str = "730511180"

def all(a: list[int], b: int) -> bool:
    """Checks if list matches int"""
    indices: int = 0
    while indices < len(a):
        if a[indices] != b:
            return False
        indices += 1
    return True
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    indices: int = 0
    most: int = input[indices]
    while indices < len(input):   
        if input[indices] > most:
            most = input[indices]
        indices +=1
    return most    
def is_equal(a: list[int], b: list[int]) -> bool:
    indices: int = 0
    if len(a) != len(b):
        return False
    while indices < len(a):
        if a[indices] != b[indices]:
            return False
        indices += 1
    return True