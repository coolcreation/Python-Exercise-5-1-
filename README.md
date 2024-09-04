# Python-Exercise-5-1-
SWDV210 Week_3 Lab_1



```python

#!/usr/bin/env python3
# Jeff Bohn
# SWDV-210 Week_3 Lab_1
# 9/3/2024
# main.py

"""
Chapter #5 - Test & Debug

List the valid entries that I'm going to make and the correct results for each set of entries:

30, 60, 90 = should be 180, average score 60
0, 20, 40, 60, 80 = should be 200, average score 40
10, 30.6, 0, 100 = should be 140.6, average score 35.15
20.1, 20.5, 20.9 = should be 61.5, average score 20.5

List the invalid entries that I'm going to make. These should include entries that test the limits
of the allowable values, and test data type discrepancies:

Test Number Limits:   -1, 0, 0.01, 1, 99, 99.99, 100.01, 101
Test Data Type:       'A', 'X', %', '', '\n', 1 1

"""
 
import validation

def main():
    
    # display a welcome message
    print("The Test Scores application\n")
    print("Enter test scores")
    print("Enter 'x' to end input")
    print("======================")

    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0

    while True:
        test_score = validation.validation(input("Enter test score (or 'x' to quit): "))  # add validation function
        print(f"This is my return value {test_score}")
        print(f"Test scores is: {bool(test_score)}")
        if test_score != "x":
            # counter += 1
            print(counter)  # added this as a check point, and (counter += 1) isn't needed
        else:
            break
        
        if test_score is not None and test_score >= 0 and test_score <= 100:    
            score_total += test_score
            counter += 1
            print(counter, test_score, score_total)
        else:
            print("Test score must be from 0 through 100. Score discarded. Try again.")

    # calculate average score & make sure counter is a number, round to 2 decimal places to keep precision
    average_score = round(score_total / int(counter), 2)  

    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}" f"\nAverage Score: {average_score}")
    print()
    print("Bye")

if __name__ == '__main__':
    main()
```



```python

# Jeff Bohn
# SWDV-210 Week_3 Lab_1
# 9/3/2024
# validation.py

"""
Input type should be string, not float. \n
Return value should be float or 'x', otherwise return None.

"""

#  Need to add this validation function to filter items not a float, or not 'x'
def validation(prompt):
    if(prompt == "x"):
       return 'x'
    else:
       try:
          val = float(prompt)
          if val == 0.0:
              val = 0
          return val
       except:
          print("Not a number, and certainly not 'x'")
          return None

```
