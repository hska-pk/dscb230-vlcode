
# # ZeroDivisionError
# x = 10
# y = 0
# z = x / y  # y ist 0 --> unzulässig

# # ModuleNotFoundError
# import notexisting  # Package existiert nicht

# # NameError
# x = NotExistingClass()  # Anlegen eines Objekts ohne existierende Klasse

# # FileNotFoundError
# f = open("notexistingfile.txt", "r")

# Einleiten des kritischen Code-Blocks
# try:
#     a = int(input("Dividend:"))  # könnte auch vor dem "try" stehen!
#     b = int(input("Divisor:"))  # könnte auch vor dem "try" stehen!
#     print(f"Quotient = {a/b}")  # muss in den try-except-block!
# except:
#     print("Unzulässige Eingabe")  # wird bei Fehler ausgeführt



# # Einleiten des kritischen Code-Blocks
# try:
#     a = int(input("Dividend:"))  # könnte auch vor dem "try" stehen!
#     b = int(input("Divisor:"))  # könnte auch vor dem "try" stehen!
#     print(f"Quotient = {a/b}")  # muss in den try-except-block!
#     print(f"Summe = {a+b}")  # muss in den try-except-block!
# except ValueError as e:  
#     print(f"Zahlenkonvertierung fehlgeschlagen ({e}")
# except ZeroDivisionError as e:
#     print(f"Division durch 0 unzulässig ({e})")
# except Exception as e:
#     print(f"Etwas anderes ist nicht in Ordnung ({e})")
# else:
#     print("Keine Fehler")
# finally:
#     print("Wird immer ausgeführt")


# def get_ratios(l1, l2):
#     """ Assumption: l1 and l2 are lists of equal length containing numbers
#         Returns: a list containing the ration l1[i]/l2[i] for each list element i"""
#     ratios = []  # holds the ratios to be returned

#     if len(l1) != len(l2):
#         raise ValueError('lists have different lengths')

#     for idx, el1 in enumerate(l1):
#         try:
#             ratios.append(el1 / l2[idx])
#         except (ZeroDivisionError, ValueError, TypeError) as e:
#             # handle issues with types and values by adding nan to the returning list
#             ratios.append(float('nan')) # add nan = not a number
#         except Exception as e:
#             # default error in case of any other issue - raise exception
#             raise ValueError(f'get_ratios called with bad arguments: {e}')
#     return ratios

# print(get_ratios([1,'a',3], [0,0,1]))


# class SalaryNotInRangeError(ValueError):
#     """ Exception raised for errors in the input salary.
#         Assumptions: rasing the exception requires the attribute salary and 
#         optionally message for a particular explanation of the error
#     """

#     def __init__(self, salary, message="Salary is not in range (5000, 15000)"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)


# salary = int(input("Enter salary amount: "))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary)



class Multiplier():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def multiply(self):
        return self._x * self._y


import unittest
class TestMultiplierMethods(unittest.TestCase):

    def test_multipy(self):
        mult1 = Multiplier(10, 20.2)
        mult2 = Multiplier(-2, 5)
        mult3 = Multiplier(-2.2, -5)
        self.assertEqual(mult1.multiply(), 202)
        self.assertEqual(mult2.multiply(), -10)
        self.assertEqual(mult3.multiply(), 11)

    def test_multiply_types(self):
        self.assertRaises(TypeError, Multiplier('a', 19).multiply())

unittest.main()

#assert(Multiplier(10, 20).multiply() == 200)
