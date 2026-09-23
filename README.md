# Quantum Algorithm Visualiser

A Python-based quantum computing project that simulates and visualises
basic quantum states, gates, probabilities and measurements.

I was motivated to work on this project to strengthen my understanding of quantum computing by implementing the underlying mathematics and quantum
operations in Python rather than relying entirely on existing quantum
computing libraries. I used AI to assist me with the code and explanations.

## Features

- Representation of single-qubit quantum states
- |0> and |1> basis states
- Pauli-X gate
- Hadamard gate
- Application of quantum gates using matrix multiplication
- Calculation of measurement probabilities
- Simulated quantum measurement
- Repeated measurements to demonstrate probabilistic behaviour

## How it works

A qubit is represented using a complex state vector.

For example:

|0> = [1, 0]

and

|1> = [0, 1]

Quantum gates are represented using matrices and applied using matrix
multiplication.

For example, the Hadamard gate is:

H = 1/sqrt(2) [[1, 1],
               [1, -1]]

Applying the Hadamard gate to |0> produces:

H|0> = 1/sqrt(2) (|0> + |1>)

This produces equal probabilities of measuring |0> or |1>.

## Example

Running the program produces output similar to:

Initial state:
[1.+0.j 0.+0.j]

After Hadamard gate:
[0.70710678+0.j 0.70710678+0.j]

Measurement probabilities:
|0>: 50.00%
|1>: 50.00%

Measurement:
Measured state: |1>

Because quantum measurement is probabilistic, the result will vary
between runs.

## Project Structure

```text
Quantum-Algorithm-Visualiser/
│
├── main.py
├── quantum.py
├── README.md
└── requirements.txt
