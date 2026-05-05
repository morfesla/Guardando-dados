import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone:str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CNPJ: {self.cnpj}\n')
        print(f'telefone:{self.telefone}')


Quantidade_empresas = 2
lista_empresas = []

print('Solicitando dados')

for i in range(Quantidade_empresas):
    nova_empresa = Empresa(
        nome=input('Digite seu nome: '),
        cnpj=input("Digite sua cnpj: "),
        telefone=input("Digite seu telefone: ")
    )
    print("")
    lista_empresas.append(nova_empresa)

print("Exibindo dados")

for empresa in lista_empresas:
    empresa.mostrar_dados()


print("Salvando dados==")

with open("Contato_Empresas.csv", "a", encoding='utf-8') as arquivo:
    for empresa in lista_empresas:
        arquivo.write(f'{empresa.nome},{empresa.cnpj},{empresa.telefone}\n')

print("Salvo com sucesso!")
print("= fim do programa. =")