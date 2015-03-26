from scipy.special import j1
def jinc(x):
    if x == 0.0:
        return 0.5
    return j1(x) / x
 