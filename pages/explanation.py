import streamlit as st

def app():
    st.header("Explanation and Documentation")
    st.markdown("""
    # Bond Pricing & Yield Curve Analysis

    This application is designed to help you understand the principles of bond pricing and how changes in yield to maturity (YTM)
    can affect the price of a bond. Below are some important sections:

    ## Bond Pricing Formula
    The bond price is calculated using the following formula:
    
       Price = Sum (Coupon Payment / (1+YTM)^t) + (Face Value / (1+YTM)^n)
    
    where:
    - Coupon Payment = Coupon Rate × Face Value
    - t: time period (from 1 to n)
    - n: total number of periods (maturity)

    ## Visualizations
    The application provides interactive visualizations that allow you to see real-time changes in the bond price
    as you adjust parameters such as Coupon Rate, Maturity, Face Value, and Yield to Maturity (YTM). The charts are built using Plotly,
    enabling high interactivity with tooltips and dynamic updates.

    ## Dataset
    A synthetic dataset is used to model various bond pricing scenarios. This dataset is purely for educational purposes and demonstrates
    how bond pricing theories can be applied.

    ## User Instructions
    - Navigate between different pages using the sidebar.
    - On the "Bond Pricing" page, input your bond parameters and calculate the bond price.
    - On the "Yield Curve Analysis" page, explore how varying YTM affects the bond price.
    """)
