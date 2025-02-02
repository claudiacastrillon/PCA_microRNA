import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# List of microRNAs
micrornas = [
    "hsa-miR-148a-3p", "hsa-miR-199a-3p", "hsa-miR-1307-3p", "hsa-let-7f-5p",
    "hsa-miR-221-3p","hsa-miR-4508", "hsa-miR-223-5p", "hsa-miR-1246",
    "hsa-miR-484", "hsa-miR-24-3p", "hsa-miR-223-3p", "hsa-miR-142-5p",
    "hsa-miR-197-3p", "hsa-miR-23a-3p","hsa-miR-143-3p", "hsa-miR-193a-5p", 
    "hsa-miR-151a-3p"
]

# Simulate some random data for microRNA expressions (100 samples)
np.random.seed(1184)
mean = np.zeros(len(micrornas))
cov = np.identity(len(micrornas)) * 0.1  # Introducing some correlation
data = np.random.multivariate_normal(mean, cov, size=1000)
data = np.exp(data)  # Log-normal distribution
df = pd.DataFrame(data, columns=micrornas)

# Perform PCA
pca = PCA(n_components=13)
principal_components = pca.fit_transform(df)
explained_variance = pca.explained_variance_ratio_

# Plot explained variance
plt.figure(figsize=(10, 7))
bars=plt.bar(range(1, 14), explained_variance * 100, alpha=0.5, align='center')
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Components')
plt.title('PCA - Explained Variance')

# Add the names of the selected 13 microRNAs on top of each bar
for bar, name in zip(bars, micrornas[:13]):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()*0.7, yval - 0.5, name, ha='center', va='bottom', fontsize=9, rotation=45)

plt.show()

# Get the loading scores for each microRNA
loadings = pca.components_.T
loading_scores = pd.DataFrame(loadings, index=micrornas)

# Sum the absolute values of the loadings for each microRNA to get their overall contribution
contribution_scores = loading_scores.abs().sum(axis=1)

# Sort the contributions and select the top 13 microRNAs
top_13_micrornas = contribution_scores.nlargest(13).index.tolist()

print("Top 13 microRNAs selected by PCA:")
print(top_13_micrornas)

# Optionally, filter the dataframe to include only the top 13 microRNAs for further analysis
df_reduced = df[top_13_micrornas]
print(df_reduced)

# Define the directory where the Excel file will be saved
directory = "/Users/claudiacastrillonalvarez/Downloads/"

# Save the reduced DataFrame to an Excel file in the specified directory
file_path = directory + 'reduced_microRNAs_PCA_13_microRNAs.xlsx'
df_reduced.to_excel(file_path, index=False)

print(f"DataFrame with top 13 microRNAs saved to '{file_path}'")