import streamlit as st
import pandas as pd

# Sayfa Ayarları (Mobil Uyumlu)
st.set_page_config(page_title="BOSS CUTTING Takım Kütüphanesi", layout="centered")

st.title("🛠️ Takım Kontrol Merkezi")

# --- YAN PANEL: YÖNETİM ---
with st.sidebar:
    st.header("Yönetim Paneli")
    islem = st.radio("İşlem Seçin:", ["Takım Ara/Görüntüle", "Yeni Takım Ekle", "Stok Güncelle"])

# Örnek Veri Seti (İleride Veritabanına Bağlanacak)
if 'takimlar' not in st.session_state:
    st.session_state.takimlar = pd.DataFrame([
        {"Kod": "BST-001", "Tip": "Karbür Freze", "Ölçü": "Ø12", "Konum": "A-01", "Resim": "https://via.placeholder.com/150"},
        {"Kod": "BST-002", "Tip": "Kademeli Matkap", "Ölçü": "Ø8.5", "Konum": "B-03", "Resim": "https://via.placeholder.com/150"}
    ])

# --- ANA EKRAN: ARAMA VE GÖRÜNTÜLEME ---
if islem == "Takım Ara/Görüntüle":
    search = st.text_input("Takım adı veya kodu yazın...", placeholder="Örn: BST-001")
    
    # Filtreleme
    df = st.session_state.takimlar
    if search:
        df = df[df['Kod'].str.contains(search) | df['Tip'].str.contains(search)]

    for index, row in df.iterrows():
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(row['Resim'], width=100)
            with col2:
                st.subheader(f"Kod: {row['Kod']}")
                st.write(f"**Tip:** {row['Tip']} | **Ölçü:** {row['Ölçü']}")
                st.write(f"📍 **Konum:** {row['Konum']}")
                if st.button(f"Teknik Resmi Gör ({row['Kod']})"):
                    st.info("Teknik resim (PDF) açılıyor...")
            st.divider()

# --- ANA EKRAN: YENİ VERİ GİRİŞİ ---
elif islem == "Yeni Takım Ekle":
    st.subheader("Yeni Takım Kaydı")
    yeni_kod = st.text_input("Takım Kodu")
    yeni_tip = st.selectbox("Tip", ["Karbür Freze", "Matkap", "Rayba", "Özel Takım"])
    yuklenen_dosya = st.file_uploader("Teknik Resim veya Fotoğraf Yükle", type=['png', 'jpg', 'pdf'])
    
    if st.button("Sisteme Kaydet"):
        st.success(f"{yeni_kod} başarıyla veritabanına eklendi!")