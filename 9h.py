import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def osciloscopio(frecuencia, tipo_onda, amplitud, duracion):
    # Frecuencia de muestreo
    fs = 44100

    # Generación de la señal
    tiempo = np.linspace(0, duracion, 50000, endpoint=False)
    if tipo_onda == "sine":
        onda = amplitud * np.sin(2*np.pi*frecuencia*tiempo)
    elif tipo_onda == "sawtooth":
        onda = amplitud * (2 * np.mod(frecuencia*tiempo,1)-1)
    elif tipo_onda == "square":
        onda = amplitud * np.sign(np.sin(2*np.pi*frecuencia*tiempo))
    elif tipo_onda == "triangle":
        onda = amplitud * (np.abs(np.mod(frecuencia*tiempo,1)-0.5)-0.25) * 4

    # Dibujar la señal
    fig, ax = plt.subplots()
    ax.plot(tiempo, onda)

    # Configuración del eje x
    ax.set_xlim([0, duracion])

    # Configuración del eje y
    ax.set_ylim([-1.2*amplitud, 1.2*amplitud])

    # Etiquetas de los ejes
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Amplitud')

    # Mostrar el gráfico
    plt.show()

    # Reproducir el sonido
    sd.play(onda, fs)

    # Esperar a que termine la reproducción
    sd.wait()

osciloscopio(0.05,"sine",1392,100)