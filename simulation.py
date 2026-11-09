##test
import random
random.seed(42)
def schaetze_pi(anzahl_punkte):
    punkte_im_kreis = 0
    for _ in range(anzahl_punkte):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            punkte_im_kreis += 1
    return (punkte_im_kreis / anzahl_punkte) * 4

anzahl = 100000
pi_wert = schaetze_pi(anzahl)
print(f"Monte-Carlo-Ergebnis für Pi nach {anzahl} Punkten: {pi_wert}")
