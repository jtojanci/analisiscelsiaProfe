from generators.generadorProductos import generarDatosProductos
import pandas as pd

def analizarDatos():
    datos=generarDatosProductos()
    tabla=pd.DataFrame(datos,columns=["Producto","Categoria"])
    tabla.to_csv("./data/TablaProductos.csv",index=False)
analizarDatos()