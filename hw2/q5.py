import numpy as np
import math
import matplotlib.pyplot as plt


A = 1.5
B = 0.7
K = 0.3
K = 2
SAMPLES = 100


def get_equi_affine_curve(curve):
    equi_affine_values = [np.random.uniform(0.5,1.5),np.random.uniform(0,1),np.random.uniform(0.5,1.5)]
    # condition for equi affine transformation is determinant = 1
    # so in matrix [a,b]
    #              [c,d]
    # assuming a!= 0
    # d = (1+bc)/a
    equi_affine_values.append((1+equi_affine_values[1]*equi_affine_values[2])/equi_affine_values[0])
    equi_affine_matrix = np.array([[equi_affine_values[0],equi_affine_values[1]],[equi_affine_values[2],equi_affine_values[3]]])
    equi_affine_curve = equi_affine_matrix @ np.vstack((curve[0].copy(),curve[1].copy()))
    equi_affine_kappa = get_kappa(equi_affine_curve[0],equi_affine_curve[1])
    return equi_affine_curve,equi_affine_kappa

def get_euclidian_curve(curve):
    rotation_deg = np.random.uniform(0,np.pi*2)
    rotation_matrix = np.array([[math.cos(rotation_deg),-math.sin(rotation_deg)],[math.sin(rotation_deg), math.cos(rotation_deg)]])
    translation_vec = np.array([[np.random.uniform(0,5)],[np.random.uniform(0,5)]])
    euclidian_curve = rotation_matrix @ np.vstack((curve[0].copy(),curve[1].copy()))
    euclidian_curve += translation_vec
    euclidian_kappa = get_kappa(euclidian_curve[0],euclidian_curve[1])
    return euclidian_curve,euclidian_kappa

def sample_curve():
    deg = np.linspace(0,2*np.pi,SAMPLES,endpoint=False)
    x = [A*math.cos(deg) for deg in deg]
    y = [B*math.sin(deg)*(1+K*math.cos(deg)) for deg in  deg]
    return np.array(x),np.array(y)

def get_kappa(x,y):
    dx = get_periodic_gradient(x)
    dy = get_periodic_gradient(y)
    dxx = get_periodic_gradient(dx)
    dyy = get_periodic_gradient(dy)

    kappa = ( dx * dyy - dy*dxx) / ((np.square(dx) + np.square(dy))**(3/2))
    
    ds_dt = np.sqrt( np.square(dx.copy()) + np.square(dy.copy()))
    dk_dt = get_periodic_gradient(kappa)

    kappa_s = dk_dt / ds_dt

    return kappa, kappa_s

def get_periodic_gradient(arr):
    # Using this instead of np.gradient since it does not handle the fact that the graph is a closed loop well
    # and calculates the last and first derivitive wrong
    return (np.roll(arr, -1) - np.roll(arr, 1)) / 2


def plot_curve(curves):
    num_plots = len(curves)
    # Create a grid: 2 rows (shape vs. signature), num_plots columns
    fig, axes = plt.subplots(2, num_plots, figsize=(4 * num_plots, 8))

    # If num_plots is 1, axes is 1D, so we force it to 2D for consistency
    if num_plots == 1:
        axes = axes.reshape(2, 1)

    labels = ["Original", "Equi-Affine", "Euclidean"]

    for i, (curve_data, signature_data) in enumerate(curves):
        # --- Top Row: The Closed Curve (x vs y) ---
        ax_curve = axes[0, i]
        
        # Close the loop for visualization by appending the first point to the end
        x_plot = np.append(curve_data[0], curve_data[0][0])
        y_plot = np.append(curve_data[1], curve_data[1][0])
        
        ax_curve.plot(x_plot, y_plot, color='blue', linewidth=2)
        ax_curve.set_title(f"{labels[i]} Shape")
        ax_curve.axis('equal') 
        ax_curve.grid(True)

        # --- Bottom Row: The Signature Curve (kappa vs kappa_s) ---
        ax_sig = axes[1, i]
        
        kappa = signature_data[0]
        kappa_s = signature_data[1]
        
        # Plot kappa on x-axis and kappa_s on y-axis
        ax_sig.plot(kappa, kappa_s, color='red', linewidth=1.5)
        ax_sig.set_title(f"{labels[i]} Signature")
        ax_sig.set_xlabel(r"$\kappa$")
        ax_sig.set_ylabel(r"$\kappa_s$")
        ax_sig.grid(True)
        ax_sig.axis('equal')

    plt.tight_layout()
    plt.show()

def demonstrate_cartan():
    curve = sample_curve()
    kappa = get_kappa(curve[0],curve[1])

    equi_affine_curve, equi_affine_kappa = get_equi_affine_curve(curve)

    euclidian_curve, euclidian_kappa = get_euclidian_curve(curve)

    plot_curve([(curve,kappa),(equi_affine_curve,equi_affine_kappa),(euclidian_curve,euclidian_kappa)])




if __name__ == "__main__":
    demonstrate_cartan()

