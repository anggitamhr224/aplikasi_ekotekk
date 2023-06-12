import streamlit as st

def calculate_present_worth_cost(investasi, biaya_operasi, gradien, nilai_sisa, suku_bunga, tahun):
    present_worth_cost = investasi

    for year in range(tahun):
        aliran_kas = biaya_operasi + gradien * tahun
        faktor = aliran_kas / ((1 + suku_bunga) ** (tahun + 1))
        present_worth_cost += faktor

    present_worth_cost -= nilai_sisa / ((1 + suku_bunga) ** tahun)
    return present_worth_cost

def main():
    st.title("Menghitung Nilai Present Worth")
    st.write("Masukkan data-data yang diperlukan:")

    # Get user input
    investasi = st.number_input("Investasi Awal:")
    biaya_operasi = st.number_input("Biaya Operasi Per Tahun:")
    gradien = st.number_input("Gradien:")
    nilai_sisa = st.number_input("Nilai Akhir:")
    suku_bunga = st.number_input("Suku Bunga (%):")
    tahun = st.number_input("Tahun:", min_value=1, step=1)

    # Calculate present worth cost for each alternative
    present_worth_cost = calculate_present_worth_cost(investasi, biaya_operasi, gradien, nilai_sisa, suku_bunga / 100, tahun)

    # Display the result
    st.write("Present Worth Cost:", present_worth_cost)

if __name__ == "__main__":
    main()
