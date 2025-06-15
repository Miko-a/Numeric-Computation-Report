import math

# Fungsi yang akan diintegrasikan
def f(x):
    return 1 / (1 + x**2)

# Metode Trapezoidal (sudah kamu buat)
def trapezoidal(x0, xn, n):
    h = (xn - x0) / n
    integration = f(x0) + f(xn)
    for i in range(1, n):
        k = x0 + i * h
        integration += 2 * f(k)
    integration *= h / 2
    return integration

# Metode Romberg Integration
def romberg(f, a, b, max_level):
    R = [[0.0] * (max_level + 1) for _ in range(max_level + 1)]

    # R[0][0] pakai metode trapezoid dengan 1 panel
    R[0][0] = (b - a) * (f(a) + f(b)) / 2

    for i in range(1, max_level + 1):
        n = 2**i
        h = (b - a) / n

        # Trapezoid level i: gunakan hasil sebelumnya dan tambahkan titik tengah
        sum_mid = sum(f(a + (k + 0.5) * h) for k in range(n // 2))
        R[i][0] = 0.5 * R[i - 1][0] + h * sum_mid

        # Richardson extrapolation
        for j in range(1, i + 1):
            R[i][j] = (4**j * R[i][j - 1] - R[i - 1][j - 1]) / (4**j - 1)

    return R

# Input dari user
a = float(input("Enter lower limit of integration: "))
b = float(input("Enter upper limit of integration: "))
n = int(input("Enter number of sub intervals (for trapezoidal): "))
max_romberg_level = int(input("Enter max level for Romberg (e.g. 4): "))

# Hitung dan tampilkan hasil metode trapezoidal
trap_result = trapezoidal(a, b, n)
print("\nIntegration result by Trapezoidal method: %0.10f" % trap_result)

# Hitung hasil Romberg
romberg_table = romberg(f, a, b, max_romberg_level)

# Tampilkan tabel Romberg
print("\nRomberg Integration Table:")
for i in range(max_romberg_level + 1):
    for j in range(i + 1):
        print("%0.10f" % romberg_table[i][j], end="\t")
    print()

# Hasil akhir Romberg adalah di pojok kanan bawah
final_romberg = romberg_table[max_romberg_level][max_romberg_level]
print("\nFinal result by Romberg method: %0.10f" % final_romberg)

# (Opsional) Bandingkan dengan nilai eksak jika integral dari 0 ke 1
if (a, b) == (0.0, 1.0):
    exact = math.atan(1)  # = pi/4
    print("Exact value (π/4): %0.10f" % exact)
    print("Error (Trapezoidal): %0.2e" % abs(exact - trap_result))
    print("Error (Romberg):     %0.2e" % abs(exact - final_romberg))
