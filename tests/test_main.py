import sys

sys.path.append(".")

import src.mandelbrot.mandelbrot as mdl

def test_mandelbrot():
    assert not mdl.is_in_Mandelbrot(c=0.251, max_iter=100), "not passed"

def test_julia():
    assert mdl.is_in_Julia(z=0.25+0.25j, c=0.25), "not passed"

if __name__ == "__main__":
    test_mandelbrot()
    test_julia()