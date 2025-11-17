import pandas as pd
import numpy as np
import datetime

print("Starting data generation...")

# Hello if you are reading this. I used this code to generate 5 messy csv files.
# I researched to understand what is the most common data problems and tried to implement it.
# It is really easy to understand if you are reading this I believe you will now everything here.
#Thanks for taking the time.

supplier_data = {
    'Material_Batch_ID': [f'B{1000 + i}' for i in range(50)],
    'Supplier_Name': np.random.choice(['ElectroInc.', 'Component Co', 'Electro Inc', 'QualityParts', 'Logi-Tek', 'ComponentCo'], 50),
    'Shipment_Date': pd.to_datetime('2025-10-01') + pd.to_timedelta(np.random.randint(0, 30, 50), 'd'),
    'Material_Cost': np.random.uniform(500, 1000, 50).round(2)
}
df_supplier = pd.DataFrame(supplier_data)
df_supplier.to_csv('supplier_performance.csv', index=False)
print("Created supplier_performance.csv")

iqc_data = {
    'Batch_ID': np.random.choice(supplier_data['Material_Batch_ID'], 100), # Some batches tested multiple times
    'IQC_Inspector': np.random.choice(['IQC-01', 'IQC-02', 'IQC-03'], 100),
    'Inspection_Timestamp': (pd.to_datetime('2025-10-10') + pd.to_timedelta(np.random.randint(0, 30*24*60, 100), 'm')).strftime('%d/%m/%Y %H:%M'),
    'Resistance_Reading': np.random.uniform(1.0, 1.5, 100).round(3).astype(str),
    'IQC_Result': np.random.choice(['Pass', 'Fail', 'PASS', 'FAIL', 'Pass '], 100)
}
df_iqc = pd.DataFrame(iqc_data)
df_iqc.loc[5, 'Resistance_Reading'] = 'N/A'
df_iqc.loc[20, 'Resistance_Reading'] = 'error'
df_iqc.to_csv('iqc_inspections.csv', index=False)
print("Created iqc_inspections.csv")

production_data = {
    'Product_Serial_Number': [f'SN{90000 + i}' for i in range(500)],
    'Material_Batch_ID': np.random.choice(supplier_data['Material_Batch_ID'], 500),
    'Production_Line': np.random.choice(['Line_A', 'Line_B', 'Line_C'], 500),
    'Build_Date': pd.to_datetime('2025-11-01') + pd.to_timedelta(np.random.randint(0, 14, 500), 'd'),
    'IPQC_Sensor_Temp': np.random.normal(75.0, 5.0, 500).round(2),
    'IPQC_Sensor_Pressure': np.random.normal(14.7, 0.2, 500).round(2)
}
df_production = pd.DataFrame(production_data)
df_production.loc[10, 'IPQC_Sensor_Temp'] = 9999.0 # Outlier
df_production.loc[50, 'IPQC_Sensor_Temp'] = -100.0 # Outlier
df_production.to_csv('ipqc_production_log.csv', index=False)
print("Created ipqc_production_log.csv")

fqc_data = {
    'Serial_No': np.random.choice(production_data['Product_Serial_Number'], 480, replace=False), # Not all products made it to FQC
    'FQC_Test_Date': pd.to_datetime('2025-11-15') + pd.to_timedelta(np.random.randint(0, 10, 480), 'd'),
    'Final_Result': np.random.choice(['PASS', 'FAIL'], 480, p=[0.9, 0.1]),
    'Defect_Code': [''] * 480
}
df_fqc = pd.DataFrame(fqc_data)
fail_indices = df_fqc[df_fqc['Final_Result'] == 'FAIL'].index
df_fqc.loc[fail_indices, 'Defect_Code'] = np.random.choice(['Code 01A-Power', 'Code 02B-Screen', '01A', '03C-Case', '02B'], len(fail_indices))
df_fqc.to_csv('fqc_final_test.csv', index=False)
print("Created fqc_final_test.csv")

return_serials = np.random.choice(df_fqc[df_fqc['Final_Result'] == 'FAIL']['Serial_No'], 20, replace=False)
return_data = {
    'product_serial': return_serials,
    'Return_Date': pd.to_datetime('2025-12-01') + pd.to_timedelta(np.random.randint(0, 20, 20), 'd'),
    'Customer_Complaint': np.random.choice(['Screen dead on arrival', 'Wont turn on', 'Case was cracked', 'Dead pixel', 'Power issue'], 20)
}
df_returns = pd.DataFrame(return_data)
df_returns.to_csv('customer_returns.csv', index=False)
print("Created customer_returns.csv")

print("\nAll 5 messy data files have been created in your project folder!")