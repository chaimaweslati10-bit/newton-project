import math
import matplotlib.pyplot as plt
import numpy as np

# Fonction
def f(x):
    return x**2 - 2

# Dérivée
def fp(x):
    return 2*x

# Valeur initiale
x = float(input("Donner une valeur initiale : "))

# Précision
epsilon = 1e-6

# Compteur
n = 0

print("\nTableau des itérations")
print("------------------------")

while True:

    # Formule de Newton
    xn = x - f(x)/fp(x)

    print("Iteration", n, ":", xn)

    if abs(xn - x) < epsilon:
        break

    x = xn
    n += 1

print("\nRacine approximative =", xn)

# --------------------------
# PARTIE GRAPHIQUE
# --------------------------

# Valeurs de x
X = np.linspace(-3, 3, 400)

# Valeurs de f(x)
Y = f(X)

# Tracer la fonction
plt.plot(X, Y)

# Axe horizontal
plt.axhline(0)

# Racine trouvée
plt.plot(xn, f(xn), marker='o')

# Titre
plt.title("Méthode de Newton")

# Affichage
plt.show()