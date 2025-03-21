id: 67ddba6814d6b2f98be31d87_documentation
summary: Bond Pricing & Yield Curve Analysis Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuCreate Streamlit Lab: Bond Pricing and Yield Curve Visualization

This codelab provides a comprehensive guide to understanding and using a Streamlit application designed for bond pricing and yield curve visualization. This application is valuable for finance professionals, students, and anyone interested in learning about fixed-income securities. It provides interactive tools to calculate bond prices and visualize the relationship between yield to maturity (YTM) and bond prices. By the end of this codelab, you will understand the application's architecture, its different functionalities, and the underlying financial concepts.

## Understanding the Application's Architecture
Duration: 00:05

The application is built using Streamlit, a Python library that makes it easy to create interactive web applications. The application follows a multi-page design, with the following structure:

-   `app.py`: The main entry point of the application. It sets up the navigation and routes users to different pages.
-   `pages/`: This directory contains the code for individual pages of the application.
    -   `bond_pricing.py`: Contains the bond pricing calculator.
    -   `visualization.py`: Contains the yield curve visualization tool.
    -   `documentation.py`: Contains the documentation for the application.
-   `tests/`: This directory contains the unit and integration tests for the application.
    -   `test_bond_pricing.py`: Contains unit tests for the bond pricing calculation.
    -   `test_integration.py`: Contains integration tests for the different pages.
-   `.streamlit/config.toml`: Configuration file for the Streamlit application.
-   `.github/workflows/build_docker_and_push.yml`: GitHub Actions workflow for building and pushing the application to Docker Hub.
-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.

The application leverages the following Python libraries:

-   Streamlit: For building the user interface.
-   NumPy: For numerical computations.
-   Pandas: For data manipulation.
-   Plotly: For creating interactive visualizations.

## Setting up the Development Environment
Duration: 00:10

To run this application locally, you need to have Python installed. Follow these steps:

