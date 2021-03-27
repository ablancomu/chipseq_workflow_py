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
    bam_tuples = []
    # search for each ID
    for id in ids:
        bam_tuples.append([id, config_file['markdups']['threads'], config_file['markdups']['outdir'],config_file['markdups']['picard'] ,config_file['markdups']['bam_dir'], 0])
    return(bam_tuples)

# Function to run the Bowtie2 alingment
def Markdups(inputs):
    ## Create outdir 
    pathlib.Path(os.path.join(inputs[2], inputs[0])).mkdir(parents=True, exist_ok=True)
    option = inputs[5]
    #Set command for each option
    if option == 0:
        # Reheader
        cmd = "samtools view -H "+os.path.join(inputs[4],inputs[0],inputs[0])+"_sorted.bam | sed 's/VN:\\t/VN:2.0\\t/g' | samtools reheader - "+os.path.join(inputs[4],inputs[0],inputs[0])+"_sorted.bam  > "+os.path.join(inputs[2],inputs[0],inputs[0])+'.bam'
        proc = subprocess.run(cmd, capture_output=True,shell=True)
        return(proc)
        #PICARD
    elif option == 1:
        pathlib.Path(os.path.join(inputs[2], inputs[0]+'_tmp')).mkdir(parents=True, exist_ok=True)
        cmd = ["java", "-jar", inputs[3],
        "MarkDuplicates", "-I", os.path.join(inputs[2],inputs[0],inputs[0]+'.bam'),
        "-O", os.path.join(inputs[2],inputs[0],inputs[0]+'_markdup.bam'),
        "-M", os.path.join(inputs[2],inputs[0],inputs[0]+'_markdup.metrics'),
        "--TMP_DIR", os.path.join(inputs[2],inputs[0]+'_tmp')
        ]
    elif option == 2:
        cmd = ["samtools", "index",
        "-@", str(inputs[1]),os.path.join(inputs[2],inputs[0],inputs[0]+'_markdup.bam'),
        ">",os.path.join(inputs[2],inputs[0],inputs[0]+'_markdup.stats'), 
        ]
    #Stats
    elif option == 3:
        cmd = ["samtools", "index",
        "-@", str(inputs[1]),
        os.path.join(inputs[2],inputs[0],inputs[0]+'_markdup.bam')
        ]
    elif option == 4:
        cmd = ["rm","-r",os.path.join(inputs[2],inputs[0]+'_tmp')]
    else:
        print("An error has ocurred")

    print("RUNNING:",cmd)
    proc = subprocess.run(cmd, capture_output=True)
    return(proc)
