import numpy as np

#this returns the |0> quantum state
def zero_state():
    return np.array([1, 0], dtype=complex)
#this returns the |1> quantum state
def one_state():
    return np.array([0, 1], dtype=complex)
#return the Pauli X gate
def x_gate():
    return np.array([
        [0, 1],
        [1, 0]
    ], dtype=complex)

#return the Hadamard gate
def h_gate():
    return (1 / np.sqrt(2)) * np.array([
        [1, 1],
        [1, -1]
    ], dtype=complex)

#then apply the quantum gate to a state
def apply_gate(gate, state):
    return gate @ state
#calculate probabilities of state
def probabilities(state):
    return np.abs(state) **2
#simulate measurement of the quantum state
def measure(state):
    probabilities = np.abs(state) ** 2
    return np.random.choice(len(state), p=probabilities)


# from quantum import zero_state, h_gate, apply_gate, probabilities, measure

# qubit = zero_state()

# qubit = apply_gate(h_gate(), qubit)

# # print("State:")
# # print(qubit)

# # print("Probabilities:")
# # print(probabilities(qubit))

# results = []

# for _ in range(1000):
    results.append(measure(qubit))

class QuantumState:

    def __init__(self, state):
        self.state = state

#create a cubit in the |0> state
    @classmethod
    def zero(cls):
        return cls(zero_state())
#create a cubit in the |1> state
    def one(cls):
        return cls(one_state())
#apply gate to quantum state
    def apply(self, gate):
        self.state = apply_gate(gate, self.state)
#return the probabilities 
    def probabilities(self):
        return probabilities(self.state)
#measure the quantum state
    def measure(self):
        return measure(self.state)