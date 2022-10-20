def suite(z, c) -> complex:
    """Générateur des éléments de la suite $z_{n+1}=z_n^2+c$
    
    c.f. Chapitre 2"""
    while True:
        yield z
        z = z ** 2 + c

def suite_mandelbrot(c:complex) -> bool:
    """Renvoie la suite de Mandelbrot"""
    return suite(0, c)

def suite_julia(z:complex, c:complex) -> bool:
    """Renvoie la suite de julia pour candidat et parametre"""
    ...
    return suite(z, c)

def is_in_Mandelbrot(c:complex, max_iter:int=50):
    """Calcule une suite de Mandelbrot et vérifie la non-divergence avec la condition $|z_n| <= 2 $
    >>> is_in_Mandelbrot(c=0.251)
    True
    >>> is_in_Mandelbrot(c=0.251,max_iter=100)
    False
    """
    Z = suite_mandelbrot(c)
    i = 0 
    while abs(next(Z)) <= 2 and i < max_iter:
        i+= 1
    return i == max_iter

def is_in_Julia(z:complex, c:complex, max_iter:int=50, eps:float=1e-3):
    """ Calcule une suite de Julia et vérifie la non-divergence, ainsi que la convergence des deux derniers termes
    >>> is_in_Julia(z=0.25+0.25j,c=0.25)
    True
    """
    Z = suite_julia(z, c)
    i = 0 
    z_old = z 
    z_cur = next(Z)
    while abs(z_cur) <= 2 and i < max_iter:
        z_old = z_cur
        z_cur = next(Z)
        i += 1
    return i == max_iter and abs(z_cur - z_old) < eps 

if __name__ == "__main__" :
    import doctest
    print(doctest.testmod(verbose=1))