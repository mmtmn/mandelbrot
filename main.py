"""
1. Plot Mendelbrot in python - ok
2. Add time - ok
3. Add gravity - not sure how yet
4. Expand => add radiation for exemple
"""
import numpy as np
import matplotlib.pyplot as plt

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin,ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:,np.newaxis] * 1j

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        #z = z ** 2 + c
        z = z*(c**2) # e = m*c**2 .. let there be energy?
        # g=9.8
        # z = z*(c**2) + (g/c)
    return abs(z) <= 2

# np.warnings.filterwarnings("ignore")

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


def creator(pixel_color, duration):
    pixel_density=1
    i = 0
    for i in range(duration):
        c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density)
        members = get_members(c, num_iterations=20)
        plt.scatter(members.real, members.imag, color=pixel_color, marker=",", s=1)
        plt.gca().set_aspect("equal")
        plt.axis("off")
        plt.tight_layout()
        plt.pause(0.0000000001)
        pixel_density += 1
        i+=1


creator("black", 55)
creator("blue", 45)
creator("red", 35)
creator("green", 25)
creator("black", 15)
creator("yellow", 10)
creator("white", 5)
plt.show()
