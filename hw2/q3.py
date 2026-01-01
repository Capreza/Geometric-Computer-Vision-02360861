import numpy as np
import math
import matplotlib.pyplot as plt
from enum import Enum

class evolution_type(Enum):
    CONSTANT = 1
    CURVATURE = 2
    EQUI_AFFINE = 3


BASE_RADIUS = 1.0
AMPLITUDE = 0.4
NUM_POINTS = 5
SAMPLES = 100
EVOLUTION_TYPE = evolution_type.EQUI_AFFINE
TIMESTEP = 0.002
EQUI_AFFINE_TRANSFORMATION = np.array([[1.0, 0.5],[0.0, 1.0]])

def sample_curve():
    deg = np.linspace(0,2*np.pi,SAMPLES,endpoint=False)
    x = [(BASE_RADIUS + AMPLITUDE*math.cos(NUM_POINTS*deg))*math.cos(deg) for deg in deg]
    y = [(BASE_RADIUS + AMPLITUDE*math.cos(NUM_POINTS*deg))*math.sin(deg) for deg in  deg]
    return np.array(x),np.array(y)

def plot_equi_affine_curve(history_list):
    # history_list contains tuples: [(orig_t0, trans_t0), (orig_t1, trans_t1), ...]
    
    num_cols = len(history_list)
    # Create 2 rows, N columns
    fig, axes = plt.subplots(2, num_cols, figsize=(3 * num_cols, 8))
    
    # Calculate Inverse matrix to "undo" the distortion for the second row
    M_inv = np.linalg.inv(EQUI_AFFINE_TRANSFORMATION)

    for i, (orig, trans) in enumerate(history_list):
        # --- Row 1: Original Curve ---
        ax1 = axes[0, i]
        
        # Close loop visually
        x_orig = np.append(orig[0], orig[0][0])
        y_orig = np.append(orig[1], orig[1][0])
        
        ax1.plot(x_orig, y_orig, 'b-', linewidth=2)
        ax1.set_title(f"Original Iter {i*20}")
        ax1.axis('equal')
        ax1.grid(True)
        ax1.set_xlim(-1.5, 1.5)
        ax1.set_ylim(-1.5, 1.5)

        # --- Row 2: Transformed (Restored) ---
        ax2 = axes[1, i]
        
        # Apply Inverse Matrix to bring it back to original space
        x_orig = np.append(trans[0], trans[0][0])
        y_orig = np.append(trans[1], trans[1][0])
        restored = M_inv @ trans
        

        x_restored = np.append(restored[0], restored[0][0])
        y_restored = np.append(restored[1], restored[1][0])
        
        ax2.plot(x_orig, y_orig, linewidth=2)

        ax2.plot(x_restored, y_restored, 'r--', linewidth=2)
        
        ax2.set_title(f"Restored Iter {i*20}")
        ax2.axis('equal')
        ax2.grid(True)
        ax2.set_xlim(-1.5, 1.5)
        ax2.set_ylim(-1.5, 1.5)

    plt.suptitle("Top: Normal Evolution | Bottom: Transformed -> Evolved -> Restored (Should match Top)")
    plt.tight_layout()
    plt.show()

def plot_curve(curves):
    num_plots = len(curves)
    fig, axes = plt.subplots(1, num_plots, figsize=(3 * num_plots, 4))

    for i, (ax, curve) in enumerate(zip(axes, curves)):
        # VISUAL FIX: Manually close the loop for plotting
        # We wrap the first point (index 0) to the end
        x_plot = np.append(curve[0], curve[0][0])
        y_plot = np.append(curve[1], curve[1][0])
        ax.plot(x_plot, y_plot, color='blue', linewidth=2)
        ax.set_title(f"Iteration {i*20}")
        ax.axis('equal') # Keeps the star shape correct
        ax.grid(True)
        
        # Optional: Fix the axis limits so you can see the curve shrinking relative to the frame
        # If you comment these out, each plot will zoom in on the curve
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)

    plt.tight_layout()
    plt.show()

def get_periodic_gradient(arr):
    # Using this instead of np.gradient since it does not handle the fact that the graph is a closed loop well
    # and calculates the last and first derivitive wrong
    return (np.roll(arr, -1) - np.roll(arr, 1)) / 2

def step(curve):
    dx = get_periodic_gradient(curve[0])
    dy = get_periodic_gradient(curve[1])

    norm_arr = np.sqrt(dx**2 + dy**2)    
    normals = np.vstack((-dy, dx)) / norm_arr
    
    if EVOLUTION_TYPE == evolution_type.CONSTANT:
            curve += normals * TIMESTEP
    else:
        dxx = get_periodic_gradient(dx)
        dyy = get_periodic_gradient(dy)
        kappa = ( dx * dyy - dy*dxx) / ((np.square(dx) + np.square(dy))**(3/2))
        if EVOLUTION_TYPE == evolution_type.CURVATURE:
            curve += normals*kappa * TIMESTEP
        if EVOLUTION_TYPE == evolution_type.EQUI_AFFINE:
            curve += normals*(np.cbrt(kappa)) * TIMESTEP

    return curve


def evolve_curve():
    curve = sample_curve()
    if EVOLUTION_TYPE == evolution_type.EQUI_AFFINE:
        equi_affine_curve = EQUI_AFFINE_TRANSFORMATION @ curve
    curve_copies = []
    for i in range(101):
        curve = step(curve)
        if EVOLUTION_TYPE == evolution_type.EQUI_AFFINE:
            equi_affine_curve = step(equi_affine_curve)
        if not i%20:
            if EVOLUTION_TYPE == evolution_type.EQUI_AFFINE:
                curve_copies.append(((curve[0].copy(),curve[1].copy()),(equi_affine_curve[0].copy(),equi_affine_curve[1].copy())))
            else:
                curve_copies.append((curve[0].copy(),curve[1].copy()))

    if EVOLUTION_TYPE == evolution_type.EQUI_AFFINE:
        plot_equi_affine_curve(curve_copies)
    else:
        plot_curve(curve_copies)
        
            




if __name__ == "__main__":
    evolve_curve()

