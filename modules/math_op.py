from scipy import interpolate

# 1. Cubic Spline Interpolation

def cspline_interp(a,b,c):

    coefficients = interpolate.splrep(b, c)
    result = interpolate.splev(a, coefficients)
    
    return result

# 2. 1st Derivative of the Interpolated Cubic Spline

def cspline_deriv(a, b, c):

    coefficients = interpolate.splrep(b, c)
    result = interpolate.splev(a, coefficients, der=1)
    
    return result

# 2. Iterative Solver using a simplified Golden Search Algorithm

    # The maxima minima between which the solution is searched must be clearly defined

def itr_sol_search(func_name, var_min, var_max):    
    
    while True:
        
        var_avg = (var_min + var_max)/2

        solution = func_name(var_avg)

        if  ( round(solution,4) == 0 ):
            break
        elif ( solution > 0 ):  
            var_max = var_avg
        elif ( solution < 0 ):
            var_min = var_avg

    return var_avg

