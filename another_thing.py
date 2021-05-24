def is_square(n):
    end_digit_condition = {0, 1, 4, 5, 6, 9}
    sum_condition = {1, 4, 7, 9}
    def adding_all_digits_until_one(n):
        # print(f"{n} is the number to add.")
        if len(str(n)) > 1:
            first = 0
            for q in str(n):
                _ = abs(int(q))
                second = _
                second = first + _
                first = _
                if str(_) == str(n)[-1]:
                     # print(f"Reached the end of summation loop and {second} is the result.") # If the iterated item is the last digit of the passed number, the loop is going to stop.
                     return second
                if len(str(second)) > 1:
                     return adding_all_digits_until_one(int(second)) # If the result contains more than one digit, then it is going to get passed into the function again.
        else:
            # print("The number is of one digit.")
            return n 
    if int(str(n)[-1]) in end_digit_condition and (adding_all_digits_until_one(int(n))) in sum_condition:
           return ("The number is a perfect square.") 
    else:
        return False
   

print(is_square(4))
