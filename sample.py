import math
inputUser = None
def volumeBalok (panjang, lebar, tinggi):
    Volume = panjang * lebar * tinggi
    print()
    return Volume

def volumeKerucut (radius, tinggi):
    Volume = math.pi * (1/3) * (radius**2) * tinggi
    print()
    return Volume

def calculatePrice (Volumes):
    TotalVolume = 0
    for i in range (len(Volumes)):
        TotalVolume = TotalVolume + Volumes[i]
    print()
    return TotalVolume
    
listVolume = []
_ = 8
while _ < 9 :
    while inputUser not in ['BALOK', 'KERUCUT', 'STOP']:
        if not inputUser == None : print(f"Input tidak benar, masukkan kembali\n")
        inputUser = str(input(f"Masukkan bentuk galon yang diinginkan (STOP untuk berhenti): "))
    if inputUser == 'STOP': 
        if not len(listVolume) == 0 : print(f"====================================================\nTotal volume air yang dikeluarkan adalah : {format(round(calculatePrice(listVolume), 2), '.2f')}\nTotal harga yang harus dibayar adalah : Rp{format(round(700*calculatePrice(listVolume), 2), '.2f')}\n====================================================\n\nTerima kasih telah menggunakan Depot Air Minum Dek Depe")
        else : print(f"====================================================\nAnda tidak memasukkan input satupun :(\nTerima kasih telah menggunakan Depot Air Minum Dek Depe\n====================================================")
        break
    if inputUser == 'BALOK' :
        p,l,t = float(0), float(0), float(0)
        while p <= 0 : p = float(input("Masukkan panjang balok : "))
        while l <= 0 : l = float(input("Masukkan lebar balok : "))
        while t <= 0 : t = float(input("Masukkan tinggi balok : "))
        listVolume.append(volumeBalok(p,l,t))
        inputUser = None
    if inputUser == 'KERUCUT' :
        rad, t = float(0), float(0)
        while rad <= 0 : rad = float(input("Masukkan jari-jari kerucut : "))
        while t <= 0 : t = float(input("Masukkan tinggi kerucut : "))
        listVolume.append(volumeKerucut(rad,t))
        inputUser = None
