# Dosyayı açın
dosya_adı = "../Norm/task/train.txt"
count = 0
with open(dosya_adı, "r") as dosya:
    # Dosyayı satır satır okuyun
    for satir in dosya:
        # Her satırı işleyin veya yazdırın
        print(satir.strip())  # Satır sonundaki yeni satır karakterini (newline) kaldırarak yazdırın
        count=count+1

print(count)
# Dosyayı otomatik olarak kapatır
