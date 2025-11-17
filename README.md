Quality Control ETL Project 

This is a complete, end-to-end data project demonstrating a full ETL (Extract, Transform, Load) and Business Intelligence workflow.

The Goal: I acted as a Data Analyst at an electronics company. My mission was to find the root cause of a high product defect rate (10.84%) by collecting, cleaning, and integrating data from 5 different, messy data silos.

Final Product: A one-page Power BI dashboard that unifies all 5 data sources to find the exact root cause of the failures.

♦ Final Dashboard Preview

My final dashboard successfully identified the root cause of the failures. The problem is not the production lines; it is 100% correlated with a single supplier, QualityParts.

♦ Project Workflow & Key Skills

The full step-by-step process is documented in the quality_analysis.ipynb notebook.

1. Extract & Transform (Python & pandas)

Generated 5 Messy Data Silos (supplier_performance.csv, iqc_inspections.csv, etc.) using a Python script.

Cleaned Each File: I loaded all 5 files into pandas and cleaned them individually.

Standardized text ('Electro Inc.' vs 'Electro Inc').

Fixed data types (pd.to_datetime, pd.to_numeric(errors='coerce')).

Handled outliers (e.g., removing 9999.0 sensor readings).

Renamed mismatched columns (Serial_No vs product_serial) to create common keys.

2. Aggregate & Integrate (Python & pandas)

Solved a "One-to-Many" Problem: The iqc_inspections table had many inspections for one Material_Batch_ID. I solved this by using .groupby() to aggregate the data into a new table (df_iqc_agg) showing Mean_Resistance_Reading and Total_IQC_Fails for each batch.

Created a "Master Table": I used pd.merge() to perform a series of left joins, combining all 5 clean/aggregated tables into a single "master" table with one row per product.

3. Load & Visualize (Power BI)

Loaded the single, clean master_quality_dataset.csv into Power BI.

Built the Dashboard:

KPIs: Created "Card" visuals to show Total Units (498) and Total Failures (54).

The Problem: A Donut chart shows the 10.84% overall failure rate.

The Root Cause: A "100% Stacked Bar Chart" proves the failure rate for QualityParts is dramatically higher than for any other supplier.

The "Not Guilty": A second bar chart proves all Production_Lines are working perfectly.

Interactive: Added a Slicer to allow a manager to filter the entire report by supplier.

♦ How to Run This Project

Clone this repository.

You can generate the 5 CSVs by running create_messy_data.py.

The entire cleaning and merging process is in quality_analysis.ipynb.

The final, clean output (master_quality_dataset.csv) is what I used to build the Power BI dashboard.