1.  **Install Python:** Download and install Python from the official website ([https://www.python.org/downloads/](https://www.python.org/downloads/)).  Make sure to add Python to your PATH during installation.
2.  **Clone the Repository:** Clone the application's repository to your local machine using Git:

    ```console
    git clone <repository_url>
    cd <repository_directory>
    ```

3.  **Create a Virtual Environment (Recommended):** Create a virtual environment to isolate the project dependencies:

    ```console
    python -m venv venv
    ```

4.  **Activate the Virtual Environment:**

    -   On Windows:

        ```console
        venv\Scripts\activate
        ```

    -   On macOS and Linux:

        ```console
        source venv/bin/activate
        ```

5.  **Install Dependencies:** Install the required Python packages using pip:

    ```console
    pip install streamlit numpy pandas plotly
    ```

## Running the Application
Duration: 00:03

To start the Streamlit application, navigate to the root directory of the project in your terminal and run the following command:

```console
streamlit run app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Exploring the Bond Pricing Calculator
Duration: 00:15

The Bond Pricing Calculator page allows users to calculate the price of a bond based on several key parameters.

1.  **Navigation:** In the sidebar, select "Bond Pricing Calculator".

2.  **Input Parameters:**
    -   **Coupon Rate:** Enter the annual coupon rate of the bond (e.g., 0.05 for 5%).
    -   **Maturity:** Enter the number of years until the bond matures.
    -   **Face Value:** Enter the face value of the bond (usually $1000).
    -   **Yield to Maturity (YTM):** Enter the expected yield to maturity of the bond (e.g., 0.04 for 4%).

3.  **Calculation:** Click the "Calculate Price" button. The calculated bond price will be displayed below the button.

    ```python
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
    ```

    The `calculate_bond_price` function computes the present value of the bond's future cash flows (coupon payments and face value) discounted at the yield to maturity.

<aside class="positive">
    The application handles the edge case where the Yield to Maturity (YTM) is zero. In such cases, the bond price is calculated as the sum of all coupon payments plus the face value.
</aside>

## Visualizing the Yield Curve
Duration: 00:20

The Yield Curve Visualization page provides an interactive chart that shows how the bond price changes as the Yield to Maturity (YTM) varies.

1.  **Navigation:** In the sidebar, select "Yield Curve Visualization".

2.  **Input Parameters:**
    -   **Coupon Rate:** Enter the coupon rate of the bond.
    -   **Maturity:** Enter the maturity of the bond.
    -   **Face Value:** Enter the face value of the bond.
    -   **Starting YTM:** Enter the starting value for the YTM range.
    -   **Ending YTM:** Enter the ending value for the YTM range.
    -   **Number of Points:** Use the slider to select the number of data points to generate for the chart.  A higher number of points will result in a smoother curve, but may take slightly longer to render.

3.  **Visualization:** The Plotly chart displays the bond price on the y-axis and the YTM on the x-axis. You can hover over the chart to see the exact bond price and YTM values at each point.

    ```python
    import plotly.express as px

    # ... (previous code)

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
    ```

    This code generates a series of YTM values using `np.linspace`, calculates the bond price for each YTM, and then creates an interactive line chart using Plotly.

<aside class="negative">
    Ensure that the Starting YTM is less than the Ending YTM to avoid errors in the application.  The application includes validation to prevent this.
</aside>

## Reviewing the Documentation
Duration: 00:05

The Documentation page provides detailed information about the application, including the bond pricing formula, its components, and instructions on how to use the application.

1.  **Navigation:** In the sidebar, select "Documentation".

2.  **Content:** Read through the documentation to understand the purpose of the application, the underlying formulas, and how to use the different features.

    The documentation includes:

    -   An overview of the application's features.
    -   The bond pricing formula with explanations of each component.
    -   Instructions on how to use the Bond Pricing Calculator and Yield Curve Visualization pages.

## Running Unit and Integration Tests
Duration: 00:10

The application includes unit and integration tests to ensure the correctness of the bond pricing calculation and the functionality of the different pages.

1.  **Navigate to the `tests` directory:**

    ```console
    cd tests
    ```

2.  **Run the unit tests:**

    ```console
    python test_bond_pricing.py
    ```

    This will run the unit tests in `test_bond_pricing.py`, which verify the `calculate_bond_price` function.

3.  **Run the integration tests:**

    ```console
    python test_integration.py
    ```

    This will run the integration tests in `test_integration.py`, which verify that the different pages of the application can be loaded without errors.

    ```python
    import unittest
    from pages.bond_pricing import calculate_bond_price

    class TestBondPricing(unittest.TestCase):
        def test_zero_ytm(self):
            # When YTM is 0, bond price should equal coupon_payment*maturity + face_value.
            price = calculate_bond_price(0.05, 10, 1000, 0)
            expected = 0.05 * 1000 * 10 + 1000
            self.assertAlmostEqual(price, expected, places=2)

        def test_nonzero_ytm(self):
            coupon_rate = 0.05
            maturity = 10
            face_value = 1000
            ytm = 0.04
            price = calculate_bond_price(coupon_rate, maturity, face_value, ytm)
            coupon_payment = coupon_rate * face_value
            expected = coupon_payment * (1 - (1+ytm)**(-maturity))/ytm + face_value*(1+ytm)**(-maturity)
            self.assertAlmostEqual(price, expected, places=2)

    if __name__ == '__main__':
        unittest.main()
    ```

    The unit tests cover cases with zero and non-zero YTM values to ensure the accuracy of the bond pricing calculation.

## Understanding the Docker Configuration
Duration: 00:07

The application includes a `Dockerfile` and a GitHub Actions workflow for building and pushing the application to Docker Hub. This allows you to easily deploy the application to any environment that supports Docker.

1.  **Dockerfile:** The `Dockerfile` specifies the steps required to build a Docker image for the application.

    ```dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.9-slim-buster

    # Set the working directory to /app
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    # Make port 8501 available to the world outside this container
    EXPOSE 8501

    # Run app.py when the container launches
    CMD ["streamlit", "run", "app.py"]
    ```

    This `Dockerfile` uses a Python 3.9 base image, sets the working directory to `/app`, copies the application code into the container, installs the required Python packages, exposes port 8501, and starts the Streamlit application.

2.  **.github/workflows/build_docker_and_push.yml:** This file defines a GitHub Actions workflow that automatically builds and pushes the Docker image to Docker Hub when a new tag is pushed to the repository.

    The workflow is triggered when a tag matching the pattern `v*.*.*` is pushed to the repository. It logs in to Docker Hub using the provided credentials, builds the Docker image, and pushes it to the specified repository.  The secrets `DOCKERHUB_USERNAME` and `DOCKERHUB_PASSWORD` need to be configured in the GitHub repository settings.

## Customizing the Streamlit Configuration
Duration: 00:05

The `.streamlit/config.toml` file allows you to customize the Streamlit application's behavior.

```toml
[server]
port = 8504
baseUrlPath = "67ddba6814d6b2f98be31d87"
enableCORS = false
enableXsrfProtection = false
```

This configuration file sets the following options:

-   `port`: The port on which the Streamlit server will listen (8504).
-   `baseUrlPath`: The base URL path for the application ("67ddba6814d6b2f98be31d87").  This is important when deploying to platforms that use subpaths.
-   `enableCORS`: Whether to enable Cross-Origin Resource Sharing (CORS) (false).
-   `enableXsrfProtection`: Whether to enable Cross-Site Request Forgery (XSRF) protection (false).  This is often disabled for simpler deployments, but should be enabled in production environments.

<aside class="positive">
    Adjust the port and baseUrlPath in the `config.toml` file to match your deployment environment.
</aside>

By completing this codelab, you should now have a solid understanding of the QuCreate Streamlit Lab application, including its architecture, functionality, and underlying financial concepts. You should also be able to run the application locally, use the different features, and customize the application to fit your needs.
