import streamlit as st
import pandas as pd

def main():
    st.title('Alternatif Investasi')

    # Membuat DataFrame kosong untuk menyimpan data alternatif
    data = pd.DataFrame(columns=['Alternatif', 'Investasi Awal', 'Biaya per Tahun', 'Gradien', 'Nilai Sisa'])

    # Meminta jumlah alternatif yang akan dimasukkan
    jumlah_alternatif = st.number_input('Jumlah Alternatif', min_value=1, step=1)

    # Memasukkan data alternatif
    for i in range(jumlah_alternatif):
        alternatif = st.text_input(f'Alternatif {i+1}')
        investasi_awal = st.number_input(f'Investasi Awal {i+1}', value=0)
        biaya_per_tahun = st.number_input(f'Biaya per Tahun {i+1}', value=0)
        gradien = st.number_input(f'Gradien {i+1}', value=0)
        nilai_sisa = st.number_input(f'Nilai Sisa {i+1}', value=0)
        data.loc[i] = [alternatif, investasi_awal, biaya_per_tahun, gradien, nilai_sisa]

    # Menampilkan data alternatif di tabel
    st.subheader('Data Alternatif')
    st.write(data)

    # Memilih alternatif
    selected_alternatif = st.selectbox('Pilih Alternatif', data['Alternatif'])

    # Menghitung tingkat pengembalian (rate of return)
    roi = (data[data['Alternatif'] == selected_alternatif]['Gradien'] - data[data['Alternatif'] == selected_alternatif]['Biaya per Tahun']) / data[data['Alternatif'] == selected_alternatif]['Investasi Awal'] * 100

    # Menampilkan tingkat pengembalian (rate of return)
    st.subheader('Tingkat Pengembalian (Rate of Return)')
    st.write(f"Tingkat Pengembalian {selected_alternatif}: {roi.values[0]:.2f}%")

if __name__ == '__main__':
    main()
