from astropy.io import fits
import matplotlib.pyplot as plt
import os

fits_folder = '/Users/Djslime07/Documents/GitHub/SomethingElse/Images'
fits_files = [f for f in os.listdir(fits_folder) if f.endswith('.fits')]
output_folder = '/Users/Djslime07/Documents/GitHub/SomethingElse/Done_Images'

for fits_file in fits_files:
    file_path = os.path.join(fits_folder, fits_file)

    # Use the same name for output, just change the extension to .png
    output_file_name = fits_file.replace('.fits', '.png')
    output_file_path = os.path.join(output_folder, output_file_name)

    # Open the FITS file
    with fits.open(file_path) as hdul:
        data = hdul[0].data
        header = hdul[0].header
        print(header)

        # Get the unit (if available) for information purposes
        bunit = header.get('BUNIT', 'Unknown Units')

    # Plot and save the image
    plt.imshow(data, origin='lower')
    plt.colorbar()
    plt.title(fits_file)  # Using the full file name as the plot title
    plt.savefig(output_file_path)
    print(f"Saved plot to: {output_file_path}")
    plt.clf()