import mandelbrot as mdl # TO DO: fix ça
from PIL import Image
import numpy as np 
from tqdm import tqdm

def plot_mandelbrot(zmin:complex=1-1j,
                    zmax:complex=1+1j,
                    pixel_size:float=5e-7,
                    max_iter:int=50,
                    fig_name:str="fig_mandel"):
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
    rmin, imin = zmin.real, zmin.imag
    rmax, imax = zmax.real, zmax.imag
    rdiff, idiff = rmax-rmin, imax-imin
    X = np.arange(rmin, rmax, pixel_size)
    Y = np.arange(imin, imax, pixel_size)
    ligne, colonne = len(X), len(Y)
    img = Image.new('L', (ligne, colonne), 255)

    stream = tqdm(X)
    stream.set_description("Génération de l'image")
    for x in stream:
        for y in Y:
            c = complex(x, y)
            if mdl.is_in_Mandelbrot(c, max_iter):
                tup = (int(ligne*(x-rmin)/rdiff), int(colonne*(y-imin)/idiff))
                img.putpixel(tup, 0)
    img.resize((2000, 2000))
    img.show()
    img.save(f"{fig_name}.png")

def plot_julia(c:complex,
               zmin:complex=1-1j,
               zmax:complex=1+1j,
               pixel_size:float=5e-7,
               max_iter:int=50,
               fig_name:str="fig_mandel"):
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
    rmin, imin = zmin.real, zmin.imag
    rmax, imax = zmax.real, zmax.imag
    rdiff, idiff = rmax-rmin, imax-imin
    X = np.arange(rmin, rmax, pixel_size)
    Y = np.arange(imin, imax, pixel_size)
    ligne, colonne = len(X), len(Y)
    img = Image.new('L', (ligne, colonne), 255)

    stream = tqdm(X)
    stream.set_description("Génération de l'image")
    for x in stream:
        for y in Y:
            z = complex(x, y)
            booleen = mdl.is_in_Julia(z, c, max_iter)
            if booleen:
                tup = (int(ligne*(x-rmin)/rdiff), int(colonne*(y-imin)/idiff))
                img.putpixel(tup, 0)
    img.resize((2000, 2000))
    img.show()
    img.save(f"{fig_name}.png")

if __name__=='__main__':
    plot_mandelbrot()