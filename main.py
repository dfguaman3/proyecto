import requests,json,urllib.request, datetime, sys
import pandas as pd
from PyQt5 import uic, QtWidgets
from mplwidget import MplWidget
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
#url_covid = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
#url= 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
qtCreatorFile = "interfaz.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.MplWidget = MplWidget(self.MplWidget)
        self.cargar.clicked.connect(self.getCSV)
        
        self.df = pd.read_csv('./data/covid_data.csv', parse_dates=['Country'], sep=',', na_values='')
        
        
    def getCSV(self):
        
        paises = self.df['Country']
        estados = self.df['State']
        fechas = self.df.loc['1/22/2020':'10/31/2020'].values()
        col_names=self.df.columns.tolist()
        dat=pd.DataFrame(self.df)
        fechas.groupby('Country')[col_names[2]].sum().plot(kin='bar',legend='Reverse')
        print(len(col_names))
        for i in paises:
            self.listacountry.addItem(str(i))
        for j in estados:
            self.listastate.addItem(str(j))   
        
    
        
        

    def presentarTabla(self):
        
        try:
            titulo='Daily Number of Cases and Deaths in '
            self.titulo=titulo
            data=self.df.loc['1/22/2020':'10/31/2020']
            self.lon=self.df.columns.tolist()
            

            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.bar(list(self.lon),data, width = 0.4, align='center')
            self.MplWidget.canvas.axes.legend((self.titulo, self.titulo), loc='upper right')
            self.MplWidget.canvas.axes.set_title(f'{self.titulo}')
            self.MplWidget.canvas.axes.set_xlabel('Fecha')
            self.MplWidget.canvas.axes.set_ylabel('Numero de casos diarios')
            self.MplWidget.canvas.axes.grid(True)
            self.MplWidget.canvas.draw()
        except Exception as e:
            print(e)     
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
