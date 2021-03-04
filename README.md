# ALCO Geocoder

Geocoder functions using [Allgheny County's GIS Esri API](http://gisdata.alleghenycounty.us/arcgis/rest/services/Geocoders/AddressPoints/GeocodeServer/findAddressCandidates) for use in Python and R. Note that the address column should be as complete as possible ie: `436 Grant Street, Pittsburgh PA, 15219` but should not include Apartment/Unit names/numbers. Geocoded addresses are the highest scored coordinates.

_Warning: For geocodes in the tens of thousands users are asked to wait until non-business hours to avoid crashing the server._

The `usps_geocde.R` functions the same way as the County script, but uses the [United States Postal Service Geocoder](https://gis.usps.com/arcgis/rest/services/locators/US_Street/GeocodeServer/findAddressCandidates).

### Loading:

R: `source('https://raw.githubusercontent.com/Allegheny-CountyStats/ALCO-Geocoder/master/alco_geocoder.R')`

Python 2 (untested): `execfile("https://raw.githubusercontent.com/Allegheny-CountyStats/ALCO-Geocoder/master/County.py")`

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
