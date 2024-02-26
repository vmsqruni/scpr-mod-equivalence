from abc import ABC, abstractmethod
import math
import unittest

class Node:
    """ A node in the model """
    def __init__(self, x, y, phi):
        self.x = x
        self.y = y
        self.phi = phi
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getPhi(self):
        return self.phi
    
class ForceCalculator(ABC):
    """ Abstract definition of a Force calculator """
    @abstractmethod
    def lx(self):
        pass

    @abstractmethod
    def ly(self):
        pass

    @abstractmethod
    def lphi(self):
        pass

    @abstractmethod
    def calculate(self):
        pass
    
    @abstractmethod
    def calculate_fnodes(self):
        pass

class ScprForceCalculator(ForceCalculator):
    """ Calculates forces like in the scpr model """
    def __init__(self, node1, node2, cell_radius, fmyo):
        self.node1 = node1
        self.node2 = node2

        # Model params
        self.r = cell_radius
        self.fmyo = fmyo
    
    def lx(self):
        return self.node2.getX() - self.node1.getX()

    def ly(self):
        dphi = self.lphi()
        return self.r * dphi

    def lphi(self):
        dphi = self.node2.getPhi() - self.node1.getPhi()

        if dphi < math.pi:
            pass
        elif dphi > 0 :
            dphi -= 2 * math.pi
        else:
            dphi += 2 * math.pi
        
        return dphi

    def calculate(self):
        """ Calculate Ftot """
        ltot = math.sqrt(math.pow(self.ly(), 2) + math.pow(self.lx(), 2))
        return ltot

    def calculate_fnodes(self):
        """ Calculate Force on nodes """
        node_forces = [[0, 0], [0, 0]] # [Fnd1, Fnd2]
        fnd1 = node_forces[0]
        fnd2 = node_forces[1]

        ftot = self.calculate()
        
        dfx = self.fmyo * self.lx() / ftot
        dfy = self.fmyo * self.ly() / ftot

        fnd1[0] += dfx
        fnd1[1] += dfy

        fnd2[0] -= dfx
        fnd2[1]  -= dfy

        return node_forces

class ModuloForceCalculator(ForceCalculator):
    """ Calculates forces using modulo operator """

    def __init__(self, node1, node2, cell_radius, fmyo):
        self.node1 = node1
        self.node2 = node2

        # Model Parameters
        self.r = cell_radius
        self.fmyo = fmyo

    def lx(self):
        return self.node2.getX() - self.node1.getX()
    
    def ly(self):
        dphi = self.lphi()
        return self.r * dphi

    def lphi(self):
        return (self.node2.getPhi() - self.node1.getPhi()) % (2 * math.pi)
    
    def calculate(self):
        """ Calculate Ftot """
        return math.sqrt(math.pow(self.ly(), 2) + math.pow(self.lx(), 2))
    
    def calculate_fnodes(self):
        """ Calculate Force on nodes """
        node_forces = [[0,0], [0,0]]
        return node_forces

if __name__ == "__main__":
    print("Entered Python App!")