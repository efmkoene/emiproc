import os
import shutil
import subprocess

import netCDF4 as nc
import amrs.nc

import zipfile

import pytest

def test_performance_at_rlon():
    """\
    Execute processing case which has rlon==0. Hard-coded (in shell) to save
    effort of sending in all correct arguments otherwise...
    """

    # working directory
    cwd = os.path.dirname(__file__)

    with zipfile.ZipFile('test_emissions.zip', 'r') as zip_ref:
        zip_ref.extractall()

    # remove outputs from previous tests
    try:
        shutil.rmtree(os.path.join(cwd, 'outputs'))
    except FileNotFoundError:
        pass

    # run emiproc
    subprocess.run(["python", "-m", "emiproc", "grid", "--case-file",
                    "tno_rlon_test.py"], shell=False,
                    cwd=cwd)

    # compare output with reference
    out_filename = os.path.join(cwd, "outputs", "online", "outgrid.nc")
    out_filename_ref = os.path.join(cwd, "tno_ref.nc")

    with nc.Dataset(out_filename) as own, nc.Dataset(out_filename_ref) as ref:
        assert amrs.nc.compare.datasets_equal(own, ref, []) 