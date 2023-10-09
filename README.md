# Global Heatwave Warning Systems Analysis

## Introduction

Heatwaves are extreme weather events with significant impacts on public health and economies globally. With the intensification of these events due to climate change, establishing efficient heatwave warning systems in a timely manner has become a priority. This research project aims to understand the global landscape of heatwave preparedness, focusing on identifying countries with operational heatwave warning systems.

## Problem Statement

Recognizing the critical need to protect vulnerable populations from the adverse effects of extreme heat, the establishment of effective Heat Warning Systems (HWS) is now a priority. The existing Heatwave Warning Systems Inventory developed by WMO is the primary source for understanding the HWS global distribution. However, it is incomplete, making it challenging to ascertain the extent of global preparedness for heatwaves. This research seeks to bridge this gap.

## Project Objective

The overarching objective of this project is not just to provide a snapshot of the current state of Heatwave Warning Systems (HWS) globally but to establish a robust foundation for future research and improvements. By establishing a systematic approach to data extraction, cleaning, and predictive modeling, we aim to create a blueprint that WMO and other stakeholders can leverage. The methodologies and insights presented here can guide efforts to enhance data collection, refine predictive models, and ultimately, improve heatwave preparedness worldwide. This project underscores the potential of data-driven strategies in addressing global challenges and paves the way for more informed decision-making in the realm of climate preparedness.

### Research Questions

1. Which specific countries or regions are documented in the WMO's database as having HWS?
2. Based on external data sources, which countries or regions have HWS but are not listed in the WMO's database?
3. What percentage of countries globally have implemented HWS, and how does this distribution vary by region?
4. Is there a discernible pattern between a country's income level (e.g., low, middle, high income) and the presence or absence of an HWS?

## Technical Details

### Data Sources

