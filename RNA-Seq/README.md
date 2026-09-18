# 🧬 High-Dimensional RNA-Seq Manifold Learning & Classifying Pipeline

An advanced transcriptomic machine learning pipeline designed to systematically combat the "curse of dimensionality" in human RNA-sequencing datasets. This architecture surveys structural matrix decompositions and *a priori* biological groupings across **9 distinct clinical disease domains** (including Glioblastoma, HIV, Pediatric ALL, and Crohn's Disease) to optimize downstream diagnostic classification.

## 🔬 Scientific & Academic Context
This software pipeline serves as the production implementation supporting the broader transcriptomic structural survey, referencing methodologies highlighted in:
> **Survey of Dimensionality Reduction Techniques and their Applications for Classifying Disease State in Human RNA-seq Data**  
> *Academic Circle & Discussions:* [ResearchGate Publication Context](https://researchgate.net) (Collaborative validation mapping frameworks by Paul Ola and Roya Campos).

---

## 🛠️ System Architecture & ML Pipeline

The software processes high-dimensional gene expression matrices where features (p > 54,000) vastly outnumber observations (n < 200). 

### 1. Dimensionality Reduction Strategies
- **Strategy 1: Base State Baseline** (No modification control array).
- **Strategy 2: *A Priori* Biological Aggregation** (Functional feature mapping leveraging Gene Ontology (GO) categorization: Component, Function, and Process).
- **Strategy 3: Principle Component Analysis (PCA)** (Linear variance maximizer preserving dominant eigenspaces).
- **Strategy 4: Kernelized PCA (KPCA)** (Non-linear manifold mapping utilizing Radial Basis Function (RBF) kernels).
- **Strategy 5: Nonnegative Matrix Factorization (NMF)** (Additive, non-centered part-based representations optimized via 200-iteration convergence loops).

### 2. Downstream Classifier Array
Processed matrices are fed into an evaluation suite calculating diagnostic cross-validation profiles across:
*   Support Vector Machines (SVM)
*   Random Forest Classifiers (RF)
*   Decision Tree Estimators (DT)
*   Naïve Bayes Classifiers (NBC)
*   k-Nearest Neighbours (k-NN)

---

## 📂 Repository Topology
```text
├── Setup.py                  # Primary data preprocessing & manifold reduction driver
├── Functions.py              # Modular core mathematical & pipeline utilities
├── SupportVectorMachine.py   # Multi-class SVM execution array
├── RandomForest.py           # Ensemble random forest estimator array
├── NaiveBayes.py             # Probabilistic classifier execution array
├── kNearestNeighbours.py     # Instance-based spatial cluster engine
├── DecisionTree.py           # Deterministic recursive partition engine
├── Figures.R                 # Statistical validation & visualization generator (ggplot2)
├── Raw/                      # Compressed raw clinical datasets (.bz2 source formats)
└── Deliverables/             # Compiled LaTeX reports (NeurIPS layout template) & specifications
```

---

## 🚀 Deployment & Operational Pipeline

### 1. Environment Initialization
Ensure your system uses a dedicated environment (`Python 3.11+` recommended) containing standard numerical and machine learning stacks:
```bash
pip install numpy scikit-learn
```

### 2. Data Decompression
Extract the compressed clinical NCBI GEO archives (`.soft` format) located inside the `Raw/` directory using standard system tooling (`tar`, `7-zip`, or `bunzip2`):
```bash
cd Raw
bunzip2 *.bz2
```

### 3. Executing the Preprocessing Engine
Run the matrix initialization pipeline. This script ingests the raw data files, matches features against target annotations, executes the 5 manifold learning methods, and structures the reduced tensors:
```bash
python Setup.py
```

### 4. Running Model Surveys & Serialization
Execute any classifier script to test performance across the processed datasets. Results automatically save as standardized confusion matrices in JSON files:
```bash
python SupportVectorMachine.py
```

### 5. Statistical Visualizations
To generate publication-grade performance charts and compile the Hotelling T-squared distribution analytics:
```bash
Rscript Figures.R
```
