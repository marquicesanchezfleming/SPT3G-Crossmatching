import pandas as pd
import matplotlib.pyplot as plt

spt_only_data = pd.read_csv('CSV')
type_counts = spt_only_data['Type'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(type_counts.index, type_counts.values, color='skyblue')
plt.xlabel('Supernova Type', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Frequency of Supernova Types (Excluding SNe without SPT cutout', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

all_data = pd.read_csv("/Fall_24_Research/CSV's/everything.csv")
type_counts2 = all_data['Type'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(type_counts2.index, type_counts2.values, color='skyblue')
plt.xlabel('Supernova Type', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Frequency', fontsize=14)
plt.title('Frequency of Supernova Types (Including SNe without SPT cutout', fontsize=16)
plt.tight_layout()
plt.show()
