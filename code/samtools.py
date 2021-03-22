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
    sam_list = pathlib.Path(config_file['samtools']['sam_dir']).rglob('*/*'+config_file['samtools']['sam_ext'])
    # Transform to list
    sam_list = [x.as_posix() for x in sam_list]
    # create empty list to store sam files
    sam_tuples = []
    # search for each ID
    for id in ids:
        sam_tuples.append([id, config_file['samtools']['threads'], config_file['samtools']['outdir'], config_file['samtools']['sam_dir'], 0])
    return(sam_tuples)

# Function to run the Bowtie2 alingment
def Samtools(inputs):
    ## Create outdir 
    pathlib.Path(os.path.join(inputs[2], inputs[0])).mkdir(parents=True, exist_ok=True)
    option = inputs[4]
    #Set command for each option
    if option == 0:
        # Sam To Bam
        cmd = ["samtools", "view", 
        "--threads", str(inputs[1]), 
        "-bSo", os.path.join(inputs[2],inputs[0],inputs[0]+'.bam'),
        os.path.join(inputs[3],inputs[0],inputs[0]+'.sam')
          ]
    #Sort Bam
    elif option == 1:
        cmd = ["samtools", "sort",
        "--threads", str(inputs[1]),
        os.path.join(inputs[2],inputs[0],inputs[0]+'.bam'),
        "-o", os.path.join(inputs[2],inputs[0],inputs[0]+'_sorted.bam')
        ]
    #Index Bam
    elif option == 2:
        cmd = ["samtools", "index",
        "-@", str(inputs[1]),
        os.path.join(inputs[2],inputs[0],inputs[0]+'_sorted.bam')
        ]
    else:
        print("An error has ocurred")

    print(cmd)
    proc = subprocess.run(cmd, capture_output=True)
    return(proc)
