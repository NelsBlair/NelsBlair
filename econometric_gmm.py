import numpy as np
from scipy.optimize import minimize

class GMM_StructuralEstimator:
    """
    A hand-coded Generalized Method of Moments (GMM) estimator
    for a structural linear model with endogenous regressors and instrumental variables.
    """
    def __init__(self):
        self.beta = None
        self.vcov = None

    def simulate_data(self, N=500):
        """Simulates simultaneous-equation economic data with endogeneity."""
        np.random.seed(42)
        Z = np.random.normal(0, 1, (N, 2)) # 2 Instrumental Variables (Exogenous)
        v = np.random.normal(0, 0.5, N)
        u = 0.5 * v + np.random.normal(0, 0.5, N) # Structural error correlated with X
        
        # Endogenous regressor X driven by instruments Z and shared error v
        X = 1.2 * Z[:, 0:1] + 0.8 * Z[:, 1:2] + v.reshape(-1, 1)
        
        # True structural parameter beta = [2.5]
        Y = 2.5 * X.flatten() + u
        return Y, X, Z

    def moment_conditions(self, params, Y, X, Z):
        """Calculates orthogonal moment conditions: E[Z'u] = 0"""
        beta = params[0]
        u = Y - beta * X.flatten()
        # Downstream orthogonality conditions
        g = Z * u.reshape(-1, 1) 
        return np.mean(g, axis=0)

    def criterion_function(self, params, Y, X, Z, W):
        """GMM Objective function: J = g' * W * g"""
        g_bar = self.moment_conditions(params, Y, X, Z)
        return float(g_bar.T @ W @ g_bar)

    def fit(self, Y, X, Z):
        """Two-Step Optimal GMM Estimation Engine"""
        # Step 1: Identity Matrix Weighting
        W1 = np.eye(Z.shape[1])
        res1 = minimize(self.criterion_function, x0=[0.0], args=(Y, X, Z, W1), method='BFGS')
        beta_1 = res1.x[0]

        # Step 2: Compute Optimal Weighting Matrix (HAC-style variance of moments)
        u_hat = Y - beta_1 * X.flatten()
        g = Z * u_hat.reshape(-1, 1)
        W2 = np.linalg.inv((g.T @ g) / len(Y))

        # Final Optimization
        res2 = minimize(self.criterion_function, x0=[beta_1], args=(Y, X, Z, W2), method='BFGS')
        self.beta = res2.x[0]
        return self.beta

if __name__ == "__main__":
    estimator = GMM_StructuralEstimator()
    Y, X, Z = estimator.simulate_data(N=1000)
    
    print("Executing Hand-Coded Structural Econometric Simulator...")
    estimated_beta = estimator.fit(Y, X, Z)
    print(f"True Beta Parameter:  2.5000")
    print(f"GMM Estimated Beta:   {estimated_beta:.4f}")
