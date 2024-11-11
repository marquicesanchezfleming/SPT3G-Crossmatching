import pandas as pd

def generate_html():
    csv_path = "../CSV's/everything.csv"
    df = pd.read_csv(csv_path)

    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SPT-ASKAP-WISE Cross-Matching</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
'''

    for index, row in df.iterrows():
        transient_name = row['name']
        ra = row['ra']
        dec = row['dec']
        type = row['type']
        redshift = row['redshift']

        row_html = f'''
        <div class="row">
            <div class="description">
                {transient_name} <br>
                Type: {type} <br>
                Right Ascension = <br>
                {ra} <br>
                Declination = <br>
                {dec} <br>
                Redshift = {redshift} <br>
            </div>
        '''

        spt_cutout_filename = f"{transient_name}_spt.png"
        spt_cutout_path = f"/Fall_24_Research/all_SPT_cutouts/{spt_cutout_filename}"
        row_html += f'''
            <div class="box">   
                <img src="{spt_cutout_path}" alt="{spt_cutout_filename}">
                <p>SPT Cutout</p>
            </div>
        '''

        askap_cutout_filename = f"{transient_name}_racs.png"
        askap_cutout_path = f"/Fall_24_Research/askap_cutouts/{askap_cutout_filename}"
        row_html += f'''
            <div class="box">   
                <img src='{askap_cutout_path}' alt="{askap_cutout_filename}">
                <p>ASKAP RACS Cutout</p>
            </div>
        '''

        allwise_cutout_filename = f"{transient_name}_allwise.png"
        allwise_cutout_path = f"/Fall_24_Research/allwise_cutouts/{allwise_cutout_filename}"
        row_html += f'''
            <div class="box">   
                <img src="{allwise_cutout_path}" alt="{allwise_cutout_filename}">
                <p>ALLWISE Cutout</p>
            </div>
        '''

        dss_cutout_filename = f"{transient_name}_dss.png"
        dss_cutout_path = f"/Fall_24_Research/dss_cutouts/{dss_cutout_filename}"
        row_html += f'''
            <div class="box">   
                <img src='{dss_cutout_path}' alt="{dss_cutout_filename}">
                <p>DSS Cutout</p>
            </div>
        '''

        row_html += '</div>'
        html_content += row_html
    html_content += '''
    </div>
</body>
</html>
'''

    output_path = "cutouts.html"
    with open(output_path, 'w') as file:
        file.write(html_content)

    print(f"HTML file '{output_path}' was successfully created.")

generate_html()
