import numpy as np
from numpy import cos, sin, sqrt, pi, exp
import Config as cf
from LightSource import LightSource


class Laser(LightSource):
    def __init__(self, rad=1.0, nrays=1_000_000, name=None):
        LightSource.__init__(self, nrays, name=name)
        self.rad = rad
        self.xorient = True
        self.yorient = True

    def GenerateRaysV(self, shape):
        V = np.zeros(shape)
        V[:,0] = 1.0
        return V

    def GenerateRays(self):
        shape = (self.nrays, 3)
        X = np.zeros(shape)
        if(self.rad != 0):
            theta = np.random.uniform(0, 2*pi, self.nrays)
            r = sqrt(np.random.uniform(0, self.rad**2, self.nrays))
            X[:,2] = r*cos(theta)
            X[:,1] = r*sin(theta)
            if(self.xorient):
                Xmark = self.GenerateXMarker()
                X = np.concatenate((X, Xmark), axis=0)
            if(self.yorient):
                Ymark = self.GenerateYMarker()
                X = np.concatenate((X, Ymark), axis=0)
        X = self.OrientRaysX(X)
        V = self.GenerateRaysV(X.shape)
        V = self.OrientRaysV(V)
       # print('Starting laser velocity')
       # print(V[:10])
       # print('Starting laser position')
       # print(X[:10])
        return X,V

    def GenerateXMarker(self):
        div = 2
        shape = (int(self.nrays/div),3)
        X = np.zeros(shape)
        theta = np.random.uniform(0, 2*pi, int(self.nrays/div))
        r = sqrt(np.random.uniform(0, (self.rad/4)**2, int(self.nrays/div)))
        X[:,2] = r*cos(theta) + self.rad*2/3
        X[:,1] = r*sin(theta)
        return X
    
    def GenerateYMarker(self):
        div = 5
        shape = (int(self.nrays/div),3)
        X = np.zeros(shape)
        theta = np.random.uniform(0, 2*pi, int(self.nrays/div))
        r = sqrt(np.random.uniform(0, (self.rad/4)**2, int(self.nrays/div)))
        X[:,2] = r*cos(theta) 
        X[:,1] = r*sin(theta) + self.rad*2/3
        return X
