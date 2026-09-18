import numpy as np
from scipy.linalg import expm

class QuantumStateEvolution:
    """
    A mathematical framework modeling state transformations and 
    decoherence using density matrices and Hamiltonian evolution.
    """
    def __init__(self):
        # Pauli Matrices
        self.I = np.eye(2, dtype=complex)
        self.X = np.array([[0, 1], [1, 0]], dtype=complex)
        self.Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
        self.Z = np.array([[1, 0], [0, -1]], dtype=complex)

    def generate_initial_density_matrix(self):
        """Creates a pure state |0><0| density matrix."""
        psi = np.array([1, 0], dtype=complex)
        return np.outer(psi, psi.conj())

    def evolve_state(self, rho, t, omega=1.0):
        """
        Evolves the density matrix under a simple Z-basis Hamiltonian.
        H = (omega / 2) * Z. Uses matrix exponential expm(-i * H * t).
        """
        H = (omega / 2.0) * self.Z
        U = expm(-1j * H * t)
        return U @ rho @ U.conj().T

    def apply_decoherence(self, rho, gamma=0.1):
        """
        Applies a phase-damping channel (decoherence) to the state matrix,
        attenuating off-diagonal elements over a discrete step.
        """
        damping_matrix = np.array([[1, np.sqrt(1 - gamma)], 
                                   [np.sqrt(1 - gamma), 1]], dtype=complex)
        return rho * damping_matrix

if __name__ == "__main__":
    simulator = QuantumStateEvolution()
    rho_0 = simulator.generate_initial_density_matrix()
    
    # Put into a superposition state using a pseudo-Hadamard transformation
    rho_superposition = 0.5 * np.array([[1, 1], [1, 1]], dtype=complex)
    
    print("Simulating Quantum State Transformation & Decoherence...")
    evolved = simulator.evolve_state(rho_superposition, t=np.pi/4)
    decayed = simulator.apply_decoherence(evolved, gamma=0.3)
    
    print("\nInitial Superposition Density Matrix:")
    print(rho_superposition)
    print("\nEvolved and Decohered Matrix (Loss of Off-Diagonal Coherence):")
    print(np.round(decayed, 4))
