import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

with fits.open('/Users/Djslime07/Downloads/SN2019esa_150GHz_yearly_collate_wideg_psth.fits') as hdul_supernova:
    supernova_data = hdul_supernova[0].data

with fits.open('/Users/Djslime07/Downloads/SN2019esa_90GHz_yearly_collate_wideg_psth.fits') as hdul_reference:
    reference_data = hdul_reference[0].data

supernova_data -= np.median(supernova_data)
reference_data -= np.median(reference_data)

difference_map = supernova_data - reference_data

plt.figure(figsize=(10, 8))
plt.imshow(difference_map, cmap='seismic', origin='lower')
plt.colorbar(label='Flux Difference')
plt.title('Difference Map (Supernova - Reference)')
plt.xlabel('X Pixel')
plt.ylabel('Y Pixel')
plt.show()
