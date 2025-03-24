import streamlit as st
import numpy as np
import plotly.express as px

def calculate_bond_price(coupon_rate, maturity, face_value, ytm):
    """
    Calculate the bond price with given parameters.
    """
    coupon = coupon_rate * face_value
    price = 0
    for t in range(1, int(maturity)+1):
        price += coupon / ((1 + ytm) ** t)
    price += face_value / ((1 + ytm) ** maturity)
    return price

def app():
    st.header("Yield Curve Analysis")
    st.markdown("""
    This page displays how the bond price varies with different Yield to Maturity (YTM) values.
    Adjust the parameters below to generate an interactive yield curve using Plotly.
    """)

    # Sidebar inputs specific to yield curve analysis for interactivity
    coupon_rate = st.sidebar.number_input("Coupon Rate", min_value=0.0, value=0.05, step=0.01)
    maturity = st.sidebar.number_input("Maturity (years)", min_value=1, value=10)
    face_value = st.sidebar.number_input("Face Value", min_value=100, value=1000)
    
    ytm_min = st.sidebar.number_input("Min YTM", min_value=0.0, value=0.01, step=0.01)
    ytm_max = st.sidebar.number_input("Max YTM", min_value=ytm_min+0.01, value=0.10, step=0.01)
    ytm_values = np.linspace(ytm_min, ytm_max, 100)
    
    prices = [calculate_bond_price(coupon_rate, int(maturity), face_value, ytm) for ytm in ytm_values]
    
    fig = px.line(x=ytm_values, y=prices,
                  labels={'x':'Yield to Maturity (YTM)', 'y':'Bond Price'},
                  title='Bond Price vs. Yield to Maturity')
    st.plotly_chart(fig, use_container_width=True)
