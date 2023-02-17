import rrbayesnet.bayesian as bayesian

"""
def setDepNodeProb(self, nodeName, probability):
            
        appearences = 0
        parents = set()
        

        for node in self.graph.values():
            if nodeName in node:
                appearences += 1
                parents = {i for i in self.graph if self.graph[i]==node}
        

        rows = 2**(len(parents)+1)
        cols = 2
        

        # tabla vacia
        # table = [[1 for j in range(cols)] for i in range(rows)]
        table = []

        # tabla booleana
        boolTable = list(product((True, False), repeat=len(parents)+1))

        print("")
        print(boolTable)
        print(table)

        for parent in parents:
            # primeros fors para llenar con valores del primer
            for x in range(len(boolTable)):
                for y in range(len(boolTable[0])):
                    if boolTable[x][y]:
                        # table[x][y] *= self.tables[parent][0]
                        pass
                    else:
                        pass
                        # table[x][y] *= self.tables[parent][1]



        print(f"heres da thing: {parents}")
        print(f"heres da table bruhhh: {table}")
        
        # ok, ya tengo al nodo influido y a los influyentes, ahora a armar tablas

"""



bn = BayesianNetwork({"Burglary": ["Alarm"],"Earthquake":["Alarm"],"Alarm": ["JohnCalls", "MaryCalls"]})

# print(bn)

bn.setParentNodeProb("Burglary", 0.002)
bn.setParentNodeProb("Earthquake", 0.001)
# bn.setParentNodeProb("Alarm", 0.5555)
# bn.setParentNodeProb("Ye",0)
print('jajajaj:')
bn.setDepNodeProb("Alarm", [0.1,0.3,0.5,0.2])
# print(bn.tables)
# print(bn.graph)

print()
print()
print()
print()
# print(bn.dependencies('Alarm'))
# print(bn.dependencies('Alarm'))
# print(bn.describe())

print()
print()
print()
print(bn.getCompact())
