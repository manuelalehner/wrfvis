""" Configuration module containing settings and constants. """
import os

wrfout = '/home/c707201/temp/WRF_output_project.nc'

# location of data directory
pkgdir = os.path.dirname(__file__)
html_template = os.path.join(pkgdir, 'data', 'template.html')
test_ts_df = os.path.join(pkgdir, 'data', 'test_df_timeseries.pkl')
test_hgt = os.path.join(pkgdir, 'data', 'test_hgt.nc')

# minimum and maximum elevations for topography plot
topo_min = 1000
topo_max = 1600
