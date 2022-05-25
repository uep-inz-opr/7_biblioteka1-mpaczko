
class Ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = str(tytul)
        self.autor = str(autor)
        self.rok = int(rok)

liczbaEgz=int(input())
ksiazkiArr=[]
egzemplarzeArr=[]

for i in range(liczbaEgz):
    dane_ksiazki = eval(input())
    tytul = dane_ksiazki[0]
    autor = dane_ksiazki[1]
    rok = dane_ksiazki[2]
    ksiazka = Ksiazka(tytul, autor, rok)
    ksiazkiArr.append(ksiazka)

tytuly = []
ilosci = []
results = []
i = 0

for ksiazka in ksiazkiArr:
    tytuly.append(ksiazka.tytul)

for t in tytuly:
    ilosci.append(tytuly.count(t))

for ksiazka in ksiazkiArr:
    results.append("('"+ksiazka.tytul+"', '"+ksiazka.autor+"', "+str(ilosci[i])+")")
    i += 1
    results = set(results)
    results = sorted(results)

for result in results:
    print(result)
    

