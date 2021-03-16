#!/usr/bin/env python
#
# Module to run fastQC on fastq files.
# Author: Alejandro Blanco
#
# Inputs: 
#   - Input folder with the fastq files 
#   - Output folder
#   - fastq extension (.fastq.gz, .fastq, .fq, .fq.gz)
#-----------------------------------------------------------------

# Import libraries
import sys
import argparse
import glob
import pathlib
import os
import shutil
import subprocess
import json

# Function to run fastQC
def fastQC(input_dir, output_dir, fq_ext):
    ## Create outdir 
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
    # Create tmp folder
    pathlib.Path(os.path.join(output_dir,'tmp_dir')).mkdir(parents=True, exist_ok=True)
    
    # Get list of fastq files
    fastq_files = os.listdir(input_dir)
    fastq_files = [ os.path.join(input_dir, x) for x in fastq_files if x.endswith(fq_ext) ]
    
    # Run fastqc
    cmd = ["fastqc", "-o", output_dir, "--format", "fastq", "--threads", str(len(fastq_files)), "--dir", os.path.join(output_dir,'tmp_dir')]
    ## Add fastq files to the command
    cmd.extend(fastq_files)
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    print(output)
    
    # Delete tmp_dir
    shutil.rmtree(os.path.join(output_dir,'tmp_dir'))



