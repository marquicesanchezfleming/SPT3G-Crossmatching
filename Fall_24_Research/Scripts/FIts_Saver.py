from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import os

fits_folder = '/Users/Djslime07/Documents/GitHub/SomethingElse/Fall_24_Research/temp_fits'
output_folder = '/Users/Djslime07/Documents/GitHub/SomethingElse/Fall_24_Research/finished_fits'
os.makedirs(output_folder, exist_ok=True)
fits_files = [f for f in os.listdir(fits_folder) if f.endswith('.fits')]

for fits_file in fits_files:
    file_path = os.path.join(fits_folder, fits_file)

    try:
        with fits.open(file_path) as hdul:
            data = hdul[0].data
            header = hdul[0].header
            print(header)
            object_name = header.get('OBJECT', 'Unknown OBJECT')
            date_obs = header.get('DATE-OBS', 'Unknown Date')

            if data is not None:
                plt.imshow(data, origin='lower')
                plt.colorbar()
                plt.title(f"SPT Cutout of {object_name}")
                output_path = os.path.join(output_folder, f"{object_name}_cutout.png")
                plt.savefig(output_path)
                plt.clf()

                data_2d_mJy = data * 1000
                mean_flux_mJy = np.mean(data_2d_mJy)
                median_flux_mJy = np.median(data_2d_mJy)
                max_flux_mJy = np.max(data_2d_mJy)
                min_flux_mJy = np.min(data_2d_mJy)
                std_flux_mJy = np.std(data_2d_mJy)
                if std_flux_mJy > 0:
                    SNR = max_flux_mJy / std_flux_mJy
                else:
                    print("No SNR!")

                print(f"Object: {object_name}")
                print(f"Mean Flux: {mean_flux_mJy:.3f} mK")
                print(f"Median Flux: {median_flux_mJy:.3f} mK")
                print(f"Max Flux: {max_flux_mJy:.3f} mK")
                print(f"Min Flux: {min_flux_mJy:.3f} mK")
                print(f"Standard Deviation of Flux: {std_flux_mJy:.3f} mK\n")
                print(f"SNR: {SNR:.3f}")


            else:
                print(f"No data found in {fits_file}")

    except Exception as e:
        print(f"Failed to process {fits_file}: {e}")
