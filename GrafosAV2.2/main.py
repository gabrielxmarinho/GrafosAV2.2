import Grafos
import matplotlib.pyplot as plt
import networkx as nx
import hierarchyTree
filename = "data.txt"
f=open(filename,'r')
conteudo=f.read().split("\n")
vertices =  range(1,int(conteudo[0])+1)
arestas = []
for j in range(1,len(conteudo)-1):
    valores = [int(conteudo[j].split(" ")[0]),int(conteudo[j].split(" ")[1])]
    arestas.append(valores)
raizIndex = int(conteudo[len(conteudo)-1].split("\n")[0])-1
G = Grafos.Grafo(vertices, arestas)
spanningTree = Grafos.SpanningTree(G,raizIndex)
for vertice in G.V:
    print(f"{vertice.dado} : {vertice.distancia}")
    print(vertice.caminho)
#Grafo
graph = nx.Graph()
for aresta in G.E:
    graph.add_edge(aresta.vertice1.dado,aresta.vertice2.dado)
nx.draw(graph, with_labels=True)
plt.show()
#Árvore
tree = nx.Graph()
spanningTree.percorrer(spanningTree.raiz,tree)
pos = hierarchyTree.hierarchy_pos(tree,spanningTree.raiz.dado)
nx.draw(tree,pos=pos,with_labels=True)
plt.show()













