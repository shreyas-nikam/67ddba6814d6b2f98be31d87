id: 67ddba6814d6b2f98be31d87_documentation
summary: Bond Pricing & Yield Curve Analysis Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuCreate Streamlit Lab: Bond Pricing and Yield Curve Analysis

This codelab guides you through a Streamlit application designed for bond pricing and yield curve visualization. This application provides a practical and interactive platform to understand key concepts in fixed-income securities.

**Why is this important?**

Bond pricing and yield curve analysis are fundamental concepts in finance. Understanding how bond prices are determined and how yield curves are constructed and interpreted is crucial for anyone involved in investment management, portfolio analysis, or risk management. This application allows you to explore these concepts interactively, making learning more engaging and effective.

**What you'll learn:**

*   Bond pricing mechanics
*   The relationship between yield to maturity (YTM) and bond prices
*   How to visualize yield curves
*   Basic Streamlit application development

Let's dive in!

## Setting up the Environment

Duration: 00:05

Before you begin, ensure you have Python installed. It is recommended to use a virtual environment to manage dependencies.

1.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

2.  **Activate the virtual environment:**

    *   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    *   On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3.  **Install the required packages:**

    ```bash
    pip install streamlit numpy pandas plotly
    ```

## Understanding the Application Structure

Duration: 00:10

The application is structured as a multi-page Streamlit app, with the following key files:

*   `app.py`: The main entry point of the application. It handles navigation between different pages.
*   `pages/bond_pricing.py`: Contains the bond pricing calculator.
*   `pages/visualization.py`: Contains the yield curve visualization tool.
*   `pages/documentation.py`: Provides documentation about the application and the underlying concepts.
*   `tests/test_bond_pricing.py`: Contains unit tests for the bond pricing logic.
*   `tests/test_integration.py`: Contains integration tests to ensure the pages are working correctly.
*   `.github/workflows/build_docker_and_push.yml`: A GitHub Actions workflow for building and pushing a Docker image.
*   `.streamlit/config.toml`: Configuration file for Streamlit, sets port and base URL.

The `app.py` file serves as the central hub, utilizing `streamlit.selectbox` in the sidebar to navigate between the "Bond Pricing Calculator", "Yield Curve Visualization", and "Documentation" pages. Each selection renders the corresponding page content, effectively creating a multi-page application.

## Exploring the Bond Pricing Calculator

Duration: 00:15

The `bond_pricing.py` file implements a bond pricing calculator.

1.  **Examine the code:**

    ```python
    import streamlit as st
    import numpy as np

    def calculate_bond_price(coupon_rate, maturity, face_value, ytm):
        """
        Calculate the price of a bond based on the input parameters.
        Coupon Payment = coupon_rate * face_value
        Price = (Coupon Payment) * (1 - (1+ytm)^(-maturity)) / ytm + face_value / (1+ytm)^(maturity)
        """
        coupon_payment = coupon_rate * face_value
        # Handle zero yield to maturity
        if ytm == 0:
            price = coupon_payment * maturity + face_value
        else:
            price = coupon_payment * (1 - (1+ytm)**(-maturity)) / ytm + face_value * (1+ytm)**(-maturity)
        return price

    def app():
        st.header("Bond Pricing Calculator")
        st.markdown("Enter the bond parameters below to calculate its price:")
        coupon_rate = st.number_input("Coupon Rate (e.g., 0.05 for 5%)", min_value=0.0, value=0.05, step=0.01, format="%.2f")
        maturity = st.number_input("Maturity (years)", min_value=1, value=10, step=1)
        face_value = st.number_input("Face Value", min_value=1, value=1000, step=1)
        ytm = st.number_input("Yield to Maturity (YTM) (e.g., 0.04 for 4%)", min_value=0.0, value=0.04, step=0.01, format="%.2f")

        if st.button("Calculate Price"):
            price = calculate_bond_price(coupon_rate, maturity, face_value, ytm)
            st.success(f"Calculated Bond Price: ${price:,.2f}")

        st.markdown("""
        ### Explanation of the Bond Pricing Formula
        The bond price is computed using the formula:

        Price = (Coupon Payment) * (1 - (1+YTM)^(-Maturity))/YTM + Face Value / (1+YTM)^(Maturity)

        where:
        - **Coupon Payment** = Coupon Rate * Face Value
        - **Maturity** is the number of years until maturity.
        - **YTM** is the Yield to Maturity or discount rate.
        """)
    ```

2.  **Key components:**

    *   `calculate_bond_price(coupon_rate, maturity, face_value, ytm)`: This function calculates the bond price based on the provided inputs.  It implements the standard bond pricing formula. It also handles the edge case where the YTM is zero to avoid division by zero errors.
    *   `st.number_input()`:  Streamlit widgets that allow users to input the coupon rate, maturity, face value, and yield to maturity.  The `format="%.2f"` argument ensures that the input is formatted to two decimal places.
    *   `st.button()`: A button that triggers the bond price calculation when clicked.
    *   `st.success()`: Displays the calculated bond price in a success message.
    *   `st.markdown()`:  Used to display text, including the bond pricing formula and explanations.

