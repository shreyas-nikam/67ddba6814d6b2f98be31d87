id: 67ddba6814d6b2f98be31d87_user_guide
summary: Bond Pricing & Yield Curve Analysis User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuCreate Streamlit Lab User Guide

This codelab will guide you through the QuCreate Streamlit Lab application, a tool designed to illustrate fundamental concepts in bond pricing and yield curve visualization. Understanding these concepts is crucial for anyone involved in finance, investment, or risk management. This application provides an interactive and intuitive way to explore how different factors influence bond prices and how yield curves are constructed and interpreted. Through hands-on exploration with the application's features, you will gain a deeper understanding of these essential financial principles.

## Exploring the Bond Pricing Calculator
Duration: 00:05

The Bond Pricing Calculator is a core feature of this application. It allows you to calculate the theoretical price of a bond based on key inputs such as coupon rate, maturity, face value, and yield to maturity (YTM). This is a fundamental tool for understanding how bond prices are determined in the market.

## Using the Bond Pricing Calculator
Duration: 00:10

1.  **Navigate to the "Bond Pricing Calculator"**: Use the navigation sidebar on the left to select "Bond Pricing Calculator."
2.  **Input Bond Parameters**: You will see input fields for:
    *   **Coupon Rate**: Enter the bond's coupon rate as a decimal (e.g., 0.05 for 5%).
    *   **Maturity**: Enter the number of years until the bond matures.
    *   **Face Value**: Enter the face value (par value) of the bond. This is the amount the bondholder will receive at maturity.
    *   **Yield to Maturity (YTM)**: Enter the YTM as a decimal (e.g., 0.04 for 4%). YTM represents the total return an investor can expect if they hold the bond until maturity.
3.  **Calculate the Price**: Click the "Calculate Price" button. The application will then display the calculated bond price.

<aside class="positive">
<b>Tip:</b> Experiment with different values for coupon rate, maturity, and YTM to see how they affect the bond price. Notice how the bond price moves inversely with YTM.
</aside>

## Understanding the Bond Pricing Formula
Duration: 00:10

The application uses the following formula to calculate the bond price:

Price = (Coupon Payment) * (1 - (1+YTM)^(-Maturity)) / YTM + Face Value / (1+YTM)^(Maturity)

where:

*   **Coupon Payment** = Coupon Rate * Face Value
*   **Maturity** is the number of years until maturity.
*   **YTM** is the Yield to Maturity or discount rate.

The formula essentially discounts all future cash flows (coupon payments and face value) back to their present value using the YTM as the discount rate.

## Exploring the Yield Curve Visualization
Duration: 00:05

The Yield Curve Visualization tool helps you understand the relationship between bond prices and YTM. By visualizing how the price of a bond changes as the YTM varies, you can gain insights into interest rate risk and bond valuation.

## Using the Yield Curve Visualization
Duration: 00:15

1.  **Navigate to "Yield Curve Visualization"**: Use the navigation sidebar to select "Yield Curve Visualization."
2.  **Input Bond Parameters**: Similar to the Bond Pricing Calculator, you'll need to input:
    *   **Coupon Rate**
    *   **Maturity**
    *   **Face Value**
    *   **Starting YTM**: This is the lowest YTM value that will be displayed on the chart.
    *   **Ending YTM**: This is the highest YTM value that will be displayed on the chart.
    *   **Number of Points**: This determines the granularity of the yield curve. A higher number of points will result in a smoother curve.
3.  **Observe the Interactive Chart**: The application will generate a Plotly chart showing the bond price on the Y-axis and the YTM on the X-axis.

<aside class="positive">
<b>Tip:</b> Hover over the chart to see the exact YTM and corresponding bond price at any point on the curve. Adjust the YTM range and the number of points to explore the relationship in more detail.
</aside>

<aside class="negative">
<b>Warning:</b> Ensure that the Starting YTM is less than the Ending YTM. Otherwise, the application will display an error.
</aside>

## Interpreting the Yield Curve
Duration: 00:10

The Yield Curve Visualization demonstrates the inverse relationship between bond prices and YTM. As the YTM increases, the bond price decreases, and vice versa. The steepness of the curve reflects the sensitivity of the bond price to changes in interest rates. A steeper curve indicates higher sensitivity.

## Exploring the Documentation
Duration: 00:05

The Documentation page provides a summary of the application's features, the bond pricing formula, and instructions on how to use the tool. It's a helpful resource for understanding the underlying concepts and the application's functionality.

## Using the Documentation
Duration: 00:05

1.  **Navigate to "Documentation"**: Use the navigation sidebar to select "Documentation".
2.  **Review the Information**: Read through the provided information to reinforce your understanding of the bond pricing formula, the application's features, and how to use the tool effectively.
