from scipy import interpolate


def cspline_interp(a,b,c):

    coefficients = interpolate.splrep(b, c)
    result = interpolate.splev(a,coefficients)
    
    return result
