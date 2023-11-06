# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(842, 658)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(187, 188, 255);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout = QVBoxLayout(self.home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(187, 188, 255);")

        self.verticalLayout.addWidget(self.label)

        self.btn_entrar = QPushButton(self.home)
        self.btn_entrar.setObjectName(u"btn_entrar")

        self.verticalLayout.addWidget(self.btn_entrar, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.home)
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout_3 = QHBoxLayout(self.main_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.main_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	border: 3px solid rgba(0, 0, 0, .2);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")

        self.verticalLayout_2.addWidget(self.btn_cadastrar, 0, Qt.AlignHCenter)

        self.btn_listar = QPushButton(self.frame)
        self.btn_listar.setObjectName(u"btn_listar")

        self.verticalLayout_2.addWidget(self.btn_listar, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_voltar = QPushButton(self.frame)
        self.btn_voltar.setObjectName(u"btn_voltar")

        self.verticalLayout_2.addWidget(self.btn_voltar)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.main_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(699, 0))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border: 3px solid rgba(0, 0, 0, .2);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_altura = QLineEdit(self.frame_3)
        self.line_altura.setObjectName(u"line_altura")
        self.line_altura.setEnabled(False)
        self.line_altura.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_altura, 1, 4, 1, 1)

        self.btn_salvar = QPushButton(self.frame_3)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setEnabled(False)

        self.gridLayout.addWidget(self.btn_salvar, 2, 2, 1, 1, Qt.AlignHCenter)

        self.line_nome = QLineEdit(self.frame_3)
        self.line_nome.setObjectName(u"line_nome")
        self.line_nome.setEnabled(False)
        self.line_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_nome, 0, 0, 1, 5)

        self.line_sexo = QLineEdit(self.frame_3)
        self.line_sexo.setObjectName(u"line_sexo")
        self.line_sexo.setEnabled(False)
        self.line_sexo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_sexo, 1, 1, 1, 1)

        self.line_peso = QLineEdit(self.frame_3)
        self.line_peso.setObjectName(u"line_peso")
        self.line_peso.setEnabled(False)
        self.line_peso.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_peso, 2, 1, 1, 1)

        self.btn_limpar = QPushButton(self.frame_3)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setEnabled(False)

        self.gridLayout.addWidget(self.btn_limpar, 2, 3, 1, 1)

        self.line_idade = QLineEdit(self.frame_3)
        self.line_idade.setObjectName(u"line_idade")
        self.line_idade.setEnabled(False)
        self.line_idade.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.line_idade, 1, 2, 1, 2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 212))
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"	border: 3px solid rgba(0, 0, 0, .2);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_atualizar = QPushButton(self.frame_6)
        self.btn_atualizar.setObjectName(u"btn_atualizar")
        self.btn_atualizar.setEnabled(False)

        self.verticalLayout_4.addWidget(self.btn_atualizar)

        self.btn_apagar = QPushButton(self.frame_6)
        self.btn_apagar.setObjectName(u"btn_apagar")
        self.btn_apagar.setEnabled(False)

        self.verticalLayout_4.addWidget(self.btn_apagar)

        self.btn_calcular = QPushButton(self.frame_6)
        self.btn_calcular.setObjectName(u"btn_calcular")
        self.btn_calcular.setEnabled(False)

        self.verticalLayout_4.addWidget(self.btn_calcular)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"#frame_5{\n"
"	border: 3px solid rgba(0, 0, 0, .2);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_nome = QLabel(self.frame_5)
        self.label_nome.setObjectName(u"label_nome")

        self.gridLayout_3.addWidget(self.label_nome, 0, 1, 1, 1)

        self.label_imc = QLabel(self.frame_5)
        self.label_imc.setObjectName(u"label_imc")

        self.gridLayout_3.addWidget(self.label_imc, 1, 1, 1, 1)

        self.label_recom = QLabel(self.frame_5)
        self.label_recom.setObjectName(u"label_recom")

        self.gridLayout_3.addWidget(self.label_recom, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.main_page)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/logo/img/hgym_logo.png\"/></p></body></html>", None))
        self.btn_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_listar.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
        self.btn_voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.line_altura.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Altura", None))
        self.btn_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.line_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.line_sexo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.line_peso.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.line_idade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Idade", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Sexo", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Idade", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Altura", None));
        self.btn_atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_apagar.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.btn_calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">IMC :</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Recomenda\u00e7\u00f5es:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome :</span></p></body></html>", None))
        self.label_nome.setText("")
        self.label_imc.setText("")
        self.label_recom.setText("")
    # retranslateUi

