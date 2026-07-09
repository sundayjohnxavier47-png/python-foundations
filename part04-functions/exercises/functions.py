
def add(x, y):
    return x + y

def is_even(n):
    return n % 2 == 0
    """
    if n % 2 == 0:
        return True
    else:
        return False
"""
def greet_user(name="Guest"):
    print(f"Hello {name}!")

print(add(3,5))
print(is_even(12))
greet_user()
greet_user("Xavier")