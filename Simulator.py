# Simulator for Senior Design Project
# Objective: Function that generates random point within a 10 radius area around a point
#
# Assumes Metric System
import random
import math
import numpy
from numpy import sqrt, dot, cross
from numpy.linalg import norm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Device:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Anchor(Device):

    def findRadius(self):
        self.radius = self.RTOF * 299792458 / 2
    
    def pingDeviceWithoutError(self, sensor: Device):
        deltaX = sensor.x - self.x
        deltaY = sensor.y - self.y
        deltaZ = sensor.z - self.z
        magnitude = math.sqrt(deltaX*deltaX + deltaY*deltaY + deltaZ*deltaZ)
        self.RTOF = magnitude*2/299792458

    def pingDeviceWithNumericalError(self, sensor: Device, maxError: float):
        deltaX = sensor.x - self.x
        deltaY = sensor.y - self.y
        deltaZ = sensor.z - self.z
        magnitude = math.sqrt(deltaX*deltaX + deltaY*deltaY + deltaZ*deltaZ)
        error = random.uniform(-maxError, maxError)
        self.RTOF = magnitude*error*2/299792458

    def pingDeviceWithPercentError(self, sensor: Device, percentError: float):
        deltaX = sensor.x - self.x
        deltaY = sensor.y - self.y
        deltaZ = sensor.z - self.z
        magnitude = math.sqrt(deltaX*deltaX + deltaY*deltaY + deltaZ*deltaZ)
        magnitude = random.uniform(magnitude - magnitude * (100 - percentError) / 100,
                                   magnitude + magnitude * (100 - percentError) / 100)
        self.RTOF = magnitude*2/299792458

class Hub:
    def __init__(self):
        self.anchors = [Anchor(0,0,0), Anchor(1,0,0), Anchor(0,1,0), Anchor(0,0,1)]

    def pingDeviceWithoutError(self, sensor: Device):
        for anchor in self.anchors:
            anchor.pingDeviceWithoutError(sensor)
            anchor.findRadius()

    def pingDeviceWithNumericalError(self, sensor: Device, maxError: float):
        for anchor in anchors:
            anchor.pingDeviceWithNumericalError(sensor, maxError)
            anchor.findRadius()

    def pingDeviceWithPercentError(self, sensor: Device, percentError: float):
        for anchor in anchors:
            anchor.pingDeviceWithPercentError(sensor, percentError)
            anchor.findRadius()

    def findCurrentDevice(self) -> list:
        # The process has three steps for error free measurements:
        #   1. Find the circle on the plane of intersection between two spheres
        #   2. Find the intersections of the two remaining spheres with that plane
        #   3. Use trilateration on those three circles to determine the final location
        anchors = self.anchors
        P0 = numpy.array([anchors[0].x, anchors[0].y, anchors[0].z])
        P1 = numpy.array([anchors[1].x, anchors[1].y, anchors[1].z])
        P2 = numpy.array([anchors[2].x, anchors[2].y, anchors[2].z])
        P3 = numpy.array([anchors[3].x, anchors[3].y, anchors[3].z])
        r = []
        for num in range(0,4):
            r.append(anchors[num].radius)
        answers = trilaterate(P0, P1, P2, r[0], r[1], r[2])
        square_dist = [numpy.sum(answers[0]**2 + P3**2, axis=0)]
        dist = [numpy.sqrt(square_dist[0])]
        square_dist.append(numpy.sum(answers[1]**2 + P3**2, axis=0))
        dist.append(numpy.sqrt(square_dist[1]))
        option1 = dist[0] - r[3]
        option2 = dist[1] - r[3]
        if option2 < option1:
            return [answers[0][0], answers[0][1], answers[0][2]]
        else:
            return [answers[1][0], answers[1][1], answers[1][2]]
        
        

class System:
    def __init__(self, x: float, y: float, z: float):
        self.hub = Hub()
        self.devices = [Device(x, y, z)]

    def addSensor(self, x: float, y: float, z: float):
        self.devices.append(Device(x, y, z))

def trilaterate(P1,P2,P3,r1,r2,r3):                      
    temp1 = P2-P1                                        
    e_x = temp1/norm(temp1)                              
    temp2 = P3-P1                                        
    i = dot(e_x,temp2)                                   
    temp3 = temp2 - i*e_x                                
    e_y = temp3/norm(temp3)                              
    e_z = cross(e_x,e_y)                                 
    d = norm(P2-P1)                                      
    j = dot(e_y,temp2)                                   
    x = (r1*r1 - r2*r2 + d*d) / (2*d)                    
    y = (r1*r1 - r3*r3 -2*i*x + i*i + j*j) / (2*j)       
    temp4 = r1*r1 - x*x - y*y                            
    if temp4<0:                                          
        raise Exception("The three spheres do not intersect!");
    z = sqrt(temp4)                                      
    p_12_a = P1 + x*e_x + y*e_y + z*e_z                  
    p_12_b = P1 + x*e_x + y*e_y - z*e_z                  
    return p_12_a,p_12_b  

if __name__ == '__main__':
    system = System(10, 18, -9)
    system.hub.pingDeviceWithoutError(system.devices[0])
    point = system.hub.findCurrentDevice()
    print(point)
    print(point[0])
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.plot([point[0]],[point[1]], [point[2]],0,marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
