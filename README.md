# Chipseq Workflow analysis pipeline

Workflow for analyze ChIP-seq data. This is a python implementation of the
previous bash-command version.

## References and tools

1. fastQC
2. TrimGalore
3. Bowtie2
4. Samtools
5. picardTools
6. macs2
7. R
    1. ChIPQC
    2. DiffBind
    3. ChIPseeker
    4. DROMPAPLUS (for visualization of peaks)

## Repository structure

```
chipseq-workflow_py/
├── code
├── data
├── docker
├── jupyter_notebooks
└── outputs
```

Where:
- __code:__ Folder to save all the pipeline scripts in python
- __data:__ The input data to analyze should be placed or linked to this folder
- __docker:__ Here are the files related to create and run the pipeline using Docker 
- __jupyter_notebooks:__ Any jupyter notebook related to the repository
- __outputs:__ The output's pipeline will be stored and organized here

## Authors
* Alejandro Blanco  |  email: ablancomu@gmail.com
* Cristopher Fierro |  email:fierrocristopher@gmail.com

