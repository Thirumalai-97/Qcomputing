from qiskit import *
%matplotlib inline
from qiskit.tools.visualization import plot_histogram
s='1010'

n= len(s)
circuit=QuantumCircuit(6+1, 6)
circuit.h([0,1,2,3,4,5])
circuit.x(6)
circuit.h(6)
circuit.barrier()

circuit.cx(5,6)
circuit.cx(3,6)
circuit.cx(1,6)
circuit.barrier()

circuit.h([0,1,2,3,4,5])

circuit.barrier()
circuit.measure([0,1,2,3,4,5],[0,1,2,3,4,5,])

circuit.draw('mpl')

simulator=Aer.get_backend('qasm_simulator')
result=execute(circuit, backend =simulator, shots=1).result()
counts=result.get_counts()
print(counts)
