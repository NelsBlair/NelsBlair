# High-Dimensional Generalized Method of Moments (GMM) Estimator

A structural econometric simulation engine running two-step optimal GMM optimization loops over endogenous multi-variable fields using matrix algebra.

## 📐 Econometric Architecture
The program bypasses macro-level statistics wrappers to isolate simultaneous structural parameters where regressors correlate directly with the disturbance terms ($E[X\epsilon] \neq 0$):

$$\hat{\beta}_{GMM} = \arg\min_{\beta} \left( \frac{1}{N} Z^T(Y - X\beta) \right)^T W \left( \frac{1}{N} Z^T(Y - X\beta) \right)$$

- **Step 1:** Initial parameter sizing using an identity matrix configuration ($W = I$).
- **Step 2:** Sphericity mapping to calculate the optimal variance-covariance weighting cluster ($W = \Omega^{-1}$).

## 🚀 Execution
```bash
pip install numpy scipy
python econometric_gmm.py
```
