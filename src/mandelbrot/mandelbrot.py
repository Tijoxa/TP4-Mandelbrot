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
    Z = suite_mandelbrot(c)
    i = 0 
    while abs(next(Z)) <= 2 and i < max_iter:
        i+= 1
    return i == max_iter

def is_in_Julia(z:complex, c:complex, max_iter:int=50):
    Z = suite_julia(z,c)
    i = 0 
    while abs(next(Z)) <= 2 and i < max_iter:
        i+= 1
    return i == max_iter