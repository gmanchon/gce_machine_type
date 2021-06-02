
import pandas as pd

import os
import subprocess


def fetch_machine_types():

    # store csv at package location
    data_file_path_fwf = os.path.join(
        os.path.dirname(__file__),
        "gce_machine_types.fwf"
    )

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

    # csv path
    data_file_path_csv = os.path.splitext(data_file_path_fwf)[0] + ".csv"

    # convert fixed width format to csv
    df = pd.read_fwf(data_file_path_fwf, widths=[18, 27, 6, 11, 100])
    df.to_csv(data_file_path_csv, index=False)


def list_machine_types():
    pass


if __name__ == '__main__':
    fetch_machine_types()
