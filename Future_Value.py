import streamlit as st

def calculate_single_payment(principal, interest_rate, duration):
    payment = principal * (1 + interest_rate/100)**duration
    return payment

def calculate_compound_payment(principal, interest_rate, duration):
    payment = principal * ((1 + interest_rate/100)**duration - 1) / (interest_rate/100)
    return payment

def main():
    st.title("Kalkulator Pembayaran")

    principal = st.number_input("Pinjaman Awal")
    interest_rate = st.number_input("Suku Bunga (%)")
    duration = st.number_input("Jangka Waktu (dalam tahun)")

    if st.button("Hitung"):
        single_payment = calculate_single_payment(principal, interest_rate, duration)
        compound_payment = calculate_compound_payment(principal, interest_rate, duration)

        st.write(f"Pembayaran Tunggal: {single_payment:.2f}")
        st.write(f"Pembayaran Majemuk: {compound_payment:.2f}")

if __name__ == "__main__":
    main()
