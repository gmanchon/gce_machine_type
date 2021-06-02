
import pandas as pd

import os
import subprocess


# store csv at package location
data_file_path_fwf = os.path.join(
    os.path.dirname(__file__),
    "gce_machine_types.fwf"
)

# csv path
data_file_path_csv = os.path.splitext(data_file_path_fwf)[0] + ".csv"


def fetch_machine_types():
    """
    retrieve machine type from gcloud
    """

    # open file for writing
    with open(data_file_path_fwf, "w") as file:

        # retrieve the list of machine types
        subprocess.call([
            "gcloud",
            "compute",
            "machine-types",
            "list",
            "--quiet"],
            stdout=file)

    # convert fixed width format to csv
    df = pd.read_fwf(data_file_path_fwf, widths=[18, 27, 6, 11, 100])
    df.to_csv(data_file_path_csv, index=False)


def list_machine_types(by=None, ascending=None, verbose=True, **kwargs):
    """
    display retrieved machine types
    """

    # load the data
    df = pd.read_csv(data_file_path_csv)

    # column params
    column_params = dict(
        zone="ZONE",
        cpu="CPUS",
        memory="MEMORY_GB")

    # sort params
    sort_params = dict()

    # convert sort by params
    if by is not None:
        by = by.split(",")
        by = [column_params[col] for col in by]

    # convert sort ascending params
    if ascending is not None:
        ascending = ascending.split(",")
        ascending = [v == "true" for v in ascending]
        sort_params["ascending"] = ascending

    # iterate through filters
    for column, value in kwargs.items():

        print(column, value, column_params[column])
        df = df[df[column_params[column]] == value]

    # show all rows
    pd.set_option("display.max_rows", None)

    # checking whether dictionary is empty
    if by is not None:
        df.sort_values(by, **sort_params, inplace=True)

    if verbose:
        print(df)

    return df


if __name__ == '__main__':

    # fetch_machine_types()

    list_machine_types(
        zone="europe-west1-b",
        cpu=4,
        by="memory,cpu",
        ascending="false,true")