- **[WMO's Heatwave Warning Systems Inventory](https://community.wmo.int/en/members/profiles)**: Primary source for understanding the HWS global distribution.
- **[PubMed](https://pubmed.ncbi.nlm.nih.gov/)**: Used to cross-verify and supplement the information from WMO's database.
- **[Google Scholar and Google Search](https://scholar.google.com/)**: Used to cross-verify and supplement the information from WMO's database.
- **[Population Density vs. Prosperity](https://ourworldindata.org/grapher/population-density-vs-prosperity)**: A supplementary dataset used to investigate patterns between HWS and income levels.

### Libraries and Tools Used

- **Python**: The primary programming language used for data analysis and processing.
- **Pandas**: For data manipulation and analysis.
- **Selenium**: For web scraping to gather data from online research journals.
- **BeautifulSoup**: For web scraping to gather data from online research journals.
- **Hugging Face's RoBERTa**: Utilized for predicting the presence of heatwave systems based on research paper abstracts.

### Repository Structure

- `data/`: 
  - `raw/`: Contains the initial data files sourced from various platforms such as WMO, PubMed, Google Scholar, and Google Search.
  - `processed/`: Datasets that have undergone cleaning, transformation, or any other processing.
  - `supplementary_data/`: Additional datasets used for deeper insights, such as the dataset on income levels.

- `scripts/`: 
  - `data_extraction/`: Scripts and notebooks dedicated to the data extraction process from various sources.
  - `data_modeling/`: Scripts and notebooks focused on predictive modeling using tools like Hugging Face's RoBERTa.
  - `data_processing/`: Scripts and notebooks used for data cleaning, validation, and other preprocessing tasks.

- `projectdocument/`: 
  - `data_engineering/`: Documentation detailing the data engineering journey, from collection to integration.
  - `visualizations/`: Charts, graphs, and other visual representations of our findings.
  - `instructions/`: Guidelines and steps for reproducing the analysis or setting up the project.
  - `presentations/`: Slides or other presentation materials showcasing the project's results and insights.

- `README.md`: This document, providing an overview of the project, methodologies, and other relevant details.


### Setup and Installation

To reproduce our analysis, follow these steps:

1. Clone this repository to your local machine.
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the Jupyter notebooks in the `scripts/` directory.

## Data Engineering Journey

Our data engineering process can be visualized as a journey through several main steps:

### 1. 📦 Data Collection
- **WMO Data Extraction**: Data was sourced from the embedded Power BI dashboard on the WMO website, a task that presented unique challenges due to its dynamic nature. 
- **PubMed Data Retrieval**: Leveraged the PubMed API to fetch relevant data, transforming the XML response into a structured DataFrame.
- **Google Scholar and Google Search**: Scanned Google and Google Scholar using specific keywords to collect research journals and papers.

### 2. 🧹 Data Cleaning & Validation
#### WMO Data:
- Harmonized data extracted from the WMO website with the provided WMO template, ensuring that country names were spelled correctly and matched the template.
- Checked for and handled duplicate entries to maintain data integrity.
- Randomly selected countries and validated their data to ensure accurate extraction from the WMO website.

#### API and Web Data:
- Cleaned and harmonized data extracted from APIs and other web sources.
- Checked for and handled duplicate entries to ensure data consistency and accuracy.
- Validated random samples to ensure the accuracy of data extraction from these sources.

### 3. 🧠 Predictive Modeling & Analysis
- **PubMed Predictions**: Adopted advanced tokenization techniques using Hugging Face's RobertaTokenizer and utilized a pretrained RoBERTa model to predict the presence of heatwave systems based on abstracts from the PubMed results.
- **Google Scholar and Google Search Predictions**: Used a Random Forest model to make predictions based on the extracted data.
- The prediction approach has potential for future improvements with more training data and model fine-tuning.

### 4. 🧩 Data Integration & Final Database Creation
- Unified various datasets, including predictions from PubMed, Google Search, and Google Scholar, to create a comprehensive database.

### 5. 📊 Results & Insights
- Formulated rules for overall prediction, emphasizing the significance of even a single positive prediction.
- Generated comprehensive summaries capturing research papers per country and detailed nested information.

## Roadmap & Future Improvements

As with any research project, there's always room for enhancement and expansion. Here's a roadmap of potential improvements and areas we're looking to focus on in the future:

### 1. **Data Enrichment**:
- **Expand Data Sources**: While we've utilized a few key sources for this project, numerous other databases and journals could provide additional valuable insights.
- **Real-time Data Integration**: Implementing a system to fetch and update data in real-time can ensure the database remains current.

### 2. **Model Refinement**:
- **Fine-tuning**: The predictive models can benefit from further fine-tuning with a larger dataset.
- **Incorporate Feedback Loop**: As more data gets collected and validated, it can be fed back into the model for continuous learning.

### 3. **User Interface & Accessibility**:
- **Develop a Web Interface**: A user-friendly web interface can make it easier for stakeholders to access and interpret the data.
- **API Development**: Creating an API would allow other systems and applications to tap into our database, fostering collaboration and data sharing.

### 4. **Collaboration & Community Engagement**:
- **Open Source Contribution**: Encouraging the community to contribute can lead to faster improvements and diverse perspectives.
- **Workshops & Webinars**: Organizing events to educate stakeholders on the importance of HWS and how to leverage our database.

### 5. **Feedback & Iteration**:
- **Feedback System**: Implementing a system for users to provide feedback on predictions, data accuracy, and usability.
- **Regular Review & Iteration**: Setting up periodic reviews to assess the system's performance and make necessary adjustments.

### Issues & Challenges:
While we've made significant strides, we've also encountered challenges along the way:
- **Data Extraction Limitations**: Dynamic websites and request limits posed challenges in data extraction.
- **Data Quality**: Ensuring the accuracy and reliability of data from various sources required rigorous validation.

We're keen on addressing these challenges and continuously refining our approach. Community feedback and collaboration will be pivotal in this journey.

## Contributors

## Team Heatwave Heroines
Five passionate ladies from around the world united with a shared mission: to be part of the solution.

- **[SylwiaK-S](https://github.com/SylwiaK-S)**: Project Manager
- **[itsfelli](https://github.com/itsfelli)**: Data Scientist
- **[hicranA](https://github.com/hicranA)**: Data Engineer
- **[cfreeccss](https://github.com/cfreeccss)**: Power BI Developer
- **[Fateeemah01](https://github.com/Fateeemah01)**: Data Analyst

Together, we've combined our diverse skills and backgrounds to tackle the challenge of understanding global heatwave preparedness. Our collaboration is a testament to the power of collective effort in addressing pressing global issues.

## Acknowledgements

This research project is a contribution to the datathon challenge hosted by [Women in Data](https://www.womenindata.org/datathon).
