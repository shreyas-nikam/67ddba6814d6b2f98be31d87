import streamlit as st

def calculate_bond_price(coupon_rate, maturity, face_value, ytm):
    """
    Calculate the bond price using the formula:
    Price = Sum (Coupon Payment / (1+YTM)^t) + (Face Value / (1+YTM)^n)
    where Coupon Payment = coupon_rate * face_value.
    """
    coupon = coupon_rate * face_value
    price = 0
    for t in range(1, int(maturity)+1):
        price += coupon / ((1 + ytm) ** t)
    price += face_value / ((1 + ytm) ** maturity)
    return price

def app():
    st.header("Bond Pricing Calculator")
    st.markdown("""
    This page allows you to calculate the price of a bond based on user-defined parameters:
    
    - **Coupon Rate**: Annual coupon rate (as a decimal, e.g., 0.05 for 5%)
    - **Maturity**: Time to maturity in years.
    - **Face Value**: The nominal value of the bond.
    - **Yield to Maturity (YTM)**: The annual yield required by the market (as a decimal).
    
    The bond price is calculated using the formula:
    
    Price = Sum (Coupon Payment / (1+YTM)^t) + (Face Value / (1+YTM)^n)
    (where Coupon Payment = Coupon Rate * Face Value)
    """)
    
    coupon_rate = st.number_input("Coupon Rate", min_value=0.0, value=0.05, step=0.01)
    maturity = st.number_input("Maturity (years)", min_value=1, value=10)
    face_value = st.number_input("Face Value", min_value=100, value=1000)
    ytm = st.number_input("Yield to Maturity (YTM)", min_value=0.0, value=0.05, step=0.01)
    
    if st.button("Calculate Bond Price"):
        price = calculate_bond_price(coupon_rate, int(maturity), face_value, ytm)
        st.success(f"The calculated bond price is: {price:.2f}")
