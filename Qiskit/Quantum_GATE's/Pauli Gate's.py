


import numpy as np
from qiskit import *

circuit =QuantumCircuit(3,3) #initialiizing quantum register = 2 and classical register =2

circuit.draw()

circuit.x(0) # pauli X Gate which when applied on |0> gives |1> and vice versa
circuit.y(1) # pauli Y Gate which when applied on |0> gives i|1> and when applied on |1> gives -i|0>
circuit.z(2) # Pauli Z Gate there will be no changes which when applied on |0> and it flips the phas when applied to |1> as -|1>


circuit.draw()

