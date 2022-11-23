file = open("a.txt", "r", encoding='Latin1')
lista = open("email0.txt", "w")
lines = file.readlines()

num_arquivo = 0
num = 0

for dado in lines:
    if ".com" in dado or ".br" in dado:
        if ".br" in dado:
            email = dado.index(".br") + 3
            pessoa = dado[:email]
        else:
            email = dado.index(".com") + 4
            pessoa = dado[:email]
        lista.write(pessoa)
        num += 1
        if num % 2000 == 0:
            lista.close()
            num_arquivo += 1
            lista = open(f"email{num_arquivo}.txt", "w")
        else:
            lista.write(",")
#56048
#56236