import streamlit as st

st.set_page_config(page_title="QuCreate Streamlit Lab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Navigation Sidebar for Multipage App
page = st.sidebar.selectbox("Select Page", ["Bond Pricing", "Yield Curve Analysis", "Explanation"])

if page == "Bond Pricing":
    from pages import bond_pricing
    bond_pricing.app()
elif page == "Yield Curve Analysis":
    from pages import yield_curve
    yield_curve.app()
elif page == "Explanation":
    from pages import explanation
    explanation.app()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
