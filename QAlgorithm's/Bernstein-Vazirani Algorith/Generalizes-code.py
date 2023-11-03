from qiskit import *
%matplotlib inline
from qiskit.tools.visualization import plot_histogram

print("Enter only binary numbers")
number=input()

n=len(number)

#creating n+1 qubits and n classical bits to measure 
circuit=QuantumCircuit(n+1,n)

#Applying Hadamard Gate on first n qubits 
circuit.h(range(0,n))
#applying X gate and Hadamard gate on nth qubit 
circuit.x(n)
circuit.h(n)
#barrier to differentiate
circuit.barrier()

#applying CX gate wherever Bin string euquals to 1, so that we can quess the number 
for i, j in enumerate(reversed(number)):
    if j=='1':
        circuit.cx(i,n)
circuit.barrier()

#Hadamard again to reverse and  get the number entered 
circuit.h(range(n+1))
circuit.barrier()

#measuring all qubit's to classical bit's
circuit.measure(range(n), range(n))

#circuit.draw('mpl')
#optinal to show the cirsuit

#guessing the number using the backend simulator
simulator=Aer.get_backend('qasm_simulator')
result=execute(circuit, backend =simulator, shots=1).result()
counts=result.get_counts()
print(counts)
