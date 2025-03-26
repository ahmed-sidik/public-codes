import numpy as np
import matplotlib.pyplot as plt

# Parametry generatora rejestru przesuwnego (LSFR)
def lfsr(seed, taps, n):
    """Generator LFSR (Linear Feedback Shift Register)"""
    state = seed
    numbers = []
    for _ in range(n):
        new_bit = sum([state >> t & 1 for t in taps]) % 2
        state = (state >> 1) | (new_bit << (len(bin(seed)) - 2))
        numbers.append(state & 1)
    return np.array(numbers)

# Parametry generatora liniowego
def linear_congruential_generator(a, c, M, seed, n):
    """Generator liniowy"""
    X = seed
    numbers = []
    for _ in range(n):
        X = (a * X + c) % M
        numbers.append(X / M)
    return np.array(numbers)

# Ustawienia
n = 100000  # Liczba generowanych liczb
seed = 12345  # Ziarno dla generatorów
a = 1664525  # Parametr generatora liniowego
c = 1013904223  # Parametr generatora liniowego
M = 2**32  # Modulo dla generatora liniowego
taps_lfsr = [32, 22]  # Współczynniki dla generatora rejestru przesuwnego (LSFR)

# Generowanie liczb
lfsr_numbers = lfsr(seed, taps_lfsr, n)
lcg_numbers = linear_congruential_generator(a, c, M, seed, n)

# Podział na 10 koszy
bins = np.linspace(0, 1, 11)

# Histogramy
plt.figure(figsize=(12, 6))

# Generator LFSR
plt.subplot(1, 2, 1)
plt.hist(lfsr_numbers, bins=bins, edgecolor='black', alpha=0.7)
plt.title('Rozkład generatora LFSR')
plt.xlabel('Wartość')
plt.ylabel('Liczba wystąpień')

# Generator liniowy
plt.subplot(1, 2, 2)
plt.hist(lcg_numbers, bins=bins, edgecolor='black', alpha=0.7)
plt.title('Rozkład generatora liniowego')
plt.xlabel('Wartość')
plt.ylabel('Liczba wystąpień')

plt.tight_layout()
plt.show()
