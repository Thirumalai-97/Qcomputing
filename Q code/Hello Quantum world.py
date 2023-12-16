#Qiskit Framework

from qiskit import *

circuit=QuantumCircuit(2,2)
circuit.h(0)
circuit.cx(0,1)
circuit.draw('mpl')

--------------------------------

Pennylane

import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

dev=qml.device("default.qubit", wires=2)

def circuit(angles):
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0,1])
    return qml.expval(qml.PauliX(wires=0))

    
angles=[0.5,0.5]
qnode = qml.QNode(circuit, dev)
qml.draw_mpl(qnode, decimals=1, style="sketch")(angles)
plt.show()


--------------------------------
