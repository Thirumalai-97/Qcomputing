circuit=QuantumCircuit(2,2)
circuit.x(0)
circuit.x(1)
circuit.y(1)
circuit.z(0)
circuit.h(0)
circuit.h(0)
circuit.cx(0,1)
circuit.draw('mpl')
