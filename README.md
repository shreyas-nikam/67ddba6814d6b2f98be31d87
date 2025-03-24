# Bond Pricing & Yield Curve Analysis Lab

This repository contains a Streamlit application that facilitates interactive bond pricing calculations and yield curve analysis.

## Features

- Multi-page application for bond pricing calculations, yield curve visualization, and detailed explanations.
- Real-time interactive visualizations using Plotly.
- Comprehensive markdown documentation explaining the bond pricing formula, data, and visualizations.
- Unit tests and integration tests to ensure code quality.
- Docker support for containerized deployment.

## Installation

1. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   streamlit run app.py
   ```

## Running Tests

- **Unit Tests:** Run `pytest tests/test_bond_pricing.py`
- **Integration Tests:** Run `pytest tests/integration/test_app.py`

## Docker

Use the provided Dockerfile and docker-compose.yml to run the application in a Docker container.

## License

© 2025 QuantUniversity. All Rights Reserved.
