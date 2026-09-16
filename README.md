# 🐍 Applicant Demographics Data Preprocessing Pipeline

A programmatic data cleaning and standardization script built using Python 3 and the **Pandas** library to process internship application records according to project guidelines.

## 🛠️ Data Cleaning Steps Implemented
1. **Deduplication:** Utilized `.drop_duplicates()` to automatically identify and isolate redundant application entries.
2. **Outlier Filtering & Imputation:** Implemented conditional logical filters (`.loc`) to detect invalid negative age fields and excessive age values, normalizing them to a cohort baseline of 23.
3. **Text Case Standardization:** Applied vectorized string methods `.str.title()` and `.str.lower()` to repair erratic text casing across names and required skills fields.
4. **Operations Deployment:** Exported the verified data frames into a clean file ready for processing (`cleaned_applicant_data.csv`).

## 💻 Tech Stack Used
* Python 3
* Pandas Library
* Python IDLE
