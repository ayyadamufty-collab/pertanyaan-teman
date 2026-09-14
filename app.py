import streamlit as st
from supabase import create_client

st.set_page_config(
    page_title="Pertanyaan Untuk Teman",
    page_icon="💌"
)

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

st.title("💌 Pertanyaan Untuk Kamu")
st.write("Jawab dengan jujur yaa 🤍")

hal_suka = st.text_area("1. Hal-hal yang kamu suka")
perlakuan = st.text_area("2. Kamu mau diperlakukan seperti apa?")
kesan = st.text_area("3. Apa kesan pertama kamu tentang aku?")
kesal = st.text_area("4. Kamu pernah kesal nggak sama sifat aku?")
pesan = st.text_area("5. Kasih aku pesan")
nama = st.text_input("6. Tulis nama kamu di sini ya")

if st.button("Kirim Jawaban 💌"):
    if hal_suka and perlakuan and kesan and kesal and pesan and nama:
        data = {
            "nama": nama,
            "hal_suka": hal_suka,
            "perlakuan": perlakuan,
            "kesan": kesan,
            "kesal": kesal,
            "pesan": pesan
        }

        response = supabase.table("jawaban").insert(data).execute()

        st.success("Jawaban kamu sudah terkirim! 💕")
        st.markdown("---")
        st.title("❤️ I LOVE YOU ❤️")
        st.write(f"Makasih sudah mau jawab, {nama}! 🫶")
        st.write("Semoga kita tetap berteman baik yaa 🤍")
    else:
        st.warning("Jangan lupa isi semua pertanyaannya yaa 😄")
