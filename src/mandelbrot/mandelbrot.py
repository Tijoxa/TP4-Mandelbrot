def suite(z, c) -> complex:
    """Générateur des éléments de la suite $z_{n+1}=z_n^2+c$
    
    c.f. Chapitre 2"""
    while True:
        yield z
        z = z ** 2 + c

def suite_mandelbrot(z=0, c=candidat) -> bool:
    """Renvoie la suite de Mandelbrot"""
    return suite(z, c)

def suite_julia(z=candidat, c=parametre) -> bool:
    """Renvoie la suite de julia pour candidat et parametre"""
    ...
    return suite(z, c)