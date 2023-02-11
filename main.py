


class BayesianNetwork:

    def __init__(self, nodes) -> None:
        self.graph = {}
        for i,j in nodes.items():
            self.graph[i] = j
        self.tables = {}

    
    def __repr__(self) -> str:
        return ''.join([(f"{i}: {j}\n") for i,j in self.graph.items()])
    

    def setParentNodeProb(self, nodeName, probability:int):
        if nodeName in self.graph.keys():
            f = 0
            for i in self.graph:
                if nodeName in self.graph[i]:
                    f = 1
            if f == 0:
                self.tables[nodeName] = probability
            else:
                print("node not independent")
        else:
            print("node not in graph")


    def setDepNodeProb(self, nodeName):

        if nodeName in self.graph.keys():

            self.tables[nodeName] += 0







            for child in self.graph.values():
                pass




bn = BayesianNetwork({"Burglary": ["Alarm"], "Earthquake":["Alarm"], "Alarm": ["JohnCalls", "MaryCalls"]})

print(bn)

bn.setParentNodeProb("Burglary", 0.9)
bn.setParentNodeProb("Earthquake", 0.2)
bn.setParentNodeProb("Alarm", 0.5555)
bn.setParentNodeProb("Alarm", 0.5555)
bn.setParentNodeProb("Alarm", 0.5555)
bn.setParentNodeProb("Alarm", 0.5555)
bn.setParentNodeProb("Ye",0)
print(bn.tables)
print(bn.graph)