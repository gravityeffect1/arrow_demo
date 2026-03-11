#  ARROW: Automated RNA Recognition and Optimization Workflow

**A CRISPR-Cas13 gRNA design platform targeting SARS-CoV-2**  
Developed with science,  code, and  purpose.

---

## Overview

ARROW is a computational tool designed to streamline the design of guide RNAs (gRNAs) for RNA-targeting CRISPR-Cas13 systems. It specifically targets the SARS-CoV-2 genome, empowering researchers to define regions of interest (e.g., the spike protein), filter gRNAs based on customizable design criteria, and export high-confidence candidates for downstream experimental use.

Whether you're developing diagnostic assays, gene silencing strategies, or just nerding out in virology and molecular biology, ARROW is your starting point.

---

## Scientific Background

The COVID-19 pandemic underscored the global need for programmable, adaptive antiviral technologies. Among them, CRISPR-Cas13 stands out for its ability to cleave RNA sequences with high specificity. However, the efficacy of Cas13-based interventions hinges critically on the design of optimal guide RNAs.

ARROW addresses this challenge by:

- Allowing direct retrieval of SARS-CoV-2 genomic data via NCBI GenBank
- Extracting user-specified genomic segments (e.g., spike gene)
- Generating gRNA candidates filtered by GC content, homopolymer length, guide length, and amino acid frame alignment
- Offering reproducible, randomized outputs suitable for experimental pipelines



