def Nome():
    nome = input("Qual o seu nome? ")
    while nome == "":
        print("Erro, não deixe o campo vazio")
        nome = input("Nome: ")
    return nome

def Idade():
    idade = input("Ano de nascimento: ")
    while idade == "":
        print("Erro, não deixe o campo vazio")
        idade = input("Ano de nascimento: ")

    idade = int(idade)
    while idade <= 1920 or idade >= 2023:
        print("Erro, insira uma data válida!")
        idade = input("Ano de nascimento: ")
        idade = int(idade)
    return idade

def Rg():
    rg = input("Seu RG: ")
    while rg == "":
        print("Erro, não deixe o campo vazio")
        rg = input("Seu RG: ")

    while len(rg) != 10:
        print("Erro, preencha o campo corretamente!")
        rg = input("Seu RG: ")
    return rg

def Cpf():
    cpf = input("Seu CPF: ")
    while cpf == "":
        print("Erro, não deixe o campo vazio")
        cpf = input("Seu CPF: ")

    while len(cpf) != 11:
        print("Erro, preencha o campo corretamente")
        cpf = input("Seu CPF: ")
    return cpf

def Endereco():
    endereco = input("Seu endereço: ")
    while endereco == "":
        print("Erro, não deixe o campo vazio")
        endereco = input("Seu endereço: ")
    return endereco

def Cep():
    cep = input("Seu Cep: ")
    while cep == "":
        print("Erro, não deixe o campo vazio")
        cep = input("Seu Cep: ")

    while len(cep) != 8:
        print("Erro, dados inválidos")
        cep = input("Seu Cep: ")
    return cep

def edicaoDados():
    edit = input("Qual campo deseja editar?")
    print("*")
    edit = int(edit)
    if edit == 1:
        nome = Nome()
    elif edit == 2:
        idade = Idade()
    elif edit == 3:
        rg = Rg()
    elif edit == 4:
        cpf = Cpf()
    elif edit == 5:
        endereco = Endereco()
    else:
        while edit not in [1, 2, 3, 4, 5]:
            print("Erro: Insira uma opção válida!")
            edicaoDados()

def confirmaDados(nome, idade, rg, cpf, endereco, cep):
    print("*" * 5)
    print("Você confirma os dados?")
    print(f"[1] Nome: {nome}")
    print(f"[2] Nascimento: {idade}")
    print(f"[3] RG: {rg}")
    print(f"[4] CPF: {cpf}")
    print(f"[5] Endereço: {endereco}")
    print(f"[6] CEP: {cep}")
    print("*" * 5)

    conf = input("Você confirma os dados? (S/N): ").upper()
    if conf == "N":
        edicaoDados()
    return conf

def confirmaRegistro(nome, idade, rg, cpf, endereco, cep):
    conf = input("Você confirma os dados? (S/N): ").upper()

    while conf not in ["S", "N"]:
        print("Erro: valor inserido inválido")
        conf = input("Você confirma os dados? (S/N): ").upper()

    if conf == "N":
        edicaoDados()
    elif conf == "S":
        confirmaDados(nome, idade, rg, cpf, endereco, cep)

def pedirCredito():
    credito = int(input("Linha de crédito: R$ "))
    while credito > 5000:
        print("Erro: novos usuários têm limite de R$ 5.000,00 de crédito")
        credito = int(input("Linha de crédito: R$ "))
    return credito

def compra(credito):
    celular = input("""
    
Celulares:

[1] Samsung A03 Core      - R$ 600,00
[2] iPhone 13 Pro          - R$ 3.000,00
[3] Motorola Moto G15      - R$ 1.500,00
[4] Positivo Twist 5 Pro   - R$ 850,00

Qual celular vai comprar? 
Digite a sua opção: """)
    
    celular = int(celular)
    if celular == 1:
        valor = 600
        escCelular = input(f"Dados do pedido:\nCelular Samsung A03 Core\nR$ {valor},00\n\nConfirma a compra? (S/N): ").upper()

    elif celular == 2:
        valor = 3000
        escCelular = input(f"Dados do pedido:\nCelular iPhone 13 Pro\nR$ {valor},00\n\nConfirma a compra? (S/N): ").upper()

    elif celular == 3:
        valor = 1500
        escCelular = input(f"Dados do pedido:\nCelular Motorola Moto G15\nR$ {valor},00\n\nConfirma a compra? (S/N): ").upper()

    elif celular == 4:
        valor = 850
        escCelular = input(f"Dados do pedido:\nCelular Positivo Twist 5 Pro\nR$ {valor},00\n\nConfirma a compra? (S/N): ").upper()

    else:
        print("Erro: Opção inválida!")
        return credito 

    while escCelular not in ["S", "N"]:
        escCelular = input("Erro: Digite S ou N: ").upper()

    if escCelular == "S":
        if credito < valor:
            print("Crédito insuficiente para efetuar a compra")
        else:
            print("Parabéns, você efetuou a compra, obrigado e volte sempre :)")
            credito -= valor 
    else:
        print("Compra cancelada.")
    
    return credito

nome = Nome()
idade = Idade()
rg = Rg()
cpf = Cpf()
endereco = Endereco()
cep = Cep()

confirmaRegistro(nome, idade, rg, cpf, endereco, cep)

credito = pedirCredito()
credito = compra(credito)  
print(f"Seu crédito restante é: R$ {credito}")
