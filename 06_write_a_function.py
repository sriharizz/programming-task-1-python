# Hackerrank: Write a Function — Leap Year
def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
    return leap

# Uncomment for testing:
# year = int(input())
# print(is_leap(year))
