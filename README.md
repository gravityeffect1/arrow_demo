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

---

##  Features

-  Live genomic retrieval from NCBI using accession numbers
-  Region-specific targeting (ideal for the Spike protein or any ORF)
-  Customizable filtering:
  - Guide length (20–40 nt)
  - GC content range
  - Max homopolymer length (e.g., AAAA)
-  Randomized output to avoid bias
-  Data output includes nucleotide position, GC content, and inferred amino acid frame
-  Downloadable CSV for lab-ready documentation
-  Interactive web app powered by [Streamlit](https://streamlit.io)

---

## Example Use Case

Targeting the Spike protein of SARS-CoV-2:

- Accession: `NC_045512.2`
- Target region: nucleotides `21563–25384`
- Guide length: `28 nt`
- GC content: `30% – 70%`
- Max homopolymer: `4`
- Output: `50` guide RNAs, ready for synthesis or modeling

---
## Why ARROW?
Unlike most existing tools designed for DNA-targeting CRISPR systems (e.g., Cas9), ARROW is optimized specifically for Cas13-based RNA targeting. It enables direct retrieval of SARS-CoV-2 genomic data from NCBI, supports precise region selection (e.g., Spike gene), and applies customizable filters for guide length, GC content, and homopolymer avoidance. Built with transparency and reproducibility in mind, ARROW is an open-source, modular platform tailored to virological applications and rapid prototyping in RNA-guided CRISPR research.

## 📸 Screenshots


![ARROW Streamlit App](screenshots)

##  Contact
Developed with ❤️ by Sara Sova
MS1 · UMF Carol Davila
📧 Email: jaquesadit7@gmail.com
---
##  Built With

- [Streamlit](https://streamlit.io) – Interactive Python apps for data science and bioinformatics
- [Biopython](https://biopython.org) – Bioinformatics library for NCBI integration
- [pandas](https://pandas.pydata.org) – Data analysis and tabular guide export

## ⚙️ Installation & Usage

### ▶ Run Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/arrow.git
cd arrow

2. Create and activate a virtual environment ):

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install dependencies:



pip install -r requirements.txt

4. Launch the app:

streamlit run streamlit_app.py

! Requirements
 -Python ≥ 3.9

 -Streamlit

 -Biopython

 -pandas

Install with:

pip install streamlit biopython pandas





