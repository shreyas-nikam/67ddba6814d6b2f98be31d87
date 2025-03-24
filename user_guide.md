id: 67ddba6814d6b2f98be31d87_user_guide
summary: Bond Pricing & Yield Curve Analysis User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuCreate Streamlit Lab User Guide

This codelab provides a comprehensive guide to using the QuCreate Streamlit Lab, a powerful tool for understanding bond pricing and yield curve dynamics. This application is designed to help you grasp essential fixed-income concepts through interactive visualizations and calculations. By the end of this guide, you'll be able to use the application effectively to explore bond pricing scenarios and understand the relationship between yield and bond prices.

## Understanding the Application's Structure
Duration: 00:02

The QuCreate Streamlit Lab is structured as a multi-page application, each page focusing on a specific aspect of bond analysis:

*   **Bond Pricing Calculator:** This page allows you to calculate the price of a bond based on your input parameters like coupon rate, maturity, face value, and yield to maturity (YTM).
*   **Yield Curve Visualization:** This page presents an interactive chart visualizing the relationship between a bond's price and its YTM, enabling you to observe how price changes as the YTM varies.
*   **Documentation:** A page that explains the formulas and underlying concepts.

Use the navigation sidebar on the left to switch between these pages.

## Bond Pricing Calculator
Duration: 00:05

This section guides you through using the Bond Pricing Calculator.

1.  **Accessing the Calculator:** Select "Bond Pricing Calculator" from the navigation sidebar.
2.  **Inputting Bond Parameters:** You will see input fields for:
    *   **Coupon Rate:** The annual interest rate paid on the bond's face value (e.g., 0.05 for 5%).
    *   **Maturity (years):** The number of years until the bond matures.
    *   **Face Value:** The amount the bondholder will receive at maturity.
    *   **Yield to Maturity (YTM):** The total return anticipated on a bond if it is held until it matures.
3.  **Calculating the Price:** After entering the values, click the "Calculate Price" button.
4.  **Interpreting the Results:** The calculated bond price will be displayed.  This is the theoretical price you should be willing to pay for the bond, given the specified parameters and assuming you hold it to maturity.
5. **Understanding the Formula:** The section below the calculator displays the Bond Pricing formula and explains each of its components.

<aside class="positive">
The calculator is a great way to see how changes in YTM, coupon rate and time to maturity affect a bond's price. Experiment with different values!
</aside>

## Yield Curve Visualization
Duration: 00:07

This section explores the Yield Curve Visualization feature. This visualization allows you to see how the bond price changes when the Yield to Maturity (YTM) changes.

1.  **Accessing the Visualization:** Select "Yield Curve Visualization" from the navigation sidebar.
2.  **Setting Visualization Parameters:**
    *   You'll find the same input fields as in the Bond Pricing Calculator: "Coupon Rate," "Maturity," and "Face Value." Adjust these to reflect the bond you want to analyze.
    *   Additionally, you can set:
        *   **Starting YTM:** The minimum YTM for the X axis of the chart.
        *   **Ending YTM:** The maximum YTM for the X axis of the chart.
        *   **Number of Points:** This controls the smoothness of the curve by specifying how many data points are used to generate it. Higher values result in a smoother curve.
3.  **Analyzing the Chart:** The application generates an interactive line chart showing the relationship between "YTM" (x-axis) and "Bond Price" (y-axis).
    *   **Observe the Relationship:** Notice the inverse relationship: as the YTM increases, the bond price decreases, and vice versa.
    *   **Hover for Details:** Hover your mouse over any point on the chart to see the exact YTM and corresponding bond price.
4. **Understanding Interactivity:** The chart dynamically updates as you adjust the input parameters, allowing for real-time analysis.

<aside class="negative">
Ensure that the "Starting YTM" is less than the "Ending YTM".
</aside>

## Documentation
Duration: 00:03

1.  **Accessing Documentation:** Click on the "Documentation" navigation on the sidebar.
2.  **Reading the Documentation:** The documentation page provides detailed explanations of:
    *   The purpose of the application.
    *   The features available.
    *   The bond pricing formula and its components.
    *   Instructions on how to use the application.

This page serves as a quick reference guide to the application's functionality and underlying concepts.
