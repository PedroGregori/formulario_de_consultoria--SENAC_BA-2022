from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import uic

from model.consulta import Consulta
from model.consulta_dao import ConsultaDAO

FILE_UI = 'view/main_window.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(FILE_UI, self)  
        
        self.addBtn.clicked.connect(self.add)
        self.editBtn.clicked.connect(self.edit)
        self.delBtn.clicked.connect(self.delete)
        
        self.tabela.horizontalHeader().setStretchLastSection(True) 
        self.tabela.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 
            
        self.loadData()

    def loadData(self):
        listCon = ConsultaDAO.selectALL()
        for c  in listCon:
            self.addTableWidget(c)
            
    def add(self):
        nome = self.nome.text()
        email = self.email.text()
        telefone = self.telefone.text()
        data = self.data.text()
        estado = self.estado.currentText()
        descricao = self.descricao.text()
        
        novaConsulta = Consulta(-1,nome, email, telefone, data, estado, descricao)
        
        id = ConsultaDAO.add(novaConsulta)
        novaConsulta.id = id
        
        self.addTableWidget(novaConsulta)
        self.nome.clear()
        self.email.clear()
        self.telefone.clear()
        self.descricao.clear()
        
        
    def edit(self):
        lineSel = self.tabela.currentRow()
        lineItem = self.tabela.item(lineSel, 0)
        id = lineItem.text()
        nome = self.nome.text()
        email = self.email.text()
        telefone = self.telefone.text()
        data = self.data.text()
        estado = self.estado.currentText()
        descricao = self.descricao.text()
        
        edit = Consulta(id,nome, email, telefone, data, estado, descricao)
        self.updateTable(edit)
        
        ConsultaDAO.edit(edit)
        
        self.nome.clear()
        self.email.clear()
        self.telefone.clear()
        self.descricao.clear()
        
        
        
    def delete(self):
        lineSel = self.tabela.currentRow()
        lineItem = self.tabela.item(lineSel, 0)
        id = lineItem.text()
        self.tabela.removeRow(lineSel)  
        ConsultaDAO.delete(int(id))
            
    def addTableWidget(self, c: Consulta):
        line = self.tabela.rowCount()
        self.tabela.insertRow(line)
        
        id = QTableWidgetItem(str(c.id))
        nome = QTableWidgetItem(c.nome)
        email = QTableWidgetItem(c.email)
        tell = QTableWidgetItem(c.telefone)
        data = QTableWidgetItem(c.data)
        estado = QTableWidgetItem(c.estado)
        descricao = QTableWidgetItem(c.descricao)
        
        self.tabela.setItem(line, 0, id)
        self.tabela.setItem(line, 1, nome)
        self.tabela.setItem(line, 2, email)
        self.tabela.setItem(line, 3, tell)
        self.tabela.setItem(line, 4, data)
        self.tabela.setItem(line, 5, estado)
        self.tabela.setItem(line, 6, descricao)
        
        
    def updateTable(self, c: Consulta):
            lineSel = self.tabela.currentRow()
            nome = QTableWidgetItem(c.nome)
            email = QTableWidgetItem(c.email)
            telefone = QTableWidgetItem(c.telefone)
            data = QTableWidgetItem(c.data)
            estado = QTableWidgetItem(c.estado)
            descricao = QTableWidgetItem(c.descricao)
            
            self.tabela.setItem(lineSel, 1, nome)
            self.tabela.setItem(lineSel, 2, email)
            self.tabela.setItem(lineSel, 3, telefone)
            self.tabela.setItem(lineSel, 4, data)
            self.tabela.setItem(lineSel, 5, estado)
            self.tabela.setItem(lineSel, 6, descricao)
        