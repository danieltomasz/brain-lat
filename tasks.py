"""
File to run the pipeline.
Author: Daniel Borek, July 2023
"""

from pathlib import Path
import invoke

VARS = "PYDEVD_DISABLE_FILE_VALIDATION=1"
ENV = "3.12.2"
VENV = "brainlat-3.12.2"
PYTHON = f"~/.pyenv/versions/{ENV}/envs/{VENV}/bin/python"


def run_notebook(c, notebook):
    """Runs a Jupyter notebook."""
    if Path(notebook).is_file():
        c.run(
            f"{VARS} {PYTHON} -m  jupyter nbconvert \\"
            f"--to notebook --execute {notebook} --inplace"
        )
    else:
        print(f"Notebook {notebook} does not exist.")


@invoke.task
def download_data(c):
    """
    Downloads data from Synapse.
    """
    c.run(f"{VARS} {PYTHON}  scripts/01_download-data.py")


@invoke.task
def dataset_overview(c):
    """
    Loads and converts PSD data to dataarray form from via Jupyter notebook.
    """
    if Path("/Volumes/T7/BrainLat").exists():
        notebook = "notebooks/00_Dataset_overview.ipynb"
        run_notebook(c, notebook)

@invoke.task
def check_subject(c):
    """
    Loads and converts PSD data to dataarray form from via Jupyter notebook.
    """
    if Path("/Volumes/T7/BrainLat").exists():
        notebook = "notebooks/01_Plot_subject.ipynb"
        run_notebook(c, notebook)


# Entire pipeline
@invoke.task
def run_all(c):
    """
    Runs the entire pipeline.
    """
    dataset_overview(c)
    check_subject(c)

