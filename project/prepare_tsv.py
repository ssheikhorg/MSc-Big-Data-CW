import pandas as pd
from sklearn.preprocessing import StandardScaler


data = pd.read_excel('climate_data.xlsx')
data['Year'] = data['Date'].dt.year  # Extract Year from Date

features = data[['Average Temperature', 'Year']]

scaler = StandardScaler()
normalized_features = scaler.fit_transform(features)

# Save features as TSV
features_df = pd.DataFrame(normalized_features, columns=['Average Temperature', 'Year'])
features_df.to_csv('features.tsv', sep='\t', index=False, header=False)

# Prepare metadata
metadata_df = data[['City', 'Country', 'Year']]

# Save metadata as TSV
metadata_df.to_csv('metadata.tsv', sep='\t', index=False, header=True)
