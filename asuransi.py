import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Membaca data dari file CSV
    file_path = "insurance.csv"  # Ganti dengan path file CSV Anda
    df = pd.read_csv(file_path)

    # Menampilkan daftar kolom yang tersedia
    print("Kolom yang tersedia:")
    print(df.columns)

    # Meminta pengguna untuk memilih kolom yang akan dianalisis
    selected_column = input("Masukkan nama kolom yang akan dianalisis: ")

    # Melakukan analisis statistik untuk kolom yang dipilih
    selected_data = df[selected_column]
    mean_value = selected_data.mean()
    median_value = selected_data.median()
    std_value = selected_data.std()

    print("Hasil analisis statistik:")
    print(f"Rata-rata: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standar Deviasi: {std_value}")

    # Membuat visualisasi data dengan histogram
    plt.figure(figsize=(8, 6))
    plt.hist(selected_data, bins=10, edgecolor='black', alpha=0.7)
    plt.xlabel(selected_column)
    plt.ylabel("Frekuensi")
    plt.title(f"Histogram dari Kolom '{selected_column}'")
    plt.grid(True)
    plt.show()

    # Membuat visualisasi data dengan plot pencar
    plt.figure(figsize=(8, 6))
    plt.scatter(df.index, selected_data, alpha=0.5)
    plt.xlabel("Indeks Data")
    plt.ylabel(selected_column)
    plt.title(f"Plot Pencar dari Kolom '{selected_column}'")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
