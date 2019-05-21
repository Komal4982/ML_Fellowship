from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class Clinic:

    # 10% of patients are prescribed narcotic pain killers
    narcotic_painkillers = 0.1

    # not prescribed narcotic pain killers
    non_prescribed_painkillers = 0.05

    # prescribed pain pills, 8% are addicts.
    addicted_painkiller = 0.08

    # five percent of the clinic’s patients are addicted to narcotics pain killers
    addicted_non_prescribed_painkillers = 0.05

    result = Utility.prescribed_pain_pills(narcotic_painkillers, addicted_non_prescribed_painkillers,
                                           addicted_painkiller, non_prescribed_painkillers)
    print("probability that patient will be prescribed pain pills:=", result)


clinic_obj = Clinic()
