
# Metode Regula Falsi (False Position)

## 1. Tujuan
Mengimplementasikan metode **Regula Falsi** dalam Python untuk menemukan akar dari suatu fungsi non-linier. Program menampilkan:
- Proses iterasi numerik
- Grafik kurva fungsi dan aproksimasi akar

---

## 2. Deskripsi Masalah
Diberikan fungsi \( f(x) \), dicari nilai \( x \) sedemikian hingga \( f(x) = 0 \), dengan metode Regula Falsi pada interval awal [x0, x1].

Metode Regula Falsi menggunakan pendekatan linear antara dua titik untuk menemukan akar dari fungsi kontinyu.

---

## 3. Fungsi Contoh
\[
f(x) = x^2 - 2
\]
Fungsi ini memiliki akar di \( \sqrt{2} \approx 1.4142 \), karena \( f(\sqrt{2}) = 0 \).

---

## 4. Rumus Regula Falsi
\[
x = x_0 - \frac{(x_1 - x_0) \cdot f(x_0)}{f(x_1) - f(x_0)}
\]

Setiap iterasi:
- Hitung nilai x baru
- Evaluasi f(x)
- Perbarui batas bawah atau atas sesuai tanda dari f(x)

---

## 5. Struktur Program

```python
def f(x):
    return x**2 - 2

def false_position(x0, x1, eps, max_iter=100):
    ...
    x = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
    ...
    return x, n_iter
```

---

## 6. Contoh Input
```
x0 = 1
x1 = 2
eps = 1e-6
```

## 7. Output Iterasi
```
N     x0         x1       f(x0)     f(x1)       x        f(x)
0  1.000000  2.000000  -1.000000  2.000000  1.333333  -0.222222
1  1.333333  2.000000  -0.222222  2.000000  1.400000  -0.040000
...
```

---

## 8. Visualisasi
Program secara otomatis memplot kurva fungsi dan menandai titik aproksimasi akar di sumbu-x.

```python
plt.plot(X, Y, label="f(x)")
plt.scatter([root], [0], label=f"akar ≈ {root:.6f}")
```

---

## 9. Kesimpulan
- Metode Regula Falsi secara efektif menemukan akar fungsi non-linier dengan iterasi sederhana.
- Memiliki kecepatan konvergensi yang lebih baik dari metode biseksi.
- Dapat digunakan untuk berbagai fungsi, cukup ganti definisi `f(x)`.

---

## 10. Catatan Tambahan
- Program tidak menggunakan pustaka eksternal selain `matplotlib` dan `numpy`.
- Program dapat dikembangkan untuk menyimpan hasil atau grafik ke file secara otomatis.