3.  **Try it out:**

    Run the application using:

    ```bash
    streamlit run app.py
    ```

    Navigate to the "Bond Pricing Calculator" page and experiment with different input values. Observe how the bond price changes as you modify the coupon rate, maturity, face value, and YTM.

## Visualizing the Yield Curve

Duration: 00:20

The `visualization.py` file implements a yield curve visualization tool.

1.  **Examine the code:**

    ```python
    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.express as px

    def calculate_bond_price(coupon_rate, maturity, face_value, ytm):
        coupon_payment = coupon_rate * face_value
        if ytm == 0:
            price = coupon_payment * maturity + face_value
        else:
            price = coupon_payment * (1 - (1+ytm)**(-maturity)) / ytm + face_value * (1+ytm)**(-maturity)
        return price

    def app():
        st.header("Yield Curve Visualization")
        st.markdown("This page allows you to visualize the bond price variations as YTM changes.")

        coupon_rate = st.number_input("Coupon Rate (e.g., 0.05 for 5%)", min_value=0.0, value=0.05, step=0.01, format="%.2f")
        maturity = st.number_input("Maturity (years)", min_value=1, value=10, step=1)
        face_value = st.number_input("Face Value", min_value=1, value=1000, step=1)
        ytm_start = st.number_input("Starting YTM", min_value=0.0, value=0.01, step=0.01, format="%.2f")
        ytm_end = st.number_input("Ending YTM", min_value=0.0, value=0.10, step=0.01, format="%.2f")
        num_points = st.slider("Number of Points", min_value=10, max_value=200, value=50)

        if ytm_start >= ytm_end:
            st.error("Starting YTM must be less than Ending YTM.")
            return

        ytm_values = np.linspace(ytm_start, ytm_end, num_points)
        prices = [calculate_bond_price(coupon_rate, maturity, face_value, ytm) for ytm in ytm_values]

        df = pd.DataFrame({
            "YTM": ytm_values,
            "Bond Price": prices
        })

        fig = px.line(df, x="YTM", y="Bond Price", title="Bond Price vs Yield to Maturity",
                      labels={"YTM": "Yield to Maturity", "Bond Price": "Bond Price"})
        fig.update_traces(mode='lines+markers', hovertemplate="YTM: %{x:.2f}<br>Bond Price: $%{y:.2f}")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        ### Interactive Chart Details
        The above chart updates dynamically as you adjust the input parameters. Hover over any point to view detailed information.
        """)
    ```

2.  **Key components:**

    *   It reuses the `calculate_bond_price` function from `bond_pricing.py`.
    *   It uses `np.linspace` to create an array of YTM values between the specified start and end points.
    *   It creates a Pandas DataFrame to store the YTM values and corresponding bond prices.
    *   `plotly.express` is used to create an interactive line chart of bond price versus YTM.
    *   The `hovertemplate` argument in `fig.update_traces` customizes the hover information displayed on the chart.
    *   `st.plotly_chart()` displays the Plotly chart in the Streamlit application.

3.  **Try it out:**

    Navigate to the "Yield Curve Visualization" page in the running application. Adjust the input parameters, such as the coupon rate, maturity, YTM range, and number of points. Observe how the yield curve changes dynamically as you modify these parameters. Hover over the chart to see the specific YTM and bond price at each point.

    <aside class="positive">
    This visualization is crucial for understanding the inverse relationship between bond prices and yields. As yields increase, bond prices decrease, and vice versa.
    </aside>

## Exploring the Documentation

Duration: 00:05

The `documentation.py` file provides documentation for the application.

1.  **Examine the code:**

    ```python
    import streamlit as st

    def app():
        st.header("Documentation")
        st.markdown("""
        ## Bond Pricing Visualizer Documentation

        This multi-page Streamlit application is designed for educational purposes to illustrate bond pricing and yield curve analysis.

        ### Features
        - **Bond Pricing Calculator**: Compute the price of a bond using user-defined parameters.
        - **Yield Curve Visualization**: Interactive Plotly chart showcasing how bond prices change with varying YTM values.
        - **Documentation**: Detailed explanations of the formulas, methodology, and interactive visualizations.

        ### Bond Pricing Formula
        The bond price is calculated using the formula:

        Price = (Coupon Payment) * (1 - (1 + YTM)^(-Maturity)) / YTM + Face Value / (1 + YTM)^(Maturity)

        where:
        - **Coupon Payment** = Coupon Rate * Face Value
        - **Maturity** is the number of years until maturity.
        - **YTM** is the yield to maturity.

        ### How to Use
        1. Navigate using the sidebar.
        2. Input the required parameters.
        3. View the calculated bond price or interactive visualization.

        Enjoy exploring the fundamentals of bond pricing!
        """)
    ```

