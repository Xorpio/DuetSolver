import json

nodes = {}

def loadNodes():
    f = open('links.json',)

    data = json.load(f)

    for link in data:
        addLink(link[0], link[1])
        addLink(link[1], link[0])

def addLink(node, link):
    if node not in nodes:
        addNode(node)
    if link not in nodes:
        addNode(link)
    
    nodes[node].append(link)

def addNode(node):
    if node[0] == "+":
        nodeLink = "-"
    else:
        nodeLink = "+"

    if len(node[1:]) > 1:
        nodeLink += node[1:][1] + node[1:][0]
    else:
        nodeLink += node[1:]

    nodes[node] = [nodeLink]

    if nodeLink not in nodes:
        addNode(nodeLink)

def findPath(nodeFrom, nodeTo, path):
    if nodeFrom not in nodes:
        raise Exception("Node from is niet gevonden. Waarde: " + nodeFrom)
    if nodeTo not in nodes:
        raise Exception("Node to is niet gevonden. Waarde: " + nodeTo)

    path.append(nodeFrom)

    if (nodeTo == nodeFrom):
        return path
    
    paths = []
    for link in nodes[nodeFrom]:
        if (link not in path):
            paths.append(findPath(link, nodeTo, path.copy()))

    shortest = 9999
    for p in paths:
        if len(p) > 1  < shortest:
            shortest = len(p)
            shortestPath = p

    if shortest == 9999:
        return []
    else:
        return shortestPath

loadNodes()
nodeFrom = str(input("Node vanaf:"))
nodeTo = str(input("Node naar"))

if (nodeFrom[0] == "+" or nodeFrom[0] == "-"):
    nodesFrom = [nodeFrom]
else:
    nodesFrom = ["+" + nodeFrom, "-" + nodeFrom]

if (nodeTo[0] == "+" or nodeTo[0] == "-"):
    nodesTo = [nodeTo]
else:
    nodesTo = ["+" + nodeTo, "-" + nodeTo]

for nTo in nodesTo:
    for nFrom in nodesFrom:
        path = findPath(nFrom, nTo, [])
    
        print(f'found path for {nFrom} > {nTo}: {len(path)} steps')
        for node in path:
            print(node)
