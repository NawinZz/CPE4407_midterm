import math 
import numpy as np
from numpy import random
import numpy
from numpy.core.defchararray import array, count
from numpy.lib.shape_base import tile
from numpy.testing._private.utils import break_cycles

class Mission:
    def __init__(self):
        self.Mname = {
            "testing equipment team",
            "maintenance team"
            "internship team"
            }
    def getJobName(self):
        return self.Mname


class Teams:
    def __init__(self):
        self.Tname = {
            "A",
            "B",
            "C",
        }
        self.TeamTable = np.array([
                    ['xxx'],['xxx'],
                    ['xxx'],['xxx'],
                    ['xxx'],['xxx'],
                    ['xxx'],['xxx'],
                    ['xxx'],['xxx'],
        ])
        self.TeamTableWeek = np.array([self.TeamTable for _ in range(len(self.Tname))])
    def getTname(self):
        return self.Tname
    def getTweek(self):
        return self.TeamTableWeek

class Workload:
    def __init__(self):
        self.WL = np.array([
                        # Name_of_work, Number_of_work , Team, TimeSlot
                         ["001",0,-1,-1],                           #0
                         ["002",1,-1,-1],
                         ["003",2,-1,-1],
                         ["004",2,-1,-1],
                         ["005",1,-1,-1],
                         ["006",0,-1,-1],
                         ["007",2,-1,-1],
                         ["008",0,-1,-1],
                         ["009",1,-1,-1],
                         ["010",0,-1,-1],                        #9
                         ["011",2,-1,-1],
                         ["012",0,-1,-1],
                         ["013",1,-1,-1],
                         ["014",0,-1,-1],
                         ["015",1,-1,-1],
                         ["016",2,-1,-1],
                         ["017",2,-1,-1],
                         ["018",1,-1,-1],
                         ["019",0,-1,-1],
                         ["020",2,-1,-1],                         #19

        ])
    def getWorkload(self):
        return self.WL


#MAIN#
def Scheduling(WL,RW):
    array = [0,0,0]
    for i in range(len(WL)):
        rndWorks = random.randint(0,len(RW))
        rndTable = random.randint(0,len(RW[0])-1)
        while(RW[rndWorks, rndTable] != 'xxx'):
            rndWorks = random.randint(0,len(RW)-1)
            rndTable = random.randint(0,len(RW[0])-1)
        WL[i,2] = rndWorks
        WL[i,3] = rndTable
        RW[int(WL[i,2]),int(WL[i,3])] = WL[i,0]
        if int(WL[i,2]) == 0:
            array[0]+=1
        elif int(WL[i,2]) == 1:
            array[1]+=1
        elif int (WL[i,2]) == 2:
            array[2]+=1
    return array
def FitnessValueCalculation(WL,RW):
    value = 20
    timetable = []
    work = []
    for r in range(len(RW)):
        if (RW[r,6] != 'xxx'):
            value -= 1
        if (RW[r,7] != 'xxx'):
            value -= 1
    for count in range(len(RW)):
        timetable.append(WL[count][3])
        work.append(WL[count][1])
    for n in range (len(WL)):
        if n+1 == len(WL):
            if WL[n][3] == timetable[0] and WL[n][1] == work[0]:
                value = 0
            else:
                break
        if(WL[n][3] == timetable[n+1]and WL[n][1] == work[n+1]):
            print(WL[n][3],timetable[n+1],work[n+1])
            value = 0
    fv = len(WL)-1
    while WL[fv][3] == timetable[fv-1] and WL[fv][1] == work[fv-1]:
        value = 0
        if fv-1 == len(WL):
            if WL[fv][3] == timetable[len(WL)-1] and WL[fv][1] == work[len(WL)-1]:
                value = 0
            else:
                break
        fv-=1
    return value
def ResultDisplay(RW,WL):
    min=int(len(RW)/len(WL))
    max=math.ceil(len(RW)/len(WL))
    number_of_Work=[]
    for i in range(len(RW)):
        count=0
        print()
        for sl in range(len(RW[i])):
            if RW[i,sl] != ['xxx']:
                count+=1
            print(RW[i,sl],end="")
            if sl%2 == 1:
                print()
        number_of_Work.append(count)
        print("total day of work",number_of_Work[i])

def WorkloadDisplay(WL):
    print(WL)

M = Mission()
T = Teams()
W = Workload()
g = W.getWorkload()
t = T.getTweek()
min = int(len(g)/len(t))
max = math.ceil(len(g)/len(t))
S = Scheduling(W.getWorkload(),T.getTweek())
while True:
    if(S[0] == min or S[0] <= max) and (S[1] == min or S[1] <= max) and (S[2] == min or S[2] <= max):
        break
    else:
        T = Teams()
        S = Scheduling(W.getWorkload(),T.getTweek())
print("AllWorkload : " , len(W.getWorkload()))
ResultDisplay(T.getTweek(),W.getWorkload())
print()