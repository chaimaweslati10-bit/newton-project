# =========================
# IMPORTS
# =========================
import tkinter as tk
import math
import numpy as np
import matplotlib.pyplot as plt


# =========================
# FONCTION UTILISATEUR
# =========================
def get_function_from_text(expr):
    """
    transforme une expression texte en fonction mathématique
    exemple: "x**2 - 2"
    """

    # fonction f(x)
    def f(x):
        return eval(expr, {"x": x, "math": math})

    # dérivée numérique (approximation)
    def fp(x):
        h = 1e-5
        return (f(x + h) - f(x - h)) / (2 * h)

    return f, fp


# =========================
# MÉTHODE DE NEWTON
# =========================
def newton():

    # valeur initiale
    x = float(entry_x.get())

    # expression mathématique entrée par l'utilisateur
    expr = entry_f.get()

    # récupérer f et f'
    f, fp = get_function_from_text(expr)

    epsilon = 1e-6
    output = "Iterations:\n----------------\n"

    # boucle Newton
    for i in range(20):

        xn = x - f(x) / fp(x)

        output += f"Iteration {i} : x = {xn}\n"

        if abs(xn - x) < epsilon:
            break

        x = xn

    # afficher résultats
    result_label.config(text=output)

    # =========================
    # GRAPHIQUE
    # =========================
    X = np.linspace(-3, 3, 400)
    Y = [f(i) for i in X]

    plt.figure(figsize=(6, 4))
    plt.plot(X, Y, label="f(x)")
    plt.axhline(0)

    plt.plot(x, f(x), "ro", label="racine approx")

    plt.legend()
    plt.title("Méthode de Newton")
    plt.show()


# =========================
# INTERFACE TKINTER
# =========================
window = tk.Tk()
window.title("Newton Method Project")

# entrée fonction
label_f = tk.Label(window, text="Entrer f(x) :")
label_f.pack()

entry_f = tk.Entry(window)
entry_f.insert(0, "x**2 - 2")
entry_f.pack()

# entrée valeur initiale
label_x = tk.Label(window, text="Valeur initiale x0 :")
label_x.pack()

entry_x = tk.Entry(window)
entry_x.insert(0, "2")
entry_x.pack()

# bouton calcul
button = tk.Button(window, text="Calculer Newton", command=newton)
button.pack()

# résultat
result_label = tk.Label(window, text="", justify="left")
result_label.pack()

# lancement
window.mainloop()