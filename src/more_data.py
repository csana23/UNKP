import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type':'reanalysis',
        'format':'grib',
        'variable':[
            'relative_humidity','temperature'
        ],
        'pressure_level':'1000',
        'year':'2014',
        'month':'02',
        'day':'26',
        'time':'15:00'
    },
    'download2.grib')