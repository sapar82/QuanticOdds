import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

input_keys = ['000E']
collapser_keys = ['005Aup', '006Aup', '007Adn']
output_keys = ['001Sup', '002Sdn', '003Sup', '004Sdn']
list_of_nodes = input_keys + collapser_keys + output_keys
list_of_edges = [('000E', '005Aup'),('005Aup', '006Aup'),('005Aup', '007Adn'),('006Aup', '001Sup'),('006Aup', '002Sdn'),('007Adn', '003Sup'),('007Adn', '004Sdn')]


G.add_nodes_from(list_of_nodes)
G.add_edges_from(list_of_edges)
nx.draw_networkx(G)
paths = nx.all_simple_paths(G, source=list_of_nodes[0], target=list_of_nodes[-4:])
list_of_paths = list(paths)
print(list_of_paths)
plt.show()

entree = [2, 3]  #Le spin et la prob
collapser =  dict([(key, {'up':(0,0,1), 'dn':(0,0,0)}) for key in collapser_keys]) #spin, prob, prob in pour up and down 

output = dict([(key, 0) for key in output_keys])


def calcul_prob(axe, spin, prob_in):
    
    prob_rel = 2
    prob_out = prob_rel*prob_in
    spin_out = 1
    out = {'up':(prob_rel, prob_out, spin_out), 'dn':(1-prob_rel, 1-prob_out, 1-spin_out)}
    return(out)

print(entree, collapser, output)
for path1 in list_of_paths:
    collapser[path1[1]]['up'] = calcul_prob(2, entree[0], entree[1])[path1[1][-2:]]
    #print(collapser[path1[1]]['up'])
    for pos, key in enumerate(path1[1:-1]):
        #print(calcul_prob(2, collapser[path1[pos+1]][key[-2:]][0], collapser[path1[pos+1]][key[-2:]][1]))
        #print(path1[pos+1])
        collapser[path1[pos+2]] = calcul_prob(2, collapser[path1[pos+1]][key[-2:]][0], collapser[path1[pos+1]][key[-2:]][1])
    output[path1[-1]] = calcul_prob(2, collapser[path1[-2]][key[-2:]][0], collapser[path1[-2]][key[-2:]][1])

print(entree, collapser, output)