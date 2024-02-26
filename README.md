## Description

This repository serves as validation that a specific refactoring provides the same results. Specifically:

This code calculates the deltas in x-, y- and phi-coordinates and the subsequent forces between two nodes.

## Classes
Node: A simple node class which holds its coordinates
ScprForceCalculator: calculates lx, ly, lphi and ltot as in the SCPR model by Vavylonis et al.
ModForceCalculator: calculates lx, ly, lphi and ltot via a refactored implementation that relies on the modulo operator rather than if-else condiditionals.