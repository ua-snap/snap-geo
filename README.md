# SNAP Geo

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ua-snap/snap-geo/HEAD)

A repository of geospatial programming examples and operations commonly used at SNAP and with SNAP data. Click the Binder icon above to explore these Jupyter notebooks interactively (note, some of the data required by the notebooks will not be available there yet).

# Environments

There are two conda environment files in here: `chinook_env.yml` and `env_from_history.yml`. The `chinook_env.yml` file has the actual environment specification for creating the environment on Chinook, and hopes to serve as a "unified" geospatial processing environment (build strings are ommitted because the conda channels to update/remove them over time). The `env_from_history.yml` is a generic version of the environment, which should be useful for recreating it on MacOS or Windows as needed. Note, there are no versions pinned in this file! 

Note, if the environment solving seems to be taking a long time, try making sure conda is up to date with `conda update conda`. 
