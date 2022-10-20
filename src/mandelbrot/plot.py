import mandelbrot as mdl 

def plot_mandelbrot(zmin:complex=1-1j,zmax:complex=1+1j,pixel_size:float=5e-7,max_iter:int=50,fig_name:str="fig_mandel"):
    """ Affiche l'ensemble de Mandelbrot pour une plage [zmin,zmax] et enregistre le résultat au format .png
    
    Parametres
    ----------
    zmin : complex, optional
        La borne inférieure des données à évaluer (default vaut -1-1j)
    zmax : complex, optional 
        La borne supérieure des données à évaluer (default vaut 1+1j)
    pixel_size : float, optional
        La taille d'un pixel dans la figure (default vaut 5e-7)
    max_iter : int, optional 
        Le nombre d'itérations maximum pour calculer chaque suite de Mandelbrot (default vaut 50)
    fig_name : str, optional
        Le nom de la figure enregistrée est "fig_name".png (default vaut "fig_mandel")

    Retours
    -------
    None 

    """
    pass

def plot_julia(c:complex,zmin:complex=1-1j,zmax:complex=1+1j,pixel_size:float=5e-7,max_iter:int=50,fig_name:str="fig_mandel"):
    """ Affiche l'ensemble de Mandelbrot pour une plage [zmin,zmax] et enregistre le résultat au format .png
    
    Parametres
    ----------
    c : complex
        Le parametre de calcul des suites de Julia 
    zmin : complex, optional
        La borne inférieure des données à évaluer (default vaut -1-1j)
    zmax : complex, optional 
        La borne supérieure des données à évaluer (default vaut 1+1j)
    pixel_size : float, optional
        La taille d'un pixel dans la figure (default vaut 5e-7)
    max_iter : int, optional 
        Le nombre d'itérations maximum pour calculer chaque suite de Mandelbrot (default vaut 50)
    fig_name : str, optional
        Le nom de la figure enregistrée est "fig_name".png (default vaut "fig_mandel")

    Retours
    -------
    None 

    """
    pass