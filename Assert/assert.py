
x = 1
y = 2

try:
    assert x == y, "x and y are not same"
except AssertionError as e:
    print(f"Assertion Error {e}")