# Quantum Decoherence & State Evolution Tool

A mathematical framework modeling closed-system Hamiltonian evolution and open-system phase-damping decoherence channels utilizing NumPy matrix exponentials.

## 📐 Mathematical Formulation
The framework evaluates unitary state evolution via the Liouville-von Neumann equation alongside discrete non-unitary kraus-operators for phase attenuation:

$$\rho(t) = e^{-iHt/\hbar}\rho(0)e^{iHt/\hbar}$$

The off-diagonal elements of the density matrix $\rho$ decay exponentially, tracking information leakage from the core system into a high-dimensional noisy environment—a direct analogue to multi-state systemic shock modeling in complex asset structures.

## 🚀 Execution
```bash
pip install numpy scipy
python quantum_state_evolution.py
```
