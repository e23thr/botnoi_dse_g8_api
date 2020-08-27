import numpy as np
import pandas as pd
import pathlib
import os


def get_team_df():
    # data_file = pathlib.Path(__file__).parent.absolute()
    data_file = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "templates", "team-data.csv"))  # {project_path}/static/team-data.csv
    data = pd.read_csv(data_file)
    # clean up
    data = data.replace(np.nan, '', regex=True)
    return data
