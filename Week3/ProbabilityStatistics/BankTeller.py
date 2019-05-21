from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class BankTeller:
    # mean value
    mean = 2

    # standard_deviation
    standard_deviation = 1 ** 0.5

    # number of customer
    cust_num1 = 50

    cust_num2 = 90

    cust_num3 = 110

    print(Utility.probability_customer(mean, standard_deviation, cust_num1, cust_num2, cust_num3))
    z = 0.9207 - 0.793
    print("probability:=", z)


teller_obj = BankTeller()


