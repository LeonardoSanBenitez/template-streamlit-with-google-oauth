import streamlit as st
import security
import sys


def main(**kwargs):
    st.markdown(f"Hello {kwargs['user_email']}")


security.login(callback=main)

# Show output on console
sys.stdout.flush()

# Hide the menu button
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
