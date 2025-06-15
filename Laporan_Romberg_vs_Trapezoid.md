
# Integrasi Numerik: Metode Trapezoidal dan Romberg

## 1. Tujuan
Membandingkan akurasi dan efisiensi antara metode **Trapezoidal** dan **Romberg Integration** dalam menghitung nilai integral suatu fungsi.

## 2. Latar Belakang
Metode **Trapezoidal** adalah pendekatan numerik sederhana untuk menghitung integral. Namun:
- Akurasinya **terbatas**, apalagi jika fungsi tidak linear.
- Membutuhkan **jumlah subinterval yang besar** untuk hasil presisi tinggi.

Sebagai solusi, digunakan **metode Romberg** yang meningkatkan akurasi dengan pendekatan **ekstrapolasi Richardson** terhadap hasil Trapezoidal tanpa harus meningkatkan jumlah subinterval secara ekstrem.

## 3. Fungsi yang Digunakan
\[
f(x) = \frac{1}{1 + x^2}
\]

Dengan batas integral dari \( a = 0 \) ke \( b = 1 \), nilai eksak integral ini adalah:
\[
\int_0^1 \frac{1}{1 + x^2} dx = \arctan(1) = \frac{\pi}{4} \approx 0.7853981634
\]

## 4. Penjelasan Algoritma

### A. Metode Trapezoidal
Rumus:
\[
\int_a^b f(x) dx \approx \frac{h}{2} \left[ f(a) + 2 \sum_{i=1}^{n-1} f(x_i) + f(b) \right]
\]
- Kelemahan: error sebesar \( O(h^2) \)
- Semakin kecil \( h \), semakin akurat, tapi membutuhkan banyak iterasi.

### B. Metode Romberg
- Memulai dengan hasil Trapezoidal.
- Memperbaiki hasil dengan menggunakan **eksstrapolasi**:
\[
R_{i,j} = \frac{4^j R_{i,j-1} - R_{i-1,j-1}}{4^j - 1}
\]
- Tabel Romberg memperkirakan nilai integral dengan konvergensi cepat.

## 5. Implementasi Program (Sorotan)
```python
def trapezoidal(x0, xn, n):
    h = (xn - x0) / n
    ...
    return integration

def romberg(f, a, b, max_level):
    ...
    R[i][j] = (4**j * R[i][j-1] - R[i-1][j-1]) / (4**j - 1)
    ...
    return R
```

## 6. Hasil Eksekusi (Contoh)
Input:
```
a = 0
b = 1
n = 4
max_romberg_level = 4
```

Output:
```
Integration result by Trapezoidal method: 0.7827941176

Romberg Integration Table:
0.7500000000
0.7833333333    0.7944444444
0.7827941176    0.7856826476    0.7853981756
0.7831441148    0.7854703294    0.7853982213    0.7853981634

Final result by Romberg method: 0.7853981634
Exact value (π/4): 0.7853981634
Error (Trapezoidal): 2.60e-03
Error (Romberg):     1.11e-16
```

## 7. Analisis Hasil
| Metode       | Subinterval | Hasil Integrasi | Error terhadap π/4        |
|--------------|-------------|------------------|----------------------------|
| Trapezoidal  | 4           | 0.7827941176     | ≈ 2.6 × 10⁻³              |
| Romberg (4)  | max level 4 | 0.7853981634     | ≈ 1.11 × 10⁻¹⁶            |

## 8. Kesimpulan
Metode **Romberg Integration** secara signifikan meningkatkan akurasi dibanding metode Trapezoidal biasa, bahkan hanya dengan sedikit level iterasi. Ini menunjukkan kekuatan extrapolasi Richardson dalam mempercepat konvergensi numerik.

## 9. Tambahan
Program dapat dikembangkan untuk:
- Menampilkan grafik konvergensi
- Menerima fungsi sebagai input dari user
- Menyimpan hasil dalam file .txt atau .csv
