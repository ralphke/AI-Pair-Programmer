# Write a Python function to display a Mandelbrot image.
# The function should:
# 1. Create a complex plane.
# 2. Iterate over each point in the plane.
# 3. Apply the Mandelbrot set formula.
# 4. Color each point based on the number of iterations.
# 5. Display the image using matplotlib.
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def display_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    
    plt.imshow(n3.T, cmap='hot', extent=[xmin, xmax, ymin, ymax])
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.show()

def main():
# Call the functions
    print(mandelbrot(0 + 0j, 1000))  # Example call to mandelbrot function
    # Example call to display_mandelbrot function
    display_mandelbrot(-2.0, 1.0, -1.5, 1.5, 1000, 1000, 100)

if __name__ == "__main__":
    main()