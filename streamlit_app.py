import streamlit as st
from Bio import Entrez, SeqIO
import pandas as pd
import random

# ===== Styling =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #ffffff;
    color: #000000;
}

body[data-theme="dark"], body[data-theme="dark"] .stApp {
    background-color: #121212 !important;
    color: #f0f0f0 !important;
}

body[data-theme="dark"] .stApp * {
    color: #f0f0f0 !important;
    background-color: transparent !important;
}

body[data-theme="dark"] .stMarkdown a {
    color: #80cbc4 !important;
    text-decoration: underline;
}

body[data-theme="dark"] input, 
body[data-theme="dark"] textarea, 
body[data-theme="dark"] select {
    background-color: #2c2c2c !important;
    color: #eaeaea !important;
    border: 1px solid #555 !important;
}

.sidebar .sidebar-content {
    background-color: #ececec;
    color: #1a1a1a;
    border-right: 1px solid #d0d0d0;
    transition: background-color 0.3s ease;
}

body[data-theme="dark"] .sidebar .sidebar-content {
    background-color: #1e1e1e !important;
    color: #eaeaea !important;
}

.stButton>button, .stDownloadButton>button {
    background-color: #005f73;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 0.5em 1em;
    transition: all 0.3s ease-in-out;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    font-size: 0.95rem;
}

.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: #0a9396;
    transform: scale(1.03);
}

.stDataFrame {
    background-color: inherit;
    color: inherit;
    border-radius: 6px;
    border: 1px solid #ccc;
    animation: slideIn 0.5s ease;
    font-size: 0.9rem;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slideIn {
    from { opacity: 0; transform: translateX(-20px); }
    to { opacity: 1; transform: translateX(0); }
}

h1 {
    font-size: 2.6em;
    text-align: center;
    margin-bottom: 1.5em;
    animation: fadeIn 1s ease;
}
</style>
""", unsafe_allow_html=True)

# ===== Title and Description =====
st.markdown("""
<h1>ARROW: A Computational Platform for Cas13 Guide RNA Design Targeting SARS-CoV-2</h1>
<p style="text-align: justify;">
ARROW (Automated RNA Recognition and Optimization Workflow) is a research-driven platform designed to assist scientists in generating optimized CRISPR-Cas13 guide RNAs against RNA viruses, with current focus on SARS-CoV-2. By integrating real-time genomic retrieval from NCBI and applying rigorous filtering criteria—including GC content, homopolymers, and region boundaries—ARROW enables efficient and customizable gRNA design.
</p>
<hr>
<h2>About ARROW</h2>
<p style="text-align: justify;">
This tool is ideal for researchers, virologists, and synthetic biologists engaged in RNA-targeted diagnostics or antiviral development. For source code and project updates, visit the <a href="https://github.com/gravityeffect1" target="_blank">official GitHub repository</a>.
</p>
<hr>
""", unsafe_allow_html=True)

# ===== Sidebar =====
with st.sidebar:
    st.header("Design Parameters")
    email = st.text_input("NCBI Email (required for data retrieval)", placeholder="Your email address")
    accession = st.text_input("NCBI Accession Number", value="NC_045512.2")
    region_start = st.number_input("Target Region Start (nt)", min_value=1, value=21563)
    region_end = st.number_input("Target Region End (nt)", min_value=region_start + 1, value=25384)
    guide_len = st.slider("Guide RNA Length (nt)", min_value=20, max_value=40, value=28)
    gc_min = st.slider("Minimum GC Content", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
    gc_max = st.slider("Maximum GC Content", min_value=0.0, max_value=1.0, value=0.7, step=0.01)
    homopolymer_len = st.slider("Maximum Homopolymer Length", min_value=2, max_value=10, value=4)
    n_guides = st.slider("Number of Guides to Generate", min_value=1, max_value=100, value=50)

# ===== Core Functions =====
def download_sars_cov2_genome(email, accession):
    Entrez.email = email
    try:
        with Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text") as handle:
            record = SeqIO.read(handle, "fasta")
        return str(record.seq).replace("T", "U")
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve genome: {e}")

def extract_region(rna_seq, start, end):
    if start < 1 or end > len(rna_seq):
        raise ValueError("Target region coordinates are out of range.")
    return rna_seq[start-1:end]

def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return gc_count / len(seq) if len(seq) > 0 else 0

def has_homopolymer(seq, max_len):
    return any(base * max_len in seq for base in 'AUCG')

def generate_grnas(rna_seq, guide_len, gc_min, gc_max, homopolymer_len, n_guides):
    candidates = []
    for i in range(len(rna_seq) - guide_len + 1):
        guide = rna_seq[i:i+guide_len]
        gc = gc_content(guide)
        if gc_min <= gc <= gc_max and not has_homopolymer(guide, homopolymer_len):
            candidates.append({
                'Nucleotide_Position': i + 1,
                'Guide_Sequence': guide,
                'GC_Content': round(gc, 3),
                'Approx_Amino_Acid_Position': (i // 3) + 1
            })
    random.shuffle(candidates)
    return candidates[:n_guides]

# ===== Main Interface =====
if st.button("Generate Guide RNAs"):
    if not email:
        st.error("Please enter your NCBI email address to proceed.")
    else:
        with st.spinner("Downloading and processing SARS-CoV-2 genome sequence..."):
            try:
                genome_rna = download_sars_cov2_genome(email, accession)
                target_region = extract_region(genome_rna, region_start, region_end)
                guides = generate_grnas(target_region, guide_len, gc_min, gc_max, homopolymer_len, n_guides)
                if guides:
                    df = pd.DataFrame(guides)
                    st.success(f"{len(guides)} guide RNAs successfully generated.")
                    st.markdown("""
                        <p style='text-align: justify;'>
                        Guide RNAs were filtered based on GC content, homopolymer avoidance, and location constraints. Each guide is annotated with nucleotide start, GC percentage, and approximate amino acid position.
                        </p>
                    """, unsafe_allow_html=True)
                    st.dataframe(df, use_container_width=True)
                    csv_data = df.to_csv(index=False).encode('utf-8')
                    st.download_button("Download as CSV", data=csv_data, file_name="ARROW_gRNA_candidates.csv", mime="text/csv")
                else:
                    st.warning("No valid guide RNAs found. Try adjusting your design parameters.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
