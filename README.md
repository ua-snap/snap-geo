# SNAP Geo

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ua-snap/snap-geo/HEAD)

A repository of geospatial programming examples and operations commonly used at SNAP and with SNAP data. Click the Binder icon above (experimental) to explore these Jupyter notebooks interactively (note, some of the data required by the notebooks will not be available there yet).

## Usage instructions

After cloning this repo, create a new `conda` environment from the `environment.yml` file:

```
conda env create -f environment.yml
```

Activate that environment and start Jupyter Lab:

```
conda activate snap-geo
jupyter lab
```

#### Using on Atlas

To use on one of the Atlas compute nodes, add the `--no-browser` flag, and specify a port number with `--port=<port number>` if desired (default is port 8888):

```
jupyter lab --no-browser --port=8887
```

and start port-forwarding on your local machine:

```
ssh -L 8887:localhost:8887 -N kmredilla@atlas<node number>.snap.uaf.edu
```
