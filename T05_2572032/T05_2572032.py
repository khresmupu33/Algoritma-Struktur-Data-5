## Definisi Kelas ##
## Definisi Kelas MyListElement
## Nama: Khresna Mulia Putra (Khresmupu)
## NRP: 2572032

## Definisi Atribut:
# first : elemen pertama dalam array(integer)
class MyList:
    def __init__(self):
        self.first=None
        return
    # Q : Nilai yang diinput(MyListElement)
    def InsertFirst(self, Q):
        Q.next = self.first
        self.first = Q
        return
    # Q : Nilai yang diinput(MyListElement)
    def InsertLast(self, Q):
        if (self.first == None):
            self.InsertFirst(Q)
        else: #search posisi last
            last = self.first
            while (last.next != None):
                last = last.next
            last.next = Q #insert
        return
    # prev : Nilai yang akan dihapus(string)
    def removeAfter(self,prev):
        Q= prev.next
        prev.next = prev.next.next
        Q.next = None
        return Q 
    def traversal(self):
        p=self.first
        while p!=None:
            print(f"|{p.info}| ",end="")
            p=p.next
        print() 
    # terpilih : Nilai yang akan terpilih(string)
    def searchPrev(self,terpilih):
        p=self.first
        if p.info!=terpilih:
            prev = None
            while p!=None:
                if  p.info==terpilih:
                    print(f"{terpilih} ditemukan, memutar lagu...") 
                    break
                else:
                    prev = p
                    p=p.next
            if p.info!=terpilih:
                print("Lagu tidak ditemukan")

            self.removeAfter(prev)
            self.InsertFirst(MyListElement(terpilih))
        else:
            print("Lagu tersebut sedang diputar")
        self.traversal()

## Definisi Atribut:
# info  : atribut yang menyimpan nilai (integer)
# next  : atribut reference elemen berikutnya
#         (Node)
class MyListElement:
    def __init__(self, value):
        self.info = value
        self.next = None
        return       

# Kamus Data (Main Program):
# p             : Gambaran objek list lagu
# tanyaObjek    : sebagai input(integer)
# n             : Jumlah lagu (integer)
# pilih         : pilih menu (integer)
# terpilih      : pilih lagu(integer)
def main():
    p=MyList()
    while True:
        n=int(input("Masukkan jumlah lagu:: "))
        if n <2:
            print("Jumlah lagu tidak boleh kurang dari 2")
        else:
            break
    print("- - - Masukkan lagu ke playlist - - -")
    for i in range(n):
        tanyaObjek=MyListElement(str(input("Judul lagu:")))
        p.InsertLast(tanyaObjek)
    print("Isi Playlist: ")
    p.traversal()
    while True:
        print("==================================")
        print("1. Putar lagu")
        print("2. keluar")
        pilih=int(input("pilih menu"))
        if pilih==2:
            break
        else:
            terpilih=str(input("Pilih lagu untuk diputar:"))
            p.searchPrev(terpilih)
        print("==================================")
    print("Selesai ^^")
if __name__ == '__main__':
    main()