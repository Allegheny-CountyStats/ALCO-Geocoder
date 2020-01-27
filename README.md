# ALCO Geocoder

Geocoder functions using Allgheny County's GIS Esri API for use in Python and R. Note that the address column should be as complete as possible ie: `436 Grant Street, Pittsburgh PA, 15219`. Geocodes addresses by the highest scored coordinates.

_Warning: For geocodes in the tens of thousands users are asked to wait until non-business hours to avoid crashing the server._

### Loading:

R: `source('https://raw.githubusercontent.com/Allegheny-CountyStats/ALCO-Geocoder/master/alco_geocoder.R')`

Python 2: `execfile("https://raw.githubusercontent.com/Allegheny-CountyStats/ALCO-Geocoder/master/County.py") (untested)`

Python 3: `exec(open('https://raw.githubusercontent.com/Allegheny-CountyStats/ALCO-Geocoder/master/County.py').read())`

### Usage:

R:

```
geo_data <- data %>%
  mutate_countyGeo(Full_Address_Column)
```

Python:

```
# Single Address
county_geocode('436 Grant Street, Pittsburgh PA 15219')
# Pandas
county_geo_pd(df, col = 'Full_Address_Col'):
```
