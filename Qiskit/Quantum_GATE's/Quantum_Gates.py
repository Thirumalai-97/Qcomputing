circuit=QuantumCircuit(2,2)
circuit.x(0) # Pauli X GATE
circuit.x(1) 
circuit.y(1) # Pauli Y GATE
circuit.z(0) # Pauli Z GATE
circuit.h(0) # Hadamard GATE
circuit.h(0)
circuit.cx(0,1) # Controlled NOT GATE
circuit.draw('mpl')
