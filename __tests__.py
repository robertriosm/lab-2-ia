from rrbayesnet.bayesian import BayesianNetwork

bn = BayesianNetwork({
    "Burglary": ["Alarm"],
    "Earthquake":["Alarm"],
    "Alarm": ["JohnCalls", "MaryCalls"],
    "JohnCalls":[],
    "MaryCalls":[]
    })

# print(bn)

# bn.setParentNodeProb("Alarm", 0.5555)
# bn.setParentNodeProb("Ye",0)

bn.setParentNodeProb("Burglary", 0.002)
bn.setParentNodeProb("Earthquake", 0.001)

bn.setDepNodeProb("Alarm", [0.94, 0.95, 0.69, 0.999])
bn.setDepNodeProb("JhonCalls", [0.91, 0.05])
bn.setDepNodeProb("MaryCalls", [0.75, 0.02])
# print(bn.graph)

print()
print()
print()
print()
# print(bn.dependencies('Alarm'))
# print(bn.dependencies('Alarm'))

print()
print()
print()
print(bn.getCompact())
print(bn.describe())
print(bn.factors())
