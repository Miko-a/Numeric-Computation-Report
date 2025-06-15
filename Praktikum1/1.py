"""
Metode Regula Falsi (False Position)
------------------------------------
• Menunjukkan iterasi numerik di terminal
• Menggambar kurva f(x) dan menandai akar aproksimasi
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Definisi fungsi
def f(x: float) -> float:
    return x**2 - 2          # ganti di sini bila mau fungsi lain

# 2. Implementasi Regula Falsi
def false_position(x0: float,
                   x1: float,
                   eps: float = 1000000,
                   max_iter: int = 100):
    """
    Mengembalikan (akar_aproksimasi, jumlah_iterasi)
    """
    if f(x0) * f(x1) >= 0:
        raise ValueError("Interval tidak mengurung akar (f(x0)·f(x1) ≥ 0).")

    print(f"{'N':^4}{'x0':>12}{'x1':>12}{'f(x0)':>12}{'f(x1)':>12}{'x':>12}{'f(x)':>12}")
    x_prev = None
    for n in range(max_iter):
        # rumus Regula Falsi
        x = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print(f"{n:4d}{x0:12.6f}{x1:12.6f}{f(x0):12.6f}{f(x1):12.6f}{x:12.6f}{f(x):12.6f}")

        # kriteria konvergensi: |f(x)| maupun |Δx|
        if abs(f(x)) < eps or (x_prev is not None and abs(x - x_prev) < eps):
            return x, n

        # perbaharui batas interval
        if f(x0) * f(x) < 0:
            x1 = x
        else:
            x0 = x
        x_prev = x

    raise RuntimeError("Melebihi jumlah iterasi maksimum.")

# 3. --- Main Program ---
if __name__ == "__main__":
    # input sederhana (bisa diganti hard‑code utk demo)
    x0 = float(input("Masukkan x0 (batas bawah): "))
    x1 = float(input("Masukkan x1 (batas atas): "))
    eps = float(input("Masukkan toleransi galat: "))

    root, n_iter = false_position(x0, x1, eps)
    print(f"\nAkar aproksimasi setelah {n_iter} iterasi: {root:.10f}")

    # 4. Plot fungsi + akar
    # rentang plot sedikit di luar interval supaya kurva jelas
    xmin, xmax = min(x0, x1) - 1, max(x0, x1) + 1
    X = np.linspace(xmin, xmax, 400)
    Y = f(X)

    plt.figure()
    plt.axhline(0, linewidth=0.6)
    plt.plot(X, Y, label="f(x)")
    plt.scatter([root], [0], s=60, marker="o", label=f"akar ≈ {root:.6f}")
    plt.title("Metode Regula Falsi")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
