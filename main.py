class Ac:
    def __init__ (self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __add__ (self, other):
        return self.jumlah + other.jumlah
    
    def __repr__ (self):
        return self.nama;
    
    @property
    def __dict__ (self):
        return self.nama;


belanja1 = Ac("LG", 2)
belanja2 = Ac("Samsung", 3)
print(belanja1 + belanja2)
print(belanja1)
print(belanja1.__dict__)