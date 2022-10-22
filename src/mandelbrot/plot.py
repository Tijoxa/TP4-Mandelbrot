import mandelbrot as mdl # TODO: fix l'import si exécution dans un autre cd
from PIL import Image
import numpy as np 
from tqdm import tqdm

def plot_mandelbrot(zmin:complex=-1-1j,
                    zmax:complex=1+1j,
                    pixel_size:float=5e-4,
                    max_iter:int=50,
                    fig_name:str="fig_mandel"):
    """ Affiche l'ensemble de Mandelbrot pour une plage [zmin, zmax] et enregistre le résultat au format .png
    
    Paramètres
    ----------
    zmin: complex, optional
        La borne inférieure des données à évaluer (default vaut -1-1j)
    zmax: complex, optional 
        La borne supérieure des données à évaluer (default vaut 1+1j)
    pixel_size: float, optional
        La taille d'un pixel dans la figure (default vaut 5e-4)
    max_iter: int, optional 
        Le nombre d'itérations maximum pour calculer chaque suite de Mandelbrot (default vaut 50)
    fig_name: str, optional
        Le nom de la figure enregistrée est "fig_name".png (default vaut "fig_mandel")

    Retours
    -------
    None 

    """
    rmin, imin = zmin.real, zmin.imag
    rmax, imax = zmax.real, zmax.imag
    rdiff, idiff = rmax-rmin, imax-imin

    if rdiff > idiff:
        w, h = int(1/pixel_size), int(idiff/pixel_size/rdiff)
    else:
        w, h = int(rdiff/pixel_size/idiff), int(1/pixel_size)

    if rmin != rmax:
        X = np.linspace(rmin, rmax, w)
    else:
        X = np.array([rmin])
    if imin != imax:
        Y = np.linspace(imin, imax, h)
    else:
        Y = np.array([imin])

    ligne, colonne = len(X), len(Y)
    img = Image.new('L', (ligne, colonne), 255)

    stream = tqdm(X)
    stream.set_description("Génération de l'image")
    for enu_x, x in enumerate(stream):
        for enu_y, y in enumerate(Y):
            c = complex(x, y)
            if mdl.is_in_Mandelbrot(c, max_iter):
                img.putpixel((enu_x, enu_y), 0)
    img.save(f"src/mandelbrot/results/{fig_name}.png")

def plot_julia(c:complex,
               zmin:complex=-1-1j,
               zmax:complex=1+1j,
               pixel_size:float=5e-4,
               max_iter:int=50,
               fig_name:str="fig_mandel"):
    """ Affiche l'ensemble de Mandelbrot pour une plage [zmin, zmax] et enregistre le résultat au format .png
    
    Paramètres
    ----------
    c: complex
        Le parametre de calcul des suites de Julia 
    zmin: complex, optional
        La borne inférieure des données à évaluer (default vaut -1-1j)
    zmax: complex, optional 
        La borne supérieure des données à évaluer (default vaut 1+1j)
    pixel_size: float, optional
        La taille d'un pixel dans la figure (default vaut 5e-4)
    max_iter: int, optional 
        Le nombre d'itérations maximum pour calculer chaque suite de Mandelbrot (default vaut 50)
    fig_name: str, optional
        Le nom de la figure enregistrée est "fig_name".png (default vaut "fig_mandel")

    Retours
    -------
    None 

    """
    rmin, imin = zmin.real, zmin.imag
    rmax, imax = zmax.real, zmax.imag
    rdiff, idiff = rmax-rmin, imax-imin
    
    if rdiff > idiff:
        w, h = int(1/pixel_size), int(idiff/pixel_size/rdiff)
    else:
        w, h = int(rdiff/pixel_size/idiff), int(1/pixel_size)

    if rmin != rmax:
        X = np.linspace(rmin, rmax, w)
    else:
        X = np.array([rmin])
    if imin != imax:
        Y = np.linspace(imin, imax, h)
    else:
        Y = np.array([imin])

    ligne, colonne = len(X), len(Y)
    img = Image.new("L", (ligne, colonne), 255)

    stream = tqdm(X)
    stream.set_description("Génération de l'image")
    for enu_x, x in enumerate(stream):
        for enu_y, y in enumerate(Y):
            z = complex(x, y)
            if mdl.is_in_Julia(z, c, max_iter):
                img.putpixel((enu_x, enu_y), 0)
    img.save(f"src/mandelbrot/results/{fig_name}.png")

if __name__ == "__main__":
    plot_mandelbrot()