# CleanSweep - Automated Data Cleaning Bot

**CleanSweep** is a Python-based tool designed to automate Exploratory Data Analysis (EDA) and data cleaning tasks, including handling missing values, detecting and removing outliers, and converting data types intelligently. It leverages popular libraries like Pandas, SweetViz, and Pandas-Profiling to simplify and speed up the data preprocessing phase in any data science project.



## Features

- **Automated EDA** using SweetViz or Pandas-Profiling for quick insights  
- **Missing Value Handling:** Summarizes and imputes missing data with configurable strategies  
- **Outlier Detection & Removal:** Detects outliers using IQR method with optional removal  
- **Data Type Conversion:** Infers and converts column data types automatically using heuristics and ML models  
- **Robust Logging:** Tracks the entire cleaning process and flags columns failing dtype conversion  
- **Command-line Interface:** Easily run and customize cleaning steps via CLI options  


## Installation

 Version : Python 3.7
 Install the dependencies:

```bash
pip install -r requirements.txt
```

or install maually
```bash
pip install pandas sweetviz pandas-profiling scikit-learn
```

## Usage
Run the cleansweep bot for any dataset
```bash
python main.py --input path/to/your/dataset.csv --output cleaned_data.csv --handle-missing --handle-outliers --handle-dtypes
```



Contact
Created by Shivani - feel free to reach out via (shivanis1273@gmail.com )

