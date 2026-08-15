<div align="center">

# 🧬 DNA Sequence Analyzer

<p>
  <strong>A Python-based bioinformatics tool for analyzing DNA sequences</strong>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Bioinformatics-DNA%20Analysis-green" alt="Bioinformatics">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
</p>

</div>

---

## 📌 Overview

The <strong>DNA Sequence Analyzer</strong> is a beginner-friendly Python project designed to perform basic analysis of DNA sequences.

The project demonstrates how <strong>Python programming can be applied to biotechnology and bioinformatics</strong> to analyze biological DNA sequences.

The tool accepts a DNA sequence from the user and provides useful information such as sequence length, nucleotide composition, GC content, AT content, complementary sequence, and reverse complement.

---

## ✨ Features

<table>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>🧬 DNA Input</td>
<td>Accepts DNA sequences from the user</td>
</tr>

<tr>
<td>✅ Sequence Validation</td>
<td>Checks whether the sequence contains valid DNA nucleotides</td>
</tr>

<tr>
<td>📏 Sequence Length</td>
<td>Calculates the total number of nucleotides</td>
</tr>

<tr>
<td>🔢 Nucleotide Count</td>
<td>Counts A, T, G and C bases</td>
</tr>

<tr>
<td>🧪 GC Content</td>
<td>Calculates the percentage of G and C nucleotides</td>
</tr>

<tr>
<td>🧪 AT Content</td>
<td>Calculates the percentage of A and T nucleotides</td>
</tr>

<tr>
<td>🔄 Complement</td>
<td>Generates the complementary DNA sequence</td>
</tr>

<tr>
<td>🔁 Reverse Complement</td>
<td>Generates the reverse complement sequence</td>
</tr>

</table>

---

## 🧠 Bioinformatics Concepts

### 🧬 DNA Nucleotides

DNA contains four major nucleotides:

<table>
<tr>
<th>Nucleotide</th>
<th>Symbol</th>
<th>Complement</th>
</tr>

<tr>
<td>Adenine</td>
<td>A</td>
<td>T</td>
</tr>

<tr>
<td>Thymine</td>
<td>T</td>
<td>A</td>
</tr>

<tr>
<td>Guanine</td>
<td>G</td>
<td>C</td>
</tr>

<tr>
<td>Cytosine</td>
<td>C</td>
<td>G</td>
</tr>

</table>

### Base Pairing

DNA follows complementary base pairing:

<pre>
A ↔ T
G ↔ C
</pre>

For example:

<pre>
Original:
ATGCGT

Complement:
TACGCA
</pre>

---

## 🧪 GC Content

GC content represents the percentage of <strong>Guanine (G)</strong> and <strong>Cytosine (C)</strong> bases present in a DNA sequence.

<pre>
GC Content = (G + C) / Total Length × 100
</pre>

---

## 🧪 AT Content

AT content represents the percentage of <strong>Adenine (A)</strong> and <strong>Thymine (T)</strong> bases present in a DNA sequence.

<pre>
AT Content = (A + T) / Total Length × 100
</pre>

---

## 🛠️ Technologies Used

<ul>
<li>🐍 Python 3</li>
<li>Python Strings</li>
<li>Python Functions</li>
<li>Loops</li>
<li>Conditional Statements</li>
<li>Dictionaries</li>
<li>Mathematical Calculations</li>
<li>Basic Bioinformatics Concepts</li>
</ul>

---

## 📂 Project Structure

<pre>
DNA-SEQUENCE-ANALYZER/
│
├── dna_analyzer.py
├── README.md
└── .gitignore
</pre>

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python version:

<pre>
python --version
</pre>

---

## 📥 Installation

### 1️⃣ Clone the Repository

<pre>
git clone https://github.com/Anupam22327/DNA-SEQUENCE-ANALYZER.git
</pre>

### 2️⃣ Navigate to the Project Directory

<pre>
cd DNA-SEQUENCE-ANALYZER
</pre>

### 3️⃣ Run the Program

<pre>
python dna_analyzer.py
</pre>

---

## 💻 Example

### Input

<pre>
Enter DNA sequence: ATGCGTACGTA
</pre>

### Output

