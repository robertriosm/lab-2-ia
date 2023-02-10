


class BayesianNetwork:
    def __init__(self, nodes) -> None:
        self.graph = {}
        for i,j in nodes.items():
            self.graph[i] = j
        self.tables = {}

    
    def __repr__(self) -> str:
        return ''.join([(f"{i}: {j}\n") for i,j in self.graph.items()])
    
    def setNodeP(self, nodeName, probability):
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


bn = BayesianNetwork({"Burglary": ["Alarm"], "Earthquake":["Alarm"], "Alarm": ["JohnCalls", "MaryCalls"]})

print(bn)

bn.setNodeP("Burglary",0.9)
bn.setNodeP("Earthquake",0.2)
bn.setNodeP("Alarm",0.5555)
bn.setNodeP("Alarm",0.5555)
bn.setNodeP("Alarm",0.5555)
bn.setNodeP("Alarm",0.5555)
bn.setNodeP("Ye",0)
print(bn.tables)