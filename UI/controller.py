import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceDDStore = None
        self._choiceDDOrd = None


    def handleCreaGrafo(self, e):
        store = self._choiceDDStore
        k = self._view._txtIntK.value
        print(store.store_id)
        self._model.buildGraph(store.store_id, k)
        for y in self._model._grafo.nodes:
            self._view._ddNode.options.append(
                ft.dropdown.Option(text=y.order_id, on_click=self._readDDOrdine, data=y))
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato coorettamenti con nodi: {len(self._model._grafo.nodes)} e con archi: {len(self._model._grafo.edges)}"))
        self._view.update_page()

    def handleCerca(self, e):
        nod_cam= self._model.cammino(self._choiceDDOrd)
        self._view.txt_result.controls.append(ft.Text(
            f"Nodo di partenza {self._choiceDDOrd}"))
        for n in nod_cam[1:]:
            self._view.txt_result.controls.append(ft.Text(
                f"{n}"))
            self._view.update_page()


    def handleRicorsione(self, e):
        pass

    def fillddStore(self):
        store = self._model.store()
        for y in store:
            self._view._ddStore.options.append(ft.dropdown.Option(text=y.store_name,on_click=self._readDDStore , data= y))

    def _readDDStore(self,e):
        if e.control.data is None:
            print("error")
            self._choiceDDStore = None
        else:
            self._choiceDDStore = e.control.data

    def _readDDOrdine(self,e):
        if e.control.data is None:
            print("error")
            self._choiceDDOrd = None
        else:
            self._choiceDDOrd = e.control.data


