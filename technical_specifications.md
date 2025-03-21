# Bond Pricing Visualizer - Technical Specifications

## Application Overview

The Bond Pricing Visualizer is designed to help users calculate and visualize the price of a bond based on user-defined parameters such as coupon rate, maturity, face value, and yield to maturity (YTM). The application uses the bond pricing formula and presents interactive visualizations of how changes in these parameters affect bond prices. It targets finance students and investment professionals, providing educational insights and real-time data-driven interaction.

## Learning Integration

### Learning Outcomes
- Gain a deep understanding of bond pricing fundamentals.
- Develop skills in creating and utilizing interactive visualizations with Streamlit.
- Enhance knowledge of data preprocessing and exploration techniques.
- Build an application that intuitively explains complex data concepts related to bond pricing.

## Technical Details

### Installation Instructions
1. **System Requirements**: 
   - Python 3.7 or higher
   - Streamlit library

2. **Dependencies**:
   - Install Streamlit using pip:
     ```shell
     pip install streamlit
     ```
   - Additional Python libraries:
     ```shell
     pip install numpy pandas matplotlib
     ```

3. **Run the Application**:
   - Save the application script as `bond_pricing_visualizer.py`.
   - Execute the application with:
     ```shell
     streamlit run bond_pricing_visualizer.py
     ```

### Key Functional Components

#### User Input
- **Input Fields**: 
  - `Coupon Rate`: User provides the bond's coupon rate.
  - `Maturity`: User specifies the bond's maturity period.
  - `Face Value`: User enters the bond's face value.
  - `Yield to Maturity (YTM)`: User inputs the YTM to calculate the bond price.
  
#### Calculations
- **Bond Pricing Formula**: The application uses the bond pricing formula discussed in Module 2.2 to compute the bond price based on the provided inputs.

#### Visualizations
- **Line Chart**: Displays bond price variations over a range of YTM values dynamically.
- **Tooltips**: Provides detailed information about each data point on the chart, enhancing understanding and interaction.

## Dataset Details

### Synthetic Dataset
- **Source**: The dataset is synthetic, generated to reflect the structure of bond pricing scenarios.
- **Content**: Comprises numerical values that facilitate the bond pricing calculation and visualization process.
- **Purpose**: To demonstrate data handling and visualization techniques in a controlled environment.

## Visualization Details

- **Interactive Charts**: Implement dynamic line charts that illustrate how bond prices change with varying YTM values.
- **Annotations & Tooltips**: Integrated into charts, providing clarity and insights directly on the visual elements.

## Additional Details

- **User Interaction**: 
  - Interactive widgets allow users to experiment with various bond parameters.
  - Real-time updates in visualizations foster an engaging learning experience.

- **Documentation**:
  - Inline help and tooltips serve as guidance tools, assisting users in understanding and utilizing the application effectively.

- **Reference**:
  - The application is tied to concepts discussed in Module 2.2: Bond Pricing Basics, offering a practical exploration of theory through visualization and interaction.