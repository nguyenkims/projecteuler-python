# -*- coding: utf-8 -*-
# inp=file("sampleMatrix.txt")
inp=file("matrix.txt")
#print enumerate(inp.readlines())

A=[j.strip().split(",") for (i,j) in enumerate(inp.readlines())]
LEN=len(A[0])
print A[0], len(A[0]), A[LEN-1][LEN-1]

import pygraph.classes.digraph
import pygraph.algorithms.minmax
#from pygraph.classes.graph import digraph
gr=pygraph.classes.digraph.digraph()
for i in range(0,LEN):
	for j in range(0,LEN):
		gr.add_node((i,j))

for i in range(0,LEN):
	for j in range(0,LEN):
		if i < LEN -1:	gr.add_edge(((i,j),(i+1,j)), int(A[i+1][j]))
		if j < LEN -1 :	gr.add_edge(((i,j),(i,j+1)), int(A[i][j+1]))
		if i >=1 :	gr.add_edge(((i,j),(i-1,j)), int(A[i-1][j]))
		if j >=1 :	gr.add_edge(((i,j),(i,j-1)), int(A[i][j-1]))
#print gr.nodes()
#print gr.edge_weight(((0,0),(0,1)))
#print gr.edge_weight(((4,3),(4,4)))
print pygraph.algorithms.minmax.shortest_path(gr,(0,0))[1][(LEN-1,LEN-1)] + int(A[0][0])