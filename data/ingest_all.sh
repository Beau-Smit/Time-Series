mkdir download_rcp_historical
mkdir download_rcp2_6
mkdir download_rcp4_5
mkdir download_rcp6_0
mkdir download_rcp8_5

tar -xf download_historical.tar.gz --directory download_historical
tar -xf download_rcp2_6.tar.gz --directory download_rcp2_6
tar -xf download_rcp4_5.tar.gz --directory download_rcp4_5
tar -xf download_rcp6_0.tar.gz --directory download_rcp6_0
tar -xf download_rcp8_5.tar.gz --directory download_rcp8_5

python3 ingest_cmip5.py CMIP5_Agroclimatic/download_historical
python3 ingest_cmip5.py CMIP5_Agroclimatic/download_rcp2_6
python3 ingest_cmip5.py CMIP5_Agroclimatic/download_rcp4_5
python3 ingest_cmip5.py CMIP5_Agroclimatic/download_rcp6_0
python3 ingest_cmip5.py CMIP5_Agroclimatic/download_rcp8_5