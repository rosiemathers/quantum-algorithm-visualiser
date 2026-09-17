import numpy as np


def zero_state():
    return np.array([1, 0], dtype=complex)

def one_state():
    return np.array([0, 1], dtype=complex)

def x_gate():
    return np.array([
        [0, 1],
        [1, 0]
    ], dtype=complex)

def apply_gate(gate, state):
    return gate @ state

def h_gate():
    return (1 / np.sqrt(2)) * np.array([
        [1, 1],
        [1, -1]
    ], dtype=complex)

def probabilities(state):
    return np.abs(state) **2

def measure(state):
    probabilities = np.abs(state) ** 2
    return np.random.choice(len(state), p=probabilities)


from quantum import zero_state, h_gate, apply_gate, probabilities, measure

qubit = zero_state()

qubit = apply_gate(h_gate(), qubit)

# print("State:")
# print(qubit)

# print("Probabilities:")
# print(probabilities(qubit))

results = []

for _ in range(1000):
    results.append(measure(qubit))

class QuantumState:

    def __init__(self, state):
        self.state = state

    @classmethod
    def zero(cls):
        return cls(zero_state())

    def apply(self, gate):
        self.state = apply_gate(gate, self.state)

    def probabilities(self):
        return probabilities(self.state)

    def measure(self):
        return measure(self.state)