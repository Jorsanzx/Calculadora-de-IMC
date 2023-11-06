from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot
from untitled import Ui_MainWindow
from bd import Data_base
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=  None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Projeto RAD")
        self.widgets_cadastro = [self.line_nome, self.line_sexo,
                                self.line_idade,self.line_altura,
                                self.line_peso, self.btn_salvar,
                                self.btn_limpar]
        
        self.widgets_listar = [self.tableWidget, self.btn_apagar, self.btn_atualizar, self.btn_calcular]

        self.btn_entrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main_page))
        self.btn_cadastrar.clicked.connect(self.habilita_cadastro)
        self.btn_listar.clicked.connect(self.habilita_listagem)
        self.btn_voltar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))

        self.btn_salvar.clicked.connect(self.incluir_aluno)
        self.btn_limpar.clicked.connect(self.limpar_cadastro)
        self.btn_listar.clicked.connect(self.listar_alunos)
        self.btn_apagar.clicked.connect(self.deletar_cadatro)
        self.btn_atualizar.clicked.connect(self.atualizar_cadastro)
        self.btn_calcular.clicked.connect(self.calc_imc)
        
    @Slot()
    def habilita_cadastro(self):
        for widget in self.widgets_cadastro:
            widget.setEnabled(True)

        for widget in self.widgets_listar:
            widget.setEnabled(False)

    @Slot()
    def habilita_listagem(self):
        for widget in self.widgets_listar:
            widget.setEnabled(True)

        for widget in self.widgets_cadastro:
            widget.setEnabled(False)

    @Slot()
    def incluir_aluno(self):
        nome = self.line_nome.text()
        sexo = self.line_sexo.text()
        idade = self.line_idade.text()
        altura = self.line_altura.text()
        peso = self.line_peso.text()

        try:
            float(altura)
        except:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("ERRO")
            alert.setText("Digite sua altura com numeros e use '.' no lugar da ','! ")
            alert.exec()
            return
        
        try:
            float(peso)
        except:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("ERRO")
            alert.setText("Digite seu peso com numeros e use '.' no lugar da ','! ")
            alert.exec()
            return



        print(banco.register_alunos(nome, sexo, idade, peso, altura))

    @Slot()
    def limpar_cadastro(self):
        self.line_nome.clear()
        self.line_sexo.clear()
        self.line_idade.clear()
        self.line_altura.clear()
        self.line_peso.clear()

    @Slot()
    def listar_alunos(self):
        result = banco.select_all_alunos()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))

    @Slot()
    def deletar_cadatro(self):
        id = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
        banco.delete_Alunos(id)
        self.listar_alunos()

    @Slot()
    def atualizar_cadastro(self):

        dados = []
        update_dados = []

        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                dados.append(self.tableWidget.item(row, column).text())

            update_dados.append(dados)
            dados = []

        for aluno in update_dados:
            banco.uppdate_alunos(tuple(aluno))

        self.tableWidget.reset()
        self.listar_alunos()

    @Slot()
    def calc_imc(self):
        try:
            id = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            cursor = banco.connection.cursor()
            cursor.execute(f"SELECT NOME, PESO, ALTURA FROM Alunos WHERE ID ={id}")
            dados = cursor.fetchall()
            try:
                float(dados[0][1])
            except:
                alert = QMessageBox()
                alert.setIcon(QMessageBox.Information)
                alert.setWindowTitle("ERRO")
                alert.setText("Dados Inválidos! Não foi possível fazer o calculo.")
                alert.exec()
                return
            
            try:
                float(dados[0][2])
            except:
                alert = QMessageBox()
                alert.setIcon(QMessageBox.Information)
                alert.setWindowTitle("ERRO")
                alert.setText("Dados Inválidos! Não foi possível fazer o calculo.")
                alert.exec()
                return
                        
            imc =  dados[0][1] / (dados[0][2] * dados[0][2])
            self.label_nome.setText(dados[0][0])
            self.label_imc.setText(f"{imc:.2f}")
            self.label_nome.setStyleSheet('font-size: 16px; font-weight: bold;')
            self.label_imc.setStyleSheet('font-size: 16px; font-weight: bold;')

            if imc <16:
                self.label_recom.setText("Extremamente magro!")
                self.label_recom.setStyleSheet('font-size: 16px; color: red; font-weight: bold;')

            elif imc >=16 and imc <16.9:
                self.label_recom.setText("Muito magro!")
                self.label_recom.setStyleSheet('font-size: 16px; color: orange; font-weight: bold;')

            elif imc >=17 and imc <18.4:
                self.label_recom.setText("Magro!")
                self.label_recom.setStyleSheet('font-size: 16px; color: blue; font-weight: bold;')

            elif imc >=18.5 and imc <24.9:
                self.label_recom.setText("Peso Ideal!")
                self.label_recom.setStyleSheet('font-size: 16px; color: green; font-weight: bold;')

            elif imc >=25 and imc <29.9:
                self.label_recom.setText("Pré-Obeso!")
                self.label_recom.setStyleSheet('font-size: 16px; color: orange; font-weight: bold;')

            elif imc >=30 and imc <34.9:
                self.label_recom.setText("Obesidade Grau I!")
                self.label_recom.setStyleSheet('font-size: 16px; color: red; font-weight: bold;')

            elif imc >=35 and imc <39.9:
                self.label_recom.setText("Obesidade Grau II")
                self.label_recom.setStyleSheet('font-size: 16px;font-weight: bold;')


            else:
                self.label_recom.setText("Obesidade Grau III! Procure ajuda profissional.")
                self.label_recom.setStyleSheet('font-size: 16px; font-weight: bold;')

        except:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("ERRO")
            alert.setText("Selecione um registro!")
            alert.exec()
            return      


if __name__ == '__main__':
    banco = Data_base()
    banco.connect()
    banco.create_table_alunos()  
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    banco.close_connection()