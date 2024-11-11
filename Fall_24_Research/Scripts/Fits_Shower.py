import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits


file_path1 = f"/Users/Djslime07/Downloads/SN 2019esa_150GHz_yearly_collate_wideg_psth.fits"
with fits.open(file_path1) as hdul:
    data = hdul[0].data
    header = hdul[0].header
    print(header)

    peak_flux = np.ma.max(data)
    peakstr = f"Peak flux: {peak_flux:.4} mK"
    print(peakstr)

    rms_temp = np.ma.std(data)
    keep = np.ma.abs(data) <= 3 * rms_temp
    rms = np.ma.std(data[keep])
    rmsstr = f"RMS: {rms:.4f} mK"
    print(rmsstr)

    if data is not None:
        plt.figure()
        plt.imshow(data, origin='lower')
        plt.colorbar()
        plt.title(f"SN2019esa, 150 GHz, G-Band \n{peakstr}\n{rmsstr}", fontsize=9.5)
        plt.show()


file_path = "/Users/Djslime07/Downloads/cutout-725130-imagecube-222879 (1).fits"
with fits.open(file_path) as hdul:
        data2 = hdul[0].data
        header = hdul[0].header

        if data2 is not None:
            data_2d = data2[0, 0, :, :]

            peak_flux = np.ma.max(data_2d) * 100
            peakstr2 = f"Peak flux: {peak_flux:.6f} cJy/beam"
            #print(peakstr2)

            rms_temp = np.ma.std(data_2d)
            keep = np.ma.abs(data_2d) <= 3 * rms_temp
            rms = np.ma.std(data_2d[keep]) * 100
            rmsstr2 = f"RMS: {rms:.6f} cJy/beam"
            #print(rmsstr2)

            plt.figure()
            plt.imshow(data_2d, origin='lower', cmap="YlOrRd")
            plt.colorbar()
            plt.title(f"SN2019esa 1367.5 MHz \n{peakstr2}\n{rmsstr2}", fontsize=9.5)
            plt.show()

fits_viewer_path = "/Users/Djslime07/Downloads/tns_2019esa_2019-05-08_10-48-06_FTS_FLOYDS-S_Global_SN_Project.fits"
with fits.open(fits_viewer_path) as hdul:
    data = hdul[0].data
    header = hdul[0].header
    if data2 is not None:
        data_2dd = data2[0, 0, :, :]

        plt.figure()
        plt.imshow(data_2dd, origin='lower')
        plt.title("SNe Light Curve")
        plt.show()