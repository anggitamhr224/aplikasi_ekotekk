import streamlit as st

def calculate_interest_rate(principal, payment, duration):
    interest_rate = ((payment - principal) / (principal * duration)) * 100
    return interest_rate

def main():
    st.title("Menghitung Besar Suku Bunga")

    principal = st.number_input("Jumlah Pinjaman")
    payment = st.number_input("Jumlah Pembayaran")
    duration = st.number_input("Jangka Waktu (dalam tahun)")

    if st.button("Hitung"):
        interest_rate = calculate_interest_rate(principal, payment, duration)
        st.write(f"Suku Bunga: {interest_rate:.2f}%")

if __name__ == "__main__":
    main()
