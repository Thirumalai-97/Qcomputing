from qiskit import *
import matplotlib.pyplot as plt
import numpy as np 

# defining oracle 
oracle = QuantumCircuit(2, name='Oracle')
oracle.cz(0,1)
oracle.to_gate()
oracle.draw()


backend = Aer.get_backend('statevector_simulator')
grover_circ=QuantumCircuit(2,2)
grover_circ.h([0,1])
grover_circ.append(oracle,[0,1])
grover_circ.draw()

# defining reflection 
reflection = QuantumCircuit(2, name="Reflection")
reflection.h([0,1])
reflection.z([0,1])
reflection.cz(0,1)
reflection.h([0,1])
reflection.to_gate()

reflection.draw()

#adding everything to circuit 
backend = Aer.get_backend('statevector_simulator')
grover_circ.append(reflection, [0,1])
grover_circ.draw()

grover_circ.measure([0,1],[0,1])
grover_circ.draw()


# getting result in one shot
job = execute(grover_circ, backend, shots=1)
result= job.result()
result.get_counts()
