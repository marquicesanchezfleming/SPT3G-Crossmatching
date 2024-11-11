import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import csv

a = 71191


def download_racs_fits(ddir, name, ra_deg, dec_deg):
    base_url = f"https://casda.csiro.au/casda_data_access/cutout/image/cube-{a}"
    params = {
        "format": "image/fits",
        "pos": f"{ra_deg},{dec_deg}",
        "size": "0.066700,0.066700"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        fits_file_path = os.path.join(ddir, f"{name}_racs.fits")
        with open(fits_file_path, 'wb') as f:
            f.write(response.content)
        print(f"FITS file downloaded and saved as {fits_file_path}")
        return fits_file_path
    else:
        return None


def process_fits_file(file_path):
    with fits.open(file_path) as hdul:
        data = hdul[0].data
        header = hdul[0].header
        print(header)

        if data is not None:
            data_2d = data[0, 0, :, :]
            plt.figure()
            plt.imshow(data_2d, origin='lower', cmap="YlOrRd")
            plt.colorbar()
            plt.title(f"Cutout of {os.path.basename(file_path)}")
            plt.savefig(file_path.replace(".fits", ".png"))
            plt.clf()

            data_2d_mJy = data_2d * 1000
            mean_flux_mJy = np.mean(data_2d_mJy)
            median_flux_mJy = np.median(data_2d_mJy)
            max_flux_mJy = np.max(data_2d_mJy)
            min_flux_mJy = np.min(data_2d_mJy)
            std_flux_mJy = np.std(data_2d_mJy)
            SNR = max_flux_mJy / std_flux_mJy
            date_obs = header.get('DATE', 'Unknown Date')

            rms_temp = np.ma.std(data_2d_mJy)
            keep = np.ma.abs(data_2d_mJy) <= 3 * rms_temp
            rms = np.ma.std(data_2d_mJy[keep])

            print(f"{os.path.basename(file_path)}Mean Flux: {mean_flux_mJy:.3f} mJy/beam")
            print(f"{os.path.basename(file_path)}Median Flux: {median_flux_mJy:.3f} mJy/beam")
            print(f"{os.path.basename(file_path)}Max Flux: {max_flux_mJy:.3f} mJy/beam")
            print(f"{os.path.basename(file_path)}Min Flux: {min_flux_mJy:.3f} mJy/beam")
            print(f"{os.path.basename(file_path)}RMS: {rms:.3f}")
            print(f"{os.path.basename(file_path)}Observation Date: {date_obs}")
        else:
            print("No data found in the FITS file.")

        output_file = "/Fall_24_Research/CSV's/SNe_data.csv"
        with open(output_file, "a") as f:
            print(f"{os.path.basename(file_path)} Mean Flux: {mean_flux_mJy:.3f} mJy/beam", file=f)
            print(f"{os.path.basename(file_path)} Median Flux: {median_flux_mJy:.3f} mJy/beam", file=f)
            print(f"{os.path.basename(file_path)} Max Flux: {max_flux_mJy:.3f} mJy/beam", file=f)
            print(f"{os.path.basename(file_path)} Min Flux: {min_flux_mJy:.3f} mJy/beam", file=f)
            print(f"{os.path.basename(file_path)} RMS: {rms:.3f}",file=f)
            print(f"{os.path.basename(file_path)} Observation Date: {date_obs}",file=f)
    try:
        os.remove(file_path)
        print(f"Deleted FITS file: {file_path}")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")


def process_csv_input(csv_file, ddir):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            name = row['name']
            ra_str = row['ra']
            dec_str = row['dec']

            fits_file = download_racs_fits(ddir, name, ra_str, dec_str)
            if fits_file:
                process_fits_file(fits_file)
            else:
                print(f"Failed to download FITS file for {name}.")

csv_file = "/everything.csv"
ddir = "/Users/Djslime07/Documents/GitHub/SomethingElse/Fall_24_Research/askap_cutouts"
process_csv_input(csv_file, ddir)