import cdsapi

c = cdsapi.Client()

# c.retrieve(
#     'sis-agroclimatic-indicators',
#     {
#         'format': 'tgz',
#         'variable': [
#             'biologically_effective_degree_days', 'frost_days', 'heavy_precipitation_days',
#             'ice_days', 'maximum_of_daily_maximum_temperature', 'maximum_of_daily_minimum_temperature',
#             'mean_of_daily_maximum_temperature', 'mean_of_daily_mean_temperature', 'mean_of_daily_minimum_temperature',
#             'mean_of_diurnal_temperature_range', 'minimum_of_daily_maximum_temperature', 'minimum_of_daily_minimum_temperature',
#             'precipitation_sum', 'simple_daily_intensity_index', 'summer_days',
#             'tropical_nights', 'very_heavy_precipitation_days', 'wet_days',
#         ],
#         'origin': 'gfdl_esm2m_model',
#         'experiment': 'historical',
#         'temporal_aggregation': '10_day',
#         'period': [
#             '195101_198012', '198101_201012',
#         ],
#         'version': '1.0',
#     },
#     'CMIP5_Agroclimatic/download_historical.tar.gz')

c.retrieve(
    'sis-agroclimatic-indicators',
    {
        'origin': 'gfdl_esm2m_model',
        'variable': [
            'biologically_effective_degree_days', 'frost_days', 'heavy_precipitation_days',
            'ice_days', 'maximum_of_daily_maximum_temperature', 'maximum_of_daily_minimum_temperature',
            'mean_of_daily_maximum_temperature', 'mean_of_daily_mean_temperature', 'mean_of_daily_minimum_temperature',
            'mean_of_diurnal_temperature_range', 'minimum_of_daily_maximum_temperature', 'minimum_of_daily_minimum_temperature',
            'precipitation_sum', 'simple_daily_intensity_index', 'summer_days',
            'tropical_nights', 'very_heavy_precipitation_days', 'wet_days',
        ],
        'experiment': 'rcp2_6',
        'temporal_aggregation': '10_day',
        'period': [
            '201101_204012', '204101_207012', '207101_209912',
        ],
        'version': '1.0',
        'format': 'tgz',
    },
    'CMIP5_Agroclimatic/download_rcp2_6.tar.gz')

c.retrieve(
    'sis-agroclimatic-indicators',
    {
        'origin': 'gfdl_esm2m_model',
        'variable': [
            'biologically_effective_degree_days', 'frost_days', 'heavy_precipitation_days',
            'ice_days', 'maximum_of_daily_maximum_temperature', 'maximum_of_daily_minimum_temperature',
            'mean_of_daily_maximum_temperature', 'mean_of_daily_mean_temperature', 'mean_of_daily_minimum_temperature',
            'mean_of_diurnal_temperature_range', 'minimum_of_daily_maximum_temperature', 'minimum_of_daily_minimum_temperature',
            'precipitation_sum', 'simple_daily_intensity_index', 'summer_days',
            'tropical_nights', 'very_heavy_precipitation_days', 'wet_days',
        ],
        'experiment': 'rcp4_5',
        'temporal_aggregation': '10_day',
        'period': [
            '201101_204012', '204101_207012', '207101_209912',
        ],
        'version': '1.0',
        'format': 'tgz',
    },
    'CMIP5_Agroclimatic/download_rcp4_5.tar.gz')

c.retrieve(
    'sis-agroclimatic-indicators',
    {
        'origin': 'gfdl_esm2m_model',
        'variable': [
            'biologically_effective_degree_days', 'frost_days', 'heavy_precipitation_days',
            'ice_days', 'maximum_of_daily_maximum_temperature', 'maximum_of_daily_minimum_temperature',
            'mean_of_daily_maximum_temperature', 'mean_of_daily_mean_temperature', 'mean_of_daily_minimum_temperature',
            'mean_of_diurnal_temperature_range', 'minimum_of_daily_maximum_temperature', 'minimum_of_daily_minimum_temperature',
            'precipitation_sum', 'simple_daily_intensity_index', 'summer_days',
            'tropical_nights', 'very_heavy_precipitation_days', 'wet_days',
        ],
        'experiment': 'rcp6_0',
        'temporal_aggregation': '10_day',
        'period': [
            '201101_204012', '204101_207012', '207101_209912',
        ],
        'version': '1.0',
        'format': 'tgz',
    },
    'CMIP5_Agroclimatic/download_rcp6_0.tar.gz')

c.retrieve(
    'sis-agroclimatic-indicators',
    {
        'origin': 'gfdl_esm2m_model',
        'variable': [
            'biologically_effective_degree_days', 'frost_days', 'heavy_precipitation_days',
            'ice_days', 'maximum_of_daily_maximum_temperature', 'maximum_of_daily_minimum_temperature',
            'mean_of_daily_maximum_temperature', 'mean_of_daily_mean_temperature', 'mean_of_daily_minimum_temperature',
            'mean_of_diurnal_temperature_range', 'minimum_of_daily_maximum_temperature', 'minimum_of_daily_minimum_temperature',
            'precipitation_sum', 'simple_daily_intensity_index', 'summer_days',
            'tropical_nights', 'very_heavy_precipitation_days', 'wet_days',
        ],
        'experiment': 'rcp8_5',
        'temporal_aggregation': '10_day',
        'period': [
            '201101_204012', '204101_207012', '207101_209912',
        ],
        'version': '1.0',
        'format': 'tgz',
    },
    'CMIP5_Agroclimatic/download_rcp8_5.tar.gz')