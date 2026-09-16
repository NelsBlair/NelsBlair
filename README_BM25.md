# Pure NumPy BM25 Lexical Ranking Engine

A single-file, zero-dependency implementation of the Okapi BM25 ranking algorithm coded entirely by hand using fundamental linear algebra operations in NumPy.

## 📐 The Mathematics Behind the Search
This script skips high-level search index wrappers to isolate the deterministic term-weighting core:

$$\text{score}(D, Q) = \sum_{i=1}^{n} \text{IDF}(q_i) \cdot \frac{f(q_i, D) \cdot (k_1 + 1)}{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}$$

- **IDF Tuning:** Uses smoothing bounds to handle keyword sparsity without causing negative weights.
- **Length Normalization ($b=0.75$):** Scales document penalty strictly against relative document lengths.

## 🚀 Execution
```bash
pip install numpy
python bm25_scratch.py
```
