FROM ubuntu:latest
MAINTAINER ablancomu@gmail.com

RUN apt update && apt install -y software-properties-common 
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'

RUN apt update -y && apt install -y \
    wget \
    unzip \
    curl \
    pigz \
    libssl-dev \
    libxml2-dev \
    libcurl4-openssl-dev \
    librsvg2-dev \
    libv8-dev \
    default-jre \
    fastqc \
    bowtie2 \
    cutadapt \
    samtools \
    python3-pip \
    r-base


RUN mkdir /home/software

# Trimgalore
WORKDIR /home/software
RUN curl -fsSL https://github.com/FelixKrueger/TrimGalore/archive/0.6.6.tar.gz -o trim_galore.tar.gz
RUN tar -xzvf trim_galore.tar.gz
ENV PATH=/home/software/TrimGalore-0.6.6:$PATH

# Picard
RUN wget https://github.com/broadinstitute/picard/releases/download/2.23.8/picard.jar
RUN echo -e '#!/bin/bash\necho $PWD\njava -jar /home/software/picard.jar' > picard && chmod +x picard
ENV PATH=/home/software:$PATH

# MACS2
RUN pip3 install macs2

# R packages
RUN echo "if ("'!'"requireNamespace(\"BiocManager\", quietly = TRUE)) install.packages(\"BiocManager\") ; BiocManager::install(\"ChIPQC\")" | R --no-save
RUN echo "if ("'!'"requireNamespace(\"BiocManager\", quietly = TRUE)) install.packages(\"BiocManager\") ; BiocManager::install(\"ChIPseeker\")" | R --no-save
RUN echo "if ("'!'"requireNamespace(\"BiocManager\", quietly = TRUE)) install.packages(\"BiocManager\") ; BiocManager::install(\"TxDb.Hsapiens.UCSC.hg38.knownGene\")" | R --no-save
RUN echo "if ("'!'"requireNamespace(\"BiocManager\", quietly = TRUE)) install.packages(\"BiocManager\") ; BiocManager::install(\"TxDb.Mmusculus.UCSC.mm10.knownGene\")" | R --no-save



