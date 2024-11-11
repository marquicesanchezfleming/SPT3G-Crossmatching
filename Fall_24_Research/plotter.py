import pandas as pd
import matplotlib.pyplot as plt
from astropy.cosmology import Planck18
import numpy as np

z1 = 0.014
z2 = 0.135
z3 = 0.0868

cow_csv = "/Users/Djslime07/Documents/GitHub/SomethingElse/output1.csv"
data1 = pd.read_csv(cow_csv)

mrf_csv = "/Users/Djslime07/Documents/GitHub/SomethingElse/output2.csv"
data2 = pd.read_csv(mrf_csv)

wpp_csv = "/Users/Djslime07/Documents/GitHub/SomethingElse/output3.csv"
data3 = pd.read_csv(wpp_csv)

data1['normalized_mjd'] = data1['mjd'] - data1['mjd'].min()
data2['normalized_mjd'] = data2['mjd'] - data2['mjd'].min()
data3['normalized_mjd'] = data3['mjd'] - data3['mjd'].min()

data1['abs_mag'] = data1['mag'] - Planck18.distmod(z=[z1]).value
data2['abs_mag'] = data2['mag'] - Planck18.distmod(z=[z2]).value
data3['abs_mag'] = data3['mag'] - Planck18.distmod(z=[z3]).value

data1["fixed_abs_mag"] = data1['abs_mag'] + 2.5*np.log10(1+z1)
data2["fixed_abs_mag"] = data2['abs_mag'] + 2.5*np.log10(1+z2)
data3["fixed_abs_mag"] = data3['abs_mag'] + 2.5*np.log10(1+z3)

mjd_cutoff = 15
data1_filtered = data1[data1['normalized_mjd'] <= mjd_cutoff]
data2_filtered = data2[data2['normalized_mjd'] <= mjd_cutoff]
data3_filtered = data3[data3['normalized_mjd'] <= mjd_cutoff]

plt.figure(figsize=(10, 6))
plt.plot(data1_filtered['normalized_mjd'], data1_filtered['fixed_abs_mag'], label='AT2018cow', linestyle='--', color='black')
plt.plot(data2_filtered['normalized_mjd'], data2_filtered['fixed_abs_mag'], label='AT2020mrf', linestyle=':', color='black')
plt.scatter(data3_filtered['normalized_mjd'], data3_filtered['fixed_abs_mag'], label='AT2024wpp', color='red', marker='o', s=10)
plt.xlabel('Days since explosion (Rest Frame)')
plt.ylabel('Absolute Magnitude')
plt.title('Optical Light Curve of Three LFBOTS, g-band')
plt.ylim(-22, -18)
plt.gca().invert_yaxis()
plt.legend()
plt.show()