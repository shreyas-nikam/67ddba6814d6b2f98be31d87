id: 67ddba6814d6b2f98be31d87_documentation
summary: Bond Pricing & Yield Curve Analysis Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Streamlit Bond Pricing and Yield Curve Analysis Codelab

This codelab will guide you through the functionalities of a Streamlit application designed for bond pricing and yield curve analysis. This application serves as an educational tool to understand the relationship between bond parameters and their price.  We will explore the key concepts of bond pricing and yield curve construction through interactive examples.

## Understanding the Application's Purpose
Duration: 00:05

This application is designed to illustrate the fundamental concepts of bond pricing and how yield curves are constructed and interpreted. By the end of this codelab, you will understand:

*   The basic formula for bond pricing.
*   How different bond parameters (coupon rate, maturity, YTM) affect the bond price.
*   How to visualize the relationship between bond price and yield to maturity through a yield curve.
*   The structure of a multi-page Streamlit application.

## Setting up the Environment
Duration: 00:02

Before diving into the application, ensure you have the necessary Python packages installed. Open your terminal and run:

```console
pip install streamlit numpy plotly
```

This command installs Streamlit for creating the user interface, NumPy for numerical computations, and Plotly for interactive visualizations.

## Exploring the `app.py` - Main Application Entry Point
Duration: 00:05

The `app.py` file serves as the main entry point for the Streamlit application. Let's break down its functionality:

```python
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
```

Key components:

*   **`import streamlit as st`**: Imports the Streamlit library, aliased as `st` for easy use.
*   **`st.set_page_config(...)`**: Configures the page title and layout.
*   **`st.sidebar.image(...)`**: Displays an image in the sidebar (in this case, the QuantUniversity logo).
*   **`st.sidebar.selectbox(...)`**: Creates a dropdown menu in the sidebar allowing users to navigate between different pages of the application.
*   **Conditional Page Loading**:  Based on the selected page in the sidebar, the corresponding module from the `pages` directory is imported and its `app()` function is executed.
*   **Copyright and Caption**:  Displays copyright information and a disclaimer at the bottom of the application.

## Understanding the `pages` Directory
Duration: 00:05

The `pages` directory contains the code for each individual page of the application. Each Python file within this directory represents a separate page accessible through the navigation sidebar in `app.py`.

### `pages/bond_pricing.py`: Bond Pricing Calculator

This page implements a bond pricing calculator.  Let's explore the code:

```python
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
```

*   **`calculate_bond_price(coupon_rate, maturity, face_value, ytm)`**: This function implements the bond pricing formula. It takes the coupon rate, maturity, face value, and yield to maturity as inputs and returns the calculated bond price.
*   **`app()`**:  This function contains the Streamlit code for the bond pricing calculator page. It includes:
    *   A header and description of the page using `st.header()` and `st.markdown()`.
    *   `st.number_input()` widgets for users to input the bond parameters (coupon rate, maturity, face value, and YTM).
    *   A `st.button()` that, when clicked, calls the `calculate_bond_price()` function with the user-provided inputs and displays the result using `st.success()`.

### `pages/yield_curve.py`: Yield Curve Analysis

This page generates an interactive yield curve, visualizing the relationship between bond price and yield to maturity.

```python
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
```

*   **`calculate_bond_price(coupon_rate, maturity, face_value, ytm)`**: This function is identical to the one in `bond_pricing.py`.
*   **`app()`**:
    *   Takes coupon rate, maturity, and face value inputs via `st.sidebar.number_input()`. Placing the input widgets in `st.sidebar` makes them persistent across interactions.
    *   Takes minimum and maximum YTM values as input to define the range for the yield curve.
    *   Generates a sequence of YTM values using `np.linspace()`.
    *   Calculates the bond price for each YTM value in the sequence.
    *   Creates an interactive line chart using `plotly.express` to visualize the relationship between YTM and bond price.
    *   Displays the chart using `st.plotly_chart()`.

### `pages/explanation.py`: Explanation and Documentation

This page provides a description of the application, the bond pricing formula, and instructions for using the application.

```python
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
```

This page primarily uses `st.markdown()` to display text, headings, and lists, providing a comprehensive explanation of the application's purpose and functionality.

## Running the Application
Duration: 00:02

To run the application, navigate to the directory containing `app.py` in your terminal and execute the following command:

```console
streamlit run app.py
```

This command will start the Streamlit server and open the application in your web browser.

## Interacting with the Application
Duration: 00:10

1.  **Bond Pricing Page**: Select "Bond Pricing" from the sidebar. Experiment with different values for the coupon rate, maturity, face value, and YTM. Click the "Calculate Bond Price" button to see the calculated price. Observe how changes in each parameter affect the bond price.  For example, increasing the YTM generally decreases the bond price, and vice versa.

2.  **Yield Curve Analysis Page**: Select "Yield Curve Analysis" from the sidebar. Adjust the coupon rate, maturity, face value, minimum YTM, and maximum YTM. Observe how the yield curve changes in response to these adjustments.  Notice how the shape of the yield curve reflects the relationship between YTM and bond price. Generally, as YTM increases, the bond price decreases, resulting in a downward-sloping curve.

3.  **Explanation Page**:  Select "Explanation" from the sidebar. Review the documentation to reinforce your understanding of the bond pricing formula and the application's functionality.

## Testing the Application
Duration: 00:05

The `tests` directory contains unit and integration tests to ensure the application functions correctly.

### `tests/test_bond_pricing.py`: Unit Tests

This file contains a unit test for the `calculate_bond_price` function.

```python
import unittest
from pages.bond_pricing import calculate_bond_price

class TestBondPricing(unittest.TestCase):
    def test_bond_price(self):
        # With coupon_rate=0.05, maturity=10, face_value=1000, ytm=0.05, the bond price should be near par.
        price = calculate_bond_price(0.05, 10, 1000, 0.05)
        # Expected value is approximately 1000 (allowing for numerical tolerance)
        self.assertAlmostEqual(price, 1000, delta=50)

if __name__ == '__main__':
    unittest.main()
```

This test asserts that when the coupon rate equals the YTM, the bond price should be close to the face value.

### `tests/integration/test_app.py`: Integration Tests

This file contains an integration test to ensure that the `app()` functions exist in each page module.

```python
import unittest
from pages import bond_pricing, yield_curve, explanation

class TestIntegration(unittest.TestCase):
    def test_pages_exist(self):
        self.assertTrue(hasattr(bond_pricing, 'app'))
        self.assertTrue(hasattr(yield_curve, 'app'))
        self.assertTrue(hasattr(explanation, 'app'))

if __name__ == '__main__':
    unittest.main()
```

To run the tests, navigate to the `tests` directory in your terminal and execute:

```console
python -m unittest discover
```

## Extending the Application
Duration: 00:15

Here are some ideas for extending the application:

*   **Add More Sophisticated Bond Pricing Models:** Implement models that account for embedded options (e.g., callable bonds) or different yield curve shapes.
*   **Implement Different Yield Curve Construction Methods:**  Explore methods like bootstrapping or the Nelson-Siegel model.
*   **Incorporate Real-World Data:** Fetch bond data from a reliable source and use it to drive the visualizations.
*   **Add Scenario Analysis:** Allow users to define different economic scenarios and see how bond prices and yield curves change under those scenarios.
*   **Add a data table:** Display the bond price calculation in a tabular format.

## Conclusion
Duration: 00:03

You have successfully completed this codelab and gained a better understanding of how to build a Streamlit application for bond pricing and yield curve analysis. This application provides a foundation for further exploration of fixed-income concepts and development of more sophisticated financial tools.
