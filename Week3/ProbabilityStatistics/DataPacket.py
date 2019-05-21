from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class DataSet:
    # each bit received error
    bit_error = 0.1

    # each packet consist of 1000 bits
    bit_packet = 1000

    data_mean = bit_error * bit_packet

    # Standard Deviation
    standard_deviation = (bit_error * (1 - bit_error)) ** 0.5

    # 120 errors in a certain data packet.
    packet_error = 120

    print(Utility.probability_data_packet(data_mean, standard_deviation, bit_error, bit_packet))

    z = 1 - 0.9821
    print("Probability of 120 errors in certain data packet:=", z)



data_obj = DataSet()
