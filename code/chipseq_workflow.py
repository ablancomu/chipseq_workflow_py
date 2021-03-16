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
from multiprocessing import Pool, TimeoutError
import json
import re
# Pipeline modules
import fastqc
import bowtie2

# Function to process the arguments
def arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="Configuration file in json format" )
    #parser.add_argument("--")
    args = parser.parse_args()
    # Check if config file exist
    config_file = pathlib.Path(args.config_file)
    if config_file.exists ():
        return(args)
    else:
        sys.exit("ERROR: The file {} doesn't exists".format(args.config_file))

# Function to get a list with the sampleIDs to analyze
def get_ids(fastq_dir, fastq_ext):
    # Get list of fastq pathobject
    fastq_list = pathlib.Path(fastq_dir).rglob('*'+fastq_ext)
    # Get file names without extension
    fastq_list = [ x.name.strip(fastq_ext) for x in fastq_list ]
    # Remove _1/_2
    fastq_list = [re.sub(r'_\d', '', x) for x in fastq_list]
    # Get unique ids
    fastq_list = set(fastq_list)
    return(list(fastq_list))

if __name__== "__main__":
    # Read arguments
    arguments = arguments_parser()
    
    # Read the config_file
    with open(arguments.config_file) as jsonf:
        config_file = json.load(jsonf)
    
    # Get list of sampleIDs
    fastq_ids = get_ids(config_file['general']['fastq_dir'], config_file['general']['fastq_ext'])
    print('List of IDs to process: {}'.format(fastq_ids))

    # Execute fastQC
    fastqc.fastQC(config_file['general']['fastq_dir'], config_file['fastqc']['outdir'], config_file['fastqc']['fastq_ext'])

    # Execute Trimgalore
    ## Trim galore ...

    # Execute Bowtie2
    ## Get list of tuples [R1, R2, id, bowtie_threads, ref_index, output_dir]
    fastq_tuples = bowtie2.get_tuples(fastq_ids, config_file)
    print(fastq_tuples)
    ## Run Bowtie2
    with Pool(config_file['bowtie2']['threads']) as p:
        output = p.map(bowtie2.Bowtie2, fastq_tuples)










