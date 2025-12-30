from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum

START_POINT = 50,50
A = np.array([[4,1],[1,2]])

def calculate_heat(image,i,j,time):
    dist_vec = np.array([(START_POINT[0] - i) ,(START_POINT[1] -j)]) 
    
    exponent_part = np.exp(-(np.matmul(np.matmul(dist_vec.transpose(),np.linalg.inv(A)),dist_vec))/(4*time))
    determinante = A[0][0]*A[1][1] - (A[0][1]**2)
    other_part = 1/(4*np.pi*time*((determinante)**1/2))
    return exponent_part * other_part

def step(image,time):
    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            image[i,j] = calculate_heat(image,i,j,time)


def display_image(image,timestep):
    # display original image


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # 1. Heatmap (as is) 🌡️
    im = ax1.imshow(image, cmap='gray')
    ax1.set_title(f"Heatmap at t={timestep}")
    ax1.axis('off')
    
    # 2. Contour Plot 🗺️
    # levels=15 adds more lines to see the detail of the spread
    cp = ax2.contour(X, Y, image, levels=15, cmap='viridis')
    ax2.set_title(f"Contours at t={timestep}")
    ax2.set_aspect('equal')
    plt.clabel(cp, inline=True, fontsize=8) # Adds temperature labels to lines
    
    plt.tight_layout()
    plt.show()

def simulate(image):
    # 1. Setup the coordinate grid for contours
    rows, cols = image.shape
    x = np.arange(cols)
    y = np.arange(rows)
    X, Y = np.meshgrid(x, y)
    
    # 2. Create a large figure: 2 rows (Heatmap, Contour) x 5 columns (Time steps)
    fig, axes = plt.subplots(2, 5, figsize=(22, 10))
    
    time_steps = [1, 250, 500, 750, 1000]
    
    for idx, time in enumerate(time_steps):
        # Calculate the heat distribution for this specific time
        # Note: 'step' in your script updates the 'image' array directly
        step(image, time)
        
        # --- Row 0: Heatmaps ---
        ax_heat = axes[0, idx]
        ax_heat.imshow(image, cmap='gray', origin='lower')
        ax_heat.set_title(f"Heatmap t={time}")
        ax_heat.axis('off')
        
        # --- Row 1: Contour Plots ---
        ax_cont = axes[1, idx]
        # 'levels' controls how many rings you see
        cp = ax_cont.contour(X, Y, image, levels=15, cmap='viridis')
        ax_cont.set_title(f"Contours t={time}")
        ax_cont.set_aspect('equal')
        plt.clabel(cp, inline=True, fontsize=8) 
            
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
 
    u_initial = np.zeros((100,100))
    simulate(u_initial)




