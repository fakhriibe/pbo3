menu = {
  "cireng"     :1000,
  "citul      ":2000,
  "usus goreng":2000,
  "ice tea    ":5000,
  "ice boba   ":10000,
}
print("===================== Daftar Menu =====================")
for i in menu:
    print("Daftar Menu : ", i,"\t Harga : ",menu[i])
print("pembelian diatas Rp50.000,- mendapatkan diskon 15%")
print("=======================================================")
beli = input("pilihan Menu : ")
jumlah = int((input("jumlah pesanan : ")))
bayar = jumlah * menu[beli]

if bayar > 100000:
  diskon = bayar*15/100
  total = bayar - diskon
else :
     total = bayar

print("===================== Detail pembayaran =====================")
print("menu yang dipesan        :  ",beli)
print("jumlah yang dipesan      : ",jumlah)
print("total biaya              : ",bayar)
print("total yang harus dibayar : ",total)