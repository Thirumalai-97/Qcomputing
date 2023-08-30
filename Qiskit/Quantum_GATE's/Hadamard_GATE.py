from qiskit import *
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex, plot_histogram
from qiskit.quantum_info import Operator

circuit=QuantumCircuit(2,2) #creating Q Circuit with required number of qubits
circuit.h(0) # h() represents Hadamard GATE
circuit.cx(0,1) # CX() represents Controlled NOT GATE

circuit.measure([0,1],[0,1])
circuit.draw('mpl') # 'mpl' is default used to draw circuit

state=Statevector.from_int(0,2**2) # intializeing 2 qubits
state=state.evolve(circuit)
state.draw('latex') # latex is same as mpl

array_to_latex(state)
state.draw('qsphere')

state.draw('hinton')

op= Operator(circuit)
op.data
