import numpy as np

from pymoo.core.sampling import Sampling
from pymoo.util.normalization import denormalize

''' 
    For the study we sample for every dimension the same number of samples (=n_samples_single); 
    but it is customizable for every dimension
'''
def cartesian_by_bounds(n_var, xl, xu, n_samples_single=10):
    n_samples_by_axis = [n_samples_single] * n_var 
    X = [np.linspace(0, 1, n) for n in n_samples_by_axis]
    grid = np.meshgrid(*X)
    grid_reshaped = [axis.reshape(-1) for axis in grid]
    val = np.stack(grid_reshaped, axis=1)
    return denormalize(val, xl, xu)


def cartesian(problem, n_samples_by_axis):
    return cartesian_by_bounds(problem.n_var, problem.xl, problem.xu, n_samples_by_axis=n_samples_by_axis)


class GridSampling(Sampling):
    def _do(self, problem, n_samples_by_axis, **kwargs):
        return cartesian(problem, n_samples_by_axis=n_samples_by_axis)
