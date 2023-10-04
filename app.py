def addition(a, b):
    sum = a + b
    return sum

# Example usage:
number1 = 5
number2 = 3
result = addition(number1, number2)
print(f'The sum of {number1} and {number2} is {result}')

def test_answer():
    assert addition(3,5) == 5