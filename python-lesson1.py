# for i in range(1,101):
#     if (i % 3 == 0) and i % 5 == 0:
#         print("FIZZBUZZ")
#     elif i % 3 == 0:
#         print("FIZZ")
#     elif i % 5 == 0:
#         print("BUZZ")


def fizzbuzz(start, end):
    for i in range(start,end):
        if (i % 3 == 0) and i % 5 == 0:
            print("FIZZBUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        elif i % 5 == 0:
            print("BUZZ")

fizzbuzz(1,101)
