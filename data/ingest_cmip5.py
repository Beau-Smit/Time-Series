from multiprocessing.sharedctypes import Value
import numpy as np
import xarray as xr
import os
import argparse
import re

def ingest_cmip5(download_dir, out_csv):
    netcdf_paths = os.listdir(download_dir)
    for netcdf_path in netcdf_paths:

        fullpath = os.path.join(download_dir, netcdf_path)
        print("processing " + netcdf_path)
        feat_xr = xr.open_dataset(fullpath)
        scenario = re.findall('(?<=esm2m_).*(?=_dek)', netcdf_path)[0]

        var = list(feat_xr.data_vars.keys())[1]
        tgt_lat = xr.DataArray(np.arange(43.75, 46.75, 0.5), dims=["lat"])
        tgt_lon = xr.DataArray(np.arange(-96.25, -93.75, 0.5), dims=["lon"])

        westMN = feat_xr.sel(
            {
                "lat": tgt_lat,
                "lon": tgt_lon
            }
        ).drop("time_bounds")

        left_bin = westMN.time[np.arange(0, westMN.dims["time"], 3)].to_numpy()

        sum_vars = [
            "BEDD",  # Biologically effective degree days
            "FD",  # Frost days
            "ID",  # Ice days,
            "R10mm",  # Heavy precipitation days
            "R20mm",  # Very heavy preciptation days
            "RR",  # Precip sum
            "RR1",  # Wet days
            "SU",  # Summer days
            "TR",  # Tropical nights - a big fat 0 for Minnesota!
        ]

        max_vars = [
            "TNx",  # Max val of the daily min temp
            "TXx",  # Max val of daily max temp
        ]

        min_vars = [
            "TNn",  # Max val of the daily min temp
            "TXn",  # Max val of daily max temp
        ]

        mean_vars = [
            "SDII", # Simple daily intensity index (Mean precip on wet days)
            "TG", # Mean of daily mean temperature 
            "TN",  # Mean of daily min temp
            "TX",  # Mean of daily max temp
            "DTR",  # Mean of diurnal temperature range
        ]

        if var in sum_vars:
            aggWestMN = westMN.groupby_bins("time", left_bin).sum(
                dim=["time", "lat", "lon"]
            )
        elif var in max_vars:
            aggWestMN = westMN.groupby_bins("time", left_bin).max(
                dim=["time", "lat", "lon"]
            )
        elif var in min_vars:
            aggWestMN = westMN.groupby_bins("time", left_bin).min(
                dim=["time", "lat", "lon"]
            )
        elif var in mean_vars:
            aggWestMN = westMN.groupby_bins("time", left_bin).mean(
                dim=["time", "lat", "lon"]
            )
        else:
            raise ValueError("Variable " + var + " has no defined aggregation!")

        aggWestMN = aggWestMN.to_dataframe()

        aggWestMN.loc[:, "feature"] = var
        aggWestMN.loc[:, "scenario"] = scenario

        aggWestMN.to_csv(out_csv, mode="a", header=False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("download_dir", type=str)
    parser.add_argument("--out_csv", type=str, required=False, default="CMIP5_Agro.csv")

    args = parser.parse_args()

    ingest_cmip5(args.download_dir, args.out_csv)
