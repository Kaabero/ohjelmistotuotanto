KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self):
        return []
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista()


    def kuuluu(self, n):
        if n in self.lista:
            return True
        return False


    def lisaa(self, n):
        if len(self.lista)<self.kapasiteetti and n not in self.lista:
            self.lista.append(n)
            return True
        
        if len(self.lista)>=self.kapasiteetti and n not in self.lista:
            uusi_lista=self._luo_lista()
            uusi_lista.append(n)
            self.lista.extend(uusi_lista)
            self.kapasiteetti+=self.kasvatuskoko
            return True

        return False

    def poista(self, n):
        indeksi = self.lista.index(n)
        return self.lista.pop(indeksi)

    def mahtavuus(self):
        return len(self.lista)

    def to_int_list(self):
        return self.lista

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for item in a_taulu:
            if item not in b_taulu:
                erotus.lisaa(item)

        return erotus

    def __str__(self):
        if len(self.lista)==0:
            return '{}'
        result='{'
        for i in range(len(self.lista)-1):
            result+=str(self.lista[i])
            result+=', '
        result+=str(self.lista[-1])
        result+='}'
        return result


           
