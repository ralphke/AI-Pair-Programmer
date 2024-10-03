import numpy as np
# Import the functions from Voice.py
from Mandelbrot import mandelbrot, display_mandelbrot

def test_mandelbrot():
    # Test case 1: Point inside the Mandelbrot set
    assert mandelbrot(0 + 0j, 1000) == 1000

    # Test case 2: Point outside the Mandelbrot set
    assert mandelbrot(2 + 2j, 1000) == 1

    # Test case 3: Point on the boundary of the Mandelbrot set
    assert mandelbrot(-0.75 + 0.1j, 1000) > 1

def test_display_mandelbrot():
    # Test case 1: Check if the function runs without errors
    try:
        display_mandelbrot(-2.0, 1.0, -1.5, 1.5, 100, 100, 256)
    except Exception as e:
        assert False, f"Function raised an exception: {e}"

    # Test case 2: Check the shape of the generated array
    xmin, xmax, ymin, ymax, width, height, max_iter = -2.0, 1.0, -1.5, 1.5, 100, 100, 256
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    
    assert n3.shape == (width, height)

def main():
    # Run the test function
    test_mandelbrot()
    test_display_mandelbrot()
    print("All test cases passed!")

if __name__ == "__main__":
    main()