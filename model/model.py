import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self_ordini = DAO.getOrdini()
        self._idMap = {}
        for o in self_ordini:
            self._idMap[o.order_id]= o


    def store(self):
        self._store = DAO.getStore()
        return self._store

    def buildGraph(self, store, k):
        self.addNodi(store)
        self.addArchi(store,k)

    def addNodi(self,store):
        self._nodi =DAO.getNodi(store)
        for n in self._nodi:
            self._grafo.add_node(self._idMap[n])

    def addArchi(self,store,k):
        store1 = store
        store2 = store
        k1 = int(k)
        self._archi = DAO.getArchi(store1, store2, k1)
        for a in self._archi:
            self._grafo.add_edge(self._idMap[a["id1"]],self._idMap[a["id2"]], weight= a["peso"])

    def cammino(self, nodo):
        dfs = nx.dfs_tree(self._grafo, nodo)
        a = list(dfs.nodes())
        return a
