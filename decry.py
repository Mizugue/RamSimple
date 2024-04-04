import os
import fernet

listagem = os.listdir()
arquivosfoco = []


for f in listagem:
    if f == "crip.py" or f == 'chave.key' or f == 'decry.py':
        continue
    if os.path.isfile(f):
        arquivosfoco.append(f)



with open("chave.key", "rb") as key:
    chave = key.read()



senha = "senha"
usersenha = input("Digite a senha: ")


try:
    if usersenha == senha:
        for f in arquivosfoco:
            with open(f, "rb") as file:
                conteudo = file.read()
                conteudodecri = fernet.Fernet(chave).decrypt(conteudo)
            with open(f, "wb") as file:
                file.write(conteudodecri)
            print(f"Arquivos descriptografado: {f}")
    else:
        print("Senha errada! ")
except:
    print("Nada a fazer...")
