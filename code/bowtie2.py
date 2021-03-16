#!/usr/bin/env python
#
# Module to execute bowtie2 on a paired end data.
# Author: Alejandro Blanco
#
# Inputs:
#   - 
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

# Function to get pairs of fastq files
def get_tuples(ids, config_file):
    # Get list of fastq pathobject
    fastq_list = pathlib.Path(config_file['bowtie2']['fastq_dir']).rglob('*'+config_file['bowtie2']['fastq_ext'])
    # Transform to list
    fastq_list = [x.as_posix() for x in fastq_list]
    # create empty list to store pairs of fastq
    fastq_tuples = []
    # search pairs for each sample ID
    for id in ids:
        pair = [ x for x in fastq_list if id in x]
        for fastq in pair:
            if '_1.' in fastq:
                R1=fastq
            elif '_2.' in fastq:
                R2=fastq
        fastq_tuples.append([R1, R2, id, config_file['bowtie2']['threads'], config_file['bowtie2']['ref_index'], config_file['bowtie2']['outdir'] ])
    return(fastq_tuples)

# Function to run the Bowtie2 alingment
def Bowtie2(inputs):
    ## Create outdir 
    pathlib.Path(os.path.join(inputs[5], inputs[2])).mkdir(parents=True, exist_ok=True)

    # Create command
    cmd = ["bowtie2", "-q", "--phred33",
           "-p", str(inputs[3]),
           "-x", inputs[4],
           "-1", inputs[0], "-2", inputs[1],
           "-S", os.path.join(inputs[5], inputs[2], inputs[2]+'.sam')
          ]
    print(cmd)
    proc = subprocess.run(cmd, capture_output=True)
    return(proc)
