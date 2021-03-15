#!/usr/bin/env python
#
# Wrapper to execute the ChIPseq pipeline in python 3.
# Author: Alejandro Blanco
# e-mail: ablancomu@gmail.com
# v0.1
#
# Usage:
#       chipseq_pipeline.py [config_file.json]
# Where:
#       config_file.json : is a json file with common and tools specific parameters
#
#--------------------------------------------------------------------------

# Import libraries

import sys
import argparse
import glob
import pathlib
import os
import shutil
import subprocess
import json
# Pipeline modules
import fastqc

# Function to process the arguments
def arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="Configuration file in json format" )
    args = parser.parse_args()
    # Check if config file exist
    config_file = pathlib.Path(args.config_file)
    if config_file.exists ():
        return(args)
    else:
        sys.exit("ERROR: The file {} doesn't exists".format(args.config_file))

if __name__== "__main__":
    # Read arguments
    arguments = arguments_parser()
    
    # Read the config_file
    with open(arguments.config_file) as jsonf:
        config_file = json.load(jsonf)
    
    fastqc.fastQC(config_file['general']['fastq_dir'], config_file['fastqc']['outdir'])









