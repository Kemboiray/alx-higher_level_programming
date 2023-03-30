class MyClass:
    x = 10

obj = MyClass()

# attempt to retrieve a non-existent attribute using getattr
try:
    val = getattr(obj, 'y')
except AttributeError as e:
    print(f"AttributeError: {e}")
