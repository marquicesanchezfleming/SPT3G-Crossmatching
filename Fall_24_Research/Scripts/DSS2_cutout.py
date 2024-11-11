import pandas as pd
import requests
import os
from astropy.io import fits
import matplotlib.pyplot as plt
def create_download_url(ra, dec, width=1200, height=900, fov=0.167):
    fov = 10 / 60
    url = (f"https://alasky.cds.unistra.fr/hips-image-services/hips2fits?"
           f"hips=CDS%2FP%2FDSS2%2Fcolor&width=1200&height=1200"
           f"&fov={fov}&projection=AIT&coordsys=icrs&rotation_angle=0.0"
           f"&ra={ra}&dec={dec}&format=fits")
    return url


def download_fits_file(url, filename):
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url} (Status code: {response.status_code})")

def fits_to_png(fits_file, png_file):
    with fits.open(fits_file) as hdul:
        image_data = hdul[0].data

        if image_data.ndim == 3:
            plt.imshow(image_data.transpose(1, 2, 0), origin='lower', aspect='auto')
        else:
            plt.imshow(image_data, cmap='gray', origin='lower', aspect='auto')
        plt.axis('off')
        plt.savefig(png_file, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"Converted {fits_file} to {png_file}")

coordinates_df = pd.read_csv('/Fall_24_Research/Original_List.csv')

os.makedirs('../Images/dss_fits', exist_ok=True)
os.makedirs('../Images/dss_cutouts', exist_ok=True)


for index, row in coordinates_df.iterrows():
    name = row['name']
    ra = row['ra']
    dec = row['dec']
    url = create_download_url(ra, dec)
    fits_filename = os.path.join('../Images/dss_fits', f"{name}.fits")
    png_filename = os.path.join('../Images/dss_cutouts', f"{name}_dss.png")

    download_fits_file(url, fits_filename)
    fits_to_png(fits_filename, png_filename)

    os.remove(fits_filename)
    print(f"Deleted: {fits_filename}")