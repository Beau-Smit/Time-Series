from multiprocessing.sharedctypes import Value
import numpy as np
import xarray as xr
import os
import argparse
import re

def ingest_cmip5(download_dir, out_dir, bin_lens = ['month', 'year']):
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

        n_grid_points = westMN.dims['lat'] * westMN.dims['lon']

        for bin_len in bin_lens:
            if bin_len == 'month':
                step = 3 #number of 10 day windows in a month
            elif bin_len == 'year':
                step = 36 #number of 10 day windows in a year
            bin_mask = np.arange(0, westMN.dims["time"] + step, step)
            bin_mask[-1] -= 1
            left_bin = westMN.time[bin_mask].to_numpy()

            if var in sum_vars:
                aggWestMN = westMN.groupby_bins("time", left_bin).sum(
                    dim=["time", "lat", "lon"]
                ) / n_grid_points
            elif var in max_vars:
                aggWestMN = westMN.groupby_bins("time", left_bin).max(
                    dim=["time", "lat", "lon"]
                ) / n_grid_points
            elif var in min_vars:
                aggWestMN = westMN.groupby_bins("time", left_bin).min(
                    dim=["time", "lat", "lon"]
                ) / n_grid_points
            elif var in mean_vars:
                aggWestMN = westMN.groupby_bins("time", left_bin).mean(
                    dim=["time", "lat", "lon"]
                ) / n_grid_points
            else:
                raise ValueError("Variable " + var + " has no defined aggregation!")

            aggWestMN = aggWestMN.to_dataframe().reset_index()\
                .rename(columns = {'index':'date_bin'})
            aggWestMN.loc[:, "year"] = \
                aggWestMN.date_bin.apply(lambda x: x.left.year)

            if bin_len == 'month':
                aggWestMN.loc[:, "month"] = \
                    aggWestMN.date_bin.apply(lambda x: x.left.month)

            aggWestMN.loc[:, "feature"] = var
            aggWestMN.loc[:, "scenario"] = scenario
            aggWestMN = aggWestMN.drop(columns='date_bin')

            out_csv = out_dir + "CMIP5_Agro_" + bin_len + ".csv"
            aggWestMN.to_csv(out_csv, mode="a", header=False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("download_dir", type=str)
    parser.add_argument("--out_dir", type=str, required=False, default="")

    args = parser.parse_args()

    ingest_cmip5(args.download_dir, args.out_dir)
