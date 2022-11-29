import obspy

from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError, URLError


# IRL, you would use beautiful soup to scrape the <a href> elements
# and download the files
url = "https://pds-geosciences.wustl.edu/lunar/urn-nasa-pds-apollo_pse/data/xa/continuous_waveform/s11/1969/202/xa.s11..att.1969.202.0.mseed"

urlretrieve(url, "flask-backend/files/xa.s11..att.1969.202.0.mseed")

