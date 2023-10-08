# Global Heatwave Warning Systems Analysis

## Introduction

Heatwaves are extreme weather events with significant impacts on public health and economies globally. With the intensification of these events due to climate change, establishing efficient and timely heatwave warning systems has become a priority. This research project aims to understand the global landscape of heatwave preparedness, focusing on identifying countries with operational heatwave warning systems.

## Problem Statement

Recognizing the critical need to protect vulnerable populations from the adverse effects of extreme heat, the establishment of effective Heat Warning Systems (HWS) is now a priority. The existing Heatwave Warning Systems Inventory developed by WMO is the primary source for understanding the HWS global distribution. However, it's incomplete, making it challenging to ascertain the extent of global preparedness for heatwaves. This research seeks to bridge this gap.

### Research Questions

1. Which specific countries or regions are documented in the WMO's database as having HWS?
2. Based on external data sources, which countries or regions have HWS but are not listed in the WMO's database?
3. What percentage of countries globally have implemented HWS, and how does this distribution vary by region?
4. Is there a discernible pattern between a country's income level (e.g., low, middle, high income) and the presence or absence of an HWS?

## Technical Details

### Data Sources

- **WMO's Heatwave Warning Systems Inventory**: Primary source for understanding the HWS global distribution.
- **[Name of the External Data Source]**: Used to cross-verify and supplement the information from WMO's database.

### Libraries and Tools Used

- **Python**: The primary programming language used for data analysis and processing.
- **Pandas**: For data manipulation and analysis.
- **BeautifulSoup**: For web scraping to gather data from online research journals.
- **[Other Library]**: [Purpose of the library/tool]

### Repository Structure

- `data/`: Contains raw data files and processed datasets.
- `scripts/`: Python scripts and Jupyter notebooks used for data analysis.
- `projectdocument/`: Charts, graphs, and other visual representations of our findings.
- `README.md`: This document, providing an overview of the project.

### Setup and Installation

To reproduce our analysis, follow these steps:

1. Clone this repository to your local machine.
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the Jupyter notebooks in the `scripts/` directory.

## Data Engineering Journey

Our data engineering process can be visualized as a journey through five main steps:

### 1. 📦 Data Collection
- **WMO Data Extraction**: Data was sourced from the embedded Power BI dashboard on the WMO website, a task that presented unique challenges due to its dynamic nature.
- **PubMed Data Retrieval**: Leveraged the PubMed API to fetch relevant data, transforming the XML response into a structured DataFrame.

### 2. 🧹 Data Cleaning & Validation
- Harmonized data with the WMO template to ensure consistency.
- Engaged in collaborative data validation with team members, streamlining the cleaning process.

### 3. 🧩 Data Integration
- Unified various datasets, including PubMed search results and additional data from Google Search and Google Scholar.

### 4. 🧠 Predictive Modeling & Analysis
- Adopted advanced tokenization techniques and utilized a pretrained RoBERTa model for predictions.
- Recognized potential for model enhancement in future iterations.

### 5. 📊 Results & Insights
- Formulated rules for overall prediction, emphasizing the significance of even a single positive prediction.
- Generated comprehensive summaries capturing research papers per country and detailed nested information.

## Contributors

[List of contributors with their roles and/or affiliations]

## Acknowledgements

This research project is a contribution to the datathon challenge organized by [Women in Data](https://www.womenindata.org/datathon).



