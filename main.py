from quantum import QuantumState, h_gate

def main():
    qubit = QuantumState.zero()

    print("=== Quantum Algorithm Visualiser ===\n")

    print("Initial state:")
    print(qubit.state)

    qubit.apply(h_gate())

    print("\nAfter Hadamard gate:")
    print(qubit.state)

    print("\nMeasurement probabilities:")
    probabilities = qubit.probabilities()

    for i, probability in enumerate(probabilities):
        print(f"|{i}>: {probability:.2%}")

    print("\nMeasurement:")
    result = qubit.measure()
    print(f"Measured state: |{result}>")
    print("\nRunning 1000 measurements...")
    results = [qubit.measure() for _ in range(1000)]
    print(f"|0> measured: {results.count(0)} times")
    print(f"|1> measured: {results.count(1)} times")


if __name__ == "__main__":
    main()
