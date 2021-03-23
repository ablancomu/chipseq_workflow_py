#!/usr/bin/env python
#
# Module to execute Drompaplus to generate a visualization file.
# Author: Alejandro Blanco
#
# Inputs:
#   - config_file in json
#--------------------------------------------------------------------------

import sys
import argparse
import glob
import pathlib
import os
import shutil
import subprocess
from multiprocessing import Pool, TimeoutError
import json
import re
import pandas as pd

# Function to convert BAM file to wig file using parse2wig+
def parse2wig():
    pass


# Function to read a datasheet from ChIPQC or DiffBind
def read_datasheet(config_file):
    # Read the data sheet
    df = pd.read_csv(config_file['drompaplus']['data_sheet'])

    
