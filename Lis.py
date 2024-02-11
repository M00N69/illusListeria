import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

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

# Streamlit sliders for interactive input
T_min = st.slider('Température minimum (°C)', 70, 90, 70)
T_max = st.slider('Température maximum (°C)', 90, 100, 100)
time_min = st.slider('Durée minimum (min)', 1, 10, 1)
time_max = st.slider('Durée maximum (min)', 10, 15, 15)

# Fonction pour tracer le graphique interactif
def plot_interactive(T_min, T_max, time_min, time_max):
    temps = np.arange(T_min, T_max + 1, 1)
    times = np.arange(time_min, time_max + 0.5, 0.5)
    T, Time = np.meshgrid(temps, times)
    Reductions = calculate_log_reduction(T, Time)

    # Create a plot using Streamlit's Matplotlib functionality
    fig, ax = plt.subplots(figsize=(12, 8))
    contour = ax.contourf(T, Time, Reductions, levels=np.linspace(0, 10, 100), cmap='viridis')
    plt.colorbar(contour)
    ax.set_xlabel('Température (°C)')
    ax.set_ylabel('Durée (min)')
    ax.set_title('Réduction de Listeria monocytogenes dans les crevettes Vannamei')
    st.pyplot(fig)

# Calling the plotting function with the selected values
plot_interactive(T_min, T_max, time_min, time_max)