<pre>
DNA Sequence: ATGCGTACGTA

Sequence Length: 11

Nucleotide Count:
A: 3
T: 3
G: 3
C: 2

GC Content: 45.45%
AT Content: 54.55%

Complement: TACGCATGCAT
Reverse Complement: TACGTACGCAT
</pre>

<p>
<strong>Note:</strong> The output depends on the DNA sequence entered by the user.
</p>

---

## 🔬 How It Works

<div align="center">

<pre>
       DNA Sequence
             ↓
       User Input
             ↓
    Sequence Validation
             ↓
     Calculate Length
             ↓
    Count Nucleotides
             ↓
 Calculate GC & AT Content
             ↓
 Generate Complement
             ↓
Generate Reverse Complement
             ↓
      Display Results
</pre>

</div>

---

## 🎯 Project Goals

<ul>
<li>Improve Python programming skills</li>
<li>Understand basic DNA sequence analysis</li>
<li>Connect programming with biotechnology</li>
<li>Practice computational thinking</li>
<li>Build a foundation in bioinformatics</li>
<li>Develop practical programming projects using biological data</li>
</ul>

---

## 📈 Future Improvements

The project can be expanded with more advanced bioinformatics features.

<table>
<tr>
<th>Status</th>
<th>Planned Feature</th>
</tr>

<tr>
<td>⬜</td>
<td>FASTA file support</td>
</tr>

<tr>
<td>⬜</td>
<td>Multiple DNA sequence analysis</td>
</tr>

<tr>
<td>⬜</td>
<td>DNA → RNA transcription</td>
</tr>

<tr>
<td>⬜</td>
<td>RNA → Protein translation</td>
</tr>

<tr>
<td>⬜</td>
<td>Codon analysis</td>
</tr>

<tr>
<td>⬜</td>
<td>Open Reading Frame (ORF) detection</td>
</tr>

<tr>
<td>⬜</td>
<td>Mutation detection</td>
</tr>

<tr>
<td>⬜</td>
<td>Sequence alignment</td>
</tr>

<tr>
<td>⬜</td>
<td>Restriction enzyme analysis</td>
</tr>

<tr>
<td>⬜</td>
<td>Sequence visualization</td>
</tr>

<tr>
<td>⬜</td>
<td>Biopython integration</td>
</tr>

<tr>
<td>⬜</td>
<td>Graphical User Interface</td>
</tr>

<tr>
<td>⬜</td>
<td>Web-based DNA Sequence Analyzer</td>
</tr>

</table>

---

## 🧬 Future Development

The project can eventually be developed into a more advanced bioinformatics application.

<pre>
Python
   ↓
NumPy
   ↓
Pandas
   ↓
Biopython
   ↓
Matplotlib
   ↓
Machine Learning
   ↓
Web Application
</pre>

This could allow the project to perform advanced sequence analysis, visualization, and biological data processing.

---

## 📚 What I Learned

Through this project, I practiced:

<ul>
<li>Python programming</li>
<li>Functions</li>
<li>Loops</li>
<li>Conditional statements</li>
<li>String manipulation</li>
<li>Dictionaries</li>
<li>Mathematical calculations</li>
<li>Input validation</li>
<li>DNA sequence analysis</li>
<li>Applying programming to biotechnology</li>
</ul>

---

## 🌱 Why This Project?

As a <strong>Biotechnology student interested in Bioinformatics and Computational Biology</strong>, I wanted to build a project that combines biological concepts with programming.

This project represents one of my first steps toward learning how computational tools can be used to solve problems in biology.

---

## 👨‍💻 Author

<div align="center">

### Anupam Gautam

BTech Biotechnology Student

<p>
🧬 Bioinformatics &nbsp; • &nbsp;
💻 Python &nbsp; • &nbsp;
🧪 Computational Biology &nbsp; • &nbsp;
📊 Data Science &nbsp; • &nbsp;
🤖 AI & Machine Learning
</p>

</div>

---

## 📄 License

This project is available for <strong>educational and learning purposes</strong>.

You are welcome to use, modify, and improve the project for learning and development.

---

<div align="center">

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

<br>

<strong>Thanks for visiting! 🧬🐍</strong>

</div>
