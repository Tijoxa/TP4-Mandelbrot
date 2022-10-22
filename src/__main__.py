import argparse
from mandelbrot.plot import plot_julia,plot_mandelbrot

def main():
    """Main Function of the module. Plots a Mandelbrot or a Julia ensemble based on given arguments """
    parser = argparse.ArgumentParser(description='Plot a Mandelbrot or a Julia ensemble.')
    group = parser.add_mutually_exclusive_group() # Ajouté afin de ne pas pouvoir sélectionner "Mandelbrot" et "Julia" en même temps

    group.add_argument('--mandelbrot', '-m', action="store_true",
                        help='Plot Mandelbrot ensemble. Exclusive with --julia')
    group.add_argument('--julia', '-j', action="store_true",
                        help='Plot Julia ensemble. Exclusive with --mandelbrot')
    parser.add_argument('--zmin', type=complex, default=-1-1j,
                        help='minimum complex to plot')
    parser.add_argument('--zmax', type=complex, default=1+1j,
                        help='maximum complex to plot')    
    parser.add_argument('--c', type=complex, 
                        help='candidate of the Julia ensemble')   
    parser.add_argument('--pixel_size', '-ps', metavar='pixel_size', type=float, default=5e-4,
                        help='size of the pixel to draw')                 
    parser.add_argument('--max_iter', '-m_i', metavar='max_iter', type=int, default=50,
                        help='maximum iterations to check ensemble membership')
    parser.add_argument('--output', '-o',metavar='output', type=str, default="fig",
                        help='name of the image to save')

    args = parser.parse_args()
    mandelbrot = args.mandelbrot

    if mandelbrot :  
        plot_mandelbrot(args.zmin,args.zmax,args.pixel_size,args.max_iter,args.output)
    else:
        c = args.c
        assert c is not None, "A candidate c is required to plot a Julia ensemble"
        plot_julia(c,args.zmin,args.zmax,args.pixel_size,args.max_iter,args.output)

if __name__ == "__main__":
    main()