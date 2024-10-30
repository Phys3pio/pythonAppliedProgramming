import numpy as np
import matplotlib.pyplot as plt


v = int(input("Введите число v:"))
T = 1
N = 1024
dt = T / N
t = np.linspace(0, T, N, endpoint=False)


def f(t, v):
    return np.sin(v * np.cos(2 * np.pi * t))


signal = f(t, v)


spectrum = np.fft.fft(signal)
frequencies = np.fft.fftfreq(N, dt)


positive_frequencies = frequencies[:N//2]
positive_spectrum = spectrum[:N//2]

max_amplitude_idx = np.argmax(np.abs(positive_spectrum))
max_frequency = positive_frequencies[max_amplitude_idx]
max_amplitude = np.abs(positive_spectrum[max_amplitude_idx])


print(f"Максимальная амплитуда: {max_amplitude:.4f}")
print(f"Соответствующая частота: {max_frequency:.4f}")


plt.plot(positive_frequencies, np.abs(positive_spectrum))
plt.xlabel('Частота')
plt.ylabel('Амплитуда')
plt.title('Спектр функции')
plt.show()