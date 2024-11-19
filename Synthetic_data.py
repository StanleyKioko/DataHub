import pandas as pd
from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata
from google.colab import files

# Step 1: Load the dataset
file_path = '/content/drive/MyDrive/receivable_details (5).xlsx'  # Update the path as needed
data = pd.read_excel(file_path)

# Step 2: Add a unique numeric ID column if not already present
if 'id' not in data.columns:
    data['id'] = range(1, len(data) + 1)

# Step 3: Define metadata to ensure synthetic data resembles the original dataset
metadata = SingleTableMetadata()

# Manually define column metadata to reflect original structure
metadata.add_column('id', sdtype='id')
metadata.add_column('item_id', sdtype='categorical')
metadata.add_column('transaction_id', sdtype='categorical')
metadata.add_column('transaction_type', sdtype='categorical')
metadata.add_column('transaction_number', sdtype='categorical')
metadata.add_column('reference_number', sdtype='categorical')
metadata.add_column('transaction_date', sdtype='datetime')
metadata.add_column('status', sdtype='categorical')
metadata.add_column('status.1', sdtype='categorical')  # Add this line to match the data
metadata.add_column('item_name', sdtype='categorical')
metadata.add_column('account_id', sdtype='categorical')
metadata.add_column('product_id', sdtype='categorical')
metadata.add_column('product_name', sdtype='categorical')
metadata.add_column('description', sdtype='categorical')
metadata.add_column('quantity_ordered', sdtype='numerical')
metadata.add_column('quantity_invoiced', sdtype='numerical')
metadata.add_column('quantity_cancelled', sdtype='numerical')
metadata.add_column('bcy_item_price', sdtype='numerical')
metadata.add_column('fcy_item_price', sdtype='numerical')
metadata.add_column('bcy_total', sdtype='numerical')
metadata.add_column('customer_name', sdtype='categorical')
metadata.add_column('salesperson_name', sdtype='categorical')
metadata.add_column('customer_id', sdtype='categorical')
metadata.add_column('currency_code', sdtype='categorical')
metadata.add_column('currency_id', sdtype='categorical')
metadata.add_column('project_id', sdtype='categorical')
metadata.add_column('invoice.CF.End  User', sdtype='categorical')

# Step 4: Initialize the CTGAN model with the metadata
model = CTGANSynthesizer(metadata)

# Step 5: Train the model on the original data
model.fit(data)

# Step 6: Save the trained model for future use
model_file_path = "sdv-ctgan-receivable-details.pkl"
model.save(model_file_path)
print(f"Model saved as {model_file_path}")

# Step 7: Generate synthetic data
num_rows_to_generate = 1000  # Adjust the number of synthetic rows as needed
synthetic_data = model.sample(num_rows=num_rows_to_generate)

# Step 8: Save the synthetic data to a CSV file
synthetic_file_path = "synthetic_receivable_data.csv"
synthetic_data.to_csv(synthetic_file_path, index=False)

# Step 9: Provide a download link for the synthetic data
print(f"Synthetic data saved as {synthetic_file_path}. You can download it using the link below:")
files.download(synthetic_file_path)
