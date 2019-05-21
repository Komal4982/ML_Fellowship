from Week3.LinearAlgebra.UtilityClass.UtilityClass import Utility


class RadarUnit:
    def __init__(self):
        self.X = 100
        self.mean = 90
        self.derivation = 10
        self.ztablevalue = 0.8413

    def findzscore(self):
        zscore = (self.X - self.mean) / self.derivation
        print(zscore)

        print(self.ztablevalue)
        print("\nthe probability that a car picked at random is travelling at more than 100 km/hr is equal to :=",
              round(1 - self.ztablevalue), 2)




radar_obj = RadarUnit()
radar_obj.findzscore()

