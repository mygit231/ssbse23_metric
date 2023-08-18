from distance_indicator_sets import DistanceIndicator, euclidean_distance

''' We reuse the implmentation for IGD calculation in pymoo to calculate CID'''
class CID(DistanceIndicator):
    def __init__(self, Z, **kwargs):
        super().__init__(Z, euclidean_distance, 1, **kwargs)