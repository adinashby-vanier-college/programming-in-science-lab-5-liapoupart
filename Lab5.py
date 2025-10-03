# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    if n == 1:
        return "*"
    result = ""
        
    for i in range(1, n+1):
        if i == 1:
            result += n * "*" + "\n"
        elif i == n:
            result += n * "*"
        else:
            result += "*" + " " * (n-2) + "*" + "\n"
    return result

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range(1, n+1):
        line = ""
        for j in range(1, i+1):
            line += str(j)
        result += line + "\n"
    result = result.rstrip("\n")
    return result

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    for i in range(1, n+1):
        result += (" " * (n - i)) + ("*" * (2 * i - 1)) 
        if i != n:
            result += "\n"
        else:
            pass
    return result