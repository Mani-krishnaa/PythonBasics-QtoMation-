def multiplier(factor):
    def multiply_by_factor(number):
        return number * factor
    return multiply_by_factor


# Creating a function that multiplies by 3
times_three = multiplier(3)
print(times_three(10))  # Output: 30

# Creating a function that multiplies by 5
times_five = multiplier(5)
print(times_five(10))   # Output: 50


def sum(a):
    def sums(b):
        return a + b
    return sums


a = sum(10054984512)
print(a(20))
