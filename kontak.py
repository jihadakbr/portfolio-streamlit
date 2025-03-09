import streamlit as st

def munculkan_kontak():
    st.title("Kontak")
    st.write("Hubungi saya melalui tautan berikut:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/willyrizkiyan)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/willyrizkiyan)"
    )

    # Email
    st.write("📧 Email: your.email@example.com")