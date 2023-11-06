import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME='db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

class Data_base:
    def __init__(self, name = DB_NAME):

        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_alunos(self):

        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Alunos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT,
            SEXO TEXT,
            IDADE  INTEGER ,
            PESO REAL,
            ALTURA REAL          
            )
        """)
        self.connection.commit()
        cursor.close()

    def register_alunos(self, nome, sexo, idade,
                            altura, peso):
        valores = [nome, sexo, idade, altura, peso]
        cursor = self.connection.cursor()

        try:

            cursor.execute('INSERT INTO Alunos'
                            '(NOME, SEXO, IDADE, PESO, ALTURA)'
                            'VALUES' 
                            '(?, ?, ? ,? ,? )', valores )
                
            self.connection.commit()
            cursor.close()

            return "DADOS INSERIDOS"
        except:
            return "ERRO NA GRAVAÇÃO"

    
    def select_all_alunos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Alunos")
            Alunos = cursor.fetchall()
            return Alunos
        
        except:
            pass

    def delete_Alunos(self, id):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Alunos WHERE ID = '{id}' ")
            
            self.connection.commit()
            cursor.close()

            return "Cadastro Excluido com Sucesso!"
        
        except:
            return "Erro ao Excluir Registro"

    def uppdate_alunos(self, valores):
        
        
  
        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Alunos SET 
                        NOME = ?, 
                        SEXO = ?, 
                        IDADE = ?, 
                        PESO = ?, 
                        ALTURA = ?
                        WHERE ID = ? """, [valores[1],valores[2], valores[3],
                                            valores[4], valores[5], valores[0]] )
        
        self.connection.commit()
        cursor.close()

