from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum

class boundry_condition(Enum):
    NEUMANN = 1
    DIRICHLET = 2
    PERIODIC = 3


DIFFUSION_CONSTANT = 0.1

def central_difference(image,x,y,boundry_condition):
    max_x, max_y = image.shape
    if x == 0 or x == max_x-1 or y==0 or y==max_y-1:
        if boundry_condition == boundry_condition.NEUMANN:
            sum = - 4*image[x][y]
            if x==0: 
                sum +=  2* image[x+1][y] 
            elif x == max_x-1:
                sum += 2* image[x-1][y] 
            else:
                sum += image[x-1][y] + image[x+1][y] 
            if y==0:
                sum += 2* image[x][y+1]
            elif y== max_y-1:
                sum += 2* image[x][y-1]
            else:
                sum += image[x][y-1] + image[x][y+1] 
            return sum
        elif boundry_condition == boundry_condition.DIRICHLET:
            return 0
        elif boundry_condition == boundry_condition.PERIODIC:
            sum = - 4*image[x][y]
            if x==0: 
                sum += image[-1][y] + image[x+1][y]
            elif x == max_x-1:
                sum += image[x-1][y] + image[0][y]
            else:
                sum += image[x-1][y] + image[x+1][y]
            if y==0:
                sum += image[x][-1] + image[x][y+1]
            elif y== max_y-1:
                sum += image[x][y-1] + image[x][0]
            else:
                sum += image[x][y-1] + image[x][y+1]
            return sum

    return image[x-1][y] + image[x+1][y] + image[x][y-1] + image[x][y+1] - 4*image[x][y]

def step(image,boundry_condition, timestep_size=1):
    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            image[i,j] = image[i,j] + timestep_size * DIFFUSION_CONSTANT * central_difference(image,i,j,boundry_condition)


def display_image(image,timestep):
    # display original image
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.title(f"Image at timestep ={timestep}")
    plt.axis('off') # Hide pixel coordinates for a cleaner look
    plt.show()

def simulate(image, b_cond, timestep_size=1):
    # Create a figure with 5 subplots in a row
    fig, axes = plt.subplots(1, 5, figsize=(20, 5))
    plot_idx = 0
    
    for i in range(1001):
        step(image, b_cond, timestep_size)
        if i % 250 == 0:
            # Display image on the specific axis
            axes[plot_idx].imshow(image, cmap='gray')
            axes[plot_idx].set_title(f"t = {i}")
            axes[plot_idx].axis('off')
            plot_idx += 1
            
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load the image into grayscale np array
    img = Image.open('hw/hw1/images/grayscale_image.jpg')

    img_gray = img.convert('L')

    u_initial = np.array(img_gray, dtype=float)
    simulate(u_initial,boundry_condition.DIRICHLET,timestep_size=2)




