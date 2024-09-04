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