2.  **Key components:**

    *   `st.markdown()`:  Used to display the documentation content, including headings, lists, and explanations.

3.  **Navigate to Documentation:**

    Navigate to the "Documentation" page to see the information about the application.

## Running Tests

Duration: 00:10

The application includes unit tests and integration tests to ensure the code is working correctly.

1.  **Run the unit tests:**

    ```bash
    python -m unittest tests/test_bond_pricing.py
    ```

    This will run the unit tests in `tests/test_bond_pricing.py`, which verify the `calculate_bond_price` function.

2.  **Run the integration tests:**

    ```bash
    python -m unittest tests/test_integration.py
    ```

    This will run the integration tests in `tests/test_integration.py`, which verify that the Streamlit pages are loading without errors.

    <aside class="positive">
    Writing tests is crucial for ensuring the reliability and correctness of your code. Unit tests verify individual functions, while integration tests verify the interaction between different parts of the application.
    </aside>

## Dockerization

Duration: 00:10

The `.github/workflows/build_docker_and_push.yml` file contains a GitHub Actions workflow that automatically builds and pushes a Docker image of the application to Docker Hub when a new tag is pushed to the repository.

1.  **Examine the workflow file:**

    ```yaml
    name: Build and Push to Docker Hub

    on:
      push:
        tags:
          - "v*.*.*"

    jobs:
      build-and-push:
        runs-on: ubuntu-latest

        steps:
          - name: Check out repository
            uses: actions/checkout@v2

          - name: Log in to Docker Hub
            run: |
              echo "${{ secrets.DOCKERHUB_PASSWORD }}" | docker login -u "${{ secrets.DOCKERHUB_USERNAME }}" --password-stdin

          - name: Build Docker image
            run: |
              docker build -t None/67ddba6814d6b2f98be31d87_streamlit_app:latest .

          - name: Push Docker image
            run: |
              docker push None/67ddba6814d6b2f98be31d87_streamlit_app:latest
    ```

2.  **Key components:**

    *   `on`:  Specifies when the workflow should run. In this case, it runs when a tag matching the pattern `v*.*.*` is pushed to the repository.
    *   `jobs`:  Defines the jobs that will be executed by the workflow. In this case, there is a single job called `build-and-push`.
    *   `steps`:  Defines the steps that will be executed by the job. These steps include checking out the repository, logging in to Docker Hub, building the Docker image, and pushing the Docker image to Docker Hub.
    *   `secrets`:  The workflow uses secrets to store the Docker Hub username and password. These secrets are stored in GitHub and are not exposed in the workflow file.

3.  **Run Locally:**

    To run the docker image locally, you first need to build it:

    ```bash
    docker build -t streamlit_app:latest .
    ```

    Then run the image:

    ```bash
    docker run -p 8504:8504 streamlit_app:latest
    ```

    <aside class="negative">
    Ensure you replace `None/67ddba6814d6b2f98be31d87_streamlit_app` with your own Docker Hub username and repository name. Also, you'll need to set up the `DOCKERHUB_USERNAME` and `DOCKERHUB_PASSWORD` secrets in your GitHub repository settings.
    </aside>

## Streamlit Configuration

Duration: 00:05

The `.streamlit/config.toml` file configures the Streamlit server.

1.  **Examine the configuration file:**

    ```toml
    [server]
    port = 8504
    baseUrlPath = "67ddba6814d6b2f98be31d87"
    enableCORS = false
    enableXsrfProtection = false
    ```

2.  **Key settings:**

    *   `port`:  Specifies the port on which the Streamlit server will listen.
    *   `baseUrlPath`:  Specifies the base URL path for the Streamlit application. This is useful when deploying the application behind a reverse proxy.
    *   `enableCORS`:  Disables Cross-Origin Resource Sharing (CORS).  In a production environment, you may need to configure CORS to allow access from specific domains.
    *   `enableXsrfProtection`:  Disables Cross-Site Request Forgery (XSRF) protection.  In a production environment, you should enable XSRF protection to prevent malicious attacks.

## Conclusion

Duration: 00:05

Congratulations! You've successfully explored the QuCreate Streamlit Lab application for bond pricing and yield curve analysis. You've learned about the application structure, key functionalities, testing, and deployment. This application provides a valuable tool for understanding and visualizing important concepts in fixed-income securities.

Further exploration:

*   Enhance the application with more advanced bond pricing models.
*   Add support for different yield curve interpolation methods.
*   Implement a user authentication system.
*   Deploy the application to a cloud platform such as Heroku or AWS.
