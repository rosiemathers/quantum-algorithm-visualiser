from quantum import QuantumState, h_gate

qubit = QuantumState.zero()

print("Initial state:")
print(qubit.state)

qubit.apply(h_gate())

print("After Hadamard:")
print(qubit.state)

print("Probabilities:")
print(qubit.probabilities())

print("Measurement:")
print(qubit.measure())