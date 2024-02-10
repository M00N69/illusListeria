pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive

# Paramètres du modèle de destruction thermique
D_ref = 1.2  # D-value à 90°C en minutes
z_value = 7.5  # z-value
T_ref = 90  # Température de référence en °C
log_reduction_target = 3  # Réduction cible en log10

# Fonction pour calculer la D-value à une température donnée
def calculate_D_value(T):
    return D_ref * 10 ** ((T_ref - T) / z_value)

# Fonction pour calculer la réduction log10
def calculate_log_reduction(T, time):
    D_value = calculate_D_value(T)
    return time / D_value

# Fonction pour tracer le graphique interactif
def plot_interactive(T_min=70, T_max=100, time_min=1, time_max=15):
    temps = np.arange(T_min, T_max + 1, 1)
    times = np.arange(time_min, time_max + 0.5, 0.5)
    T, Time = np.meshgrid(temps, times)
    Reductions = calculate_log_reduction(T, Time)

    plt.figure(figsize=(12, 8))
    contour = plt.contourf(T, Time, Reductions, levels=np.linspace(0, 10, 100), cmap='viridis')
    plt.colorbar(contour)
    plt.xlabel('Température (°C)')
    plt.ylabel('Durée (min)')
    plt.title('Réduction de Listeria monocytogenes dans les crevettes Vannamei')
    plt.show()

# Widgets interactifs pour ajuster la plage de température et de durée
interactive_plot = interactive(plot_interactive,
                               T_min=(70, 90),
                               T_max=(90, 100),
                               time_min=(1, 10),
                               time_max=(10, 15))
interactive_plot
