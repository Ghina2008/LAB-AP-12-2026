class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        return (
            f"{self.nama:<12} "
            f"{self.id_pemain:<12} "
            f"{self.role:<12} "
            f"{self.hitung_skor_akhir():<10.2f} "
            f"{self.status_performa()}"
        )


daftar_pemain = []

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
while True:
    jumlah = int(input("Masukkan jumlah pemain: "))
    if jumlah < 0 :
        print ("Error! jumlah pemain tidak boleh minus")
        continue
    elif jumlah == 0:
        print ("Error! Jumlah pemain tidak boleh kosong")
        continue
    else:
        break
for i in range(jumlah):
    print(f"\n-- Data Pemain ke-{i+1} --")

    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = float(input("Nilai Kill: "))
    nilai_assist = float(input("Nilai Assist: "))
    nilai_objective = float(input("Nilai Objective: "))

    pemain = Pemain(
        nama,
        id_pemain,
        role,
        nilai_kill,
        nilai_assist,
        nilai_objective
    )

    daftar_pemain.append(pemain)

print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("-" * 80)
print(f"{'No':<5}{'Nama':<12}{'ID Pemain':<12}{'Role':<12}{'Skor Akhir':<12}{'Status'}")
print("-" * 80)

for i, pemain in enumerate(daftar_pemain, start=1):
    print(
        f"{i:<5}"
        f"{pemain.nama:<12}"
        f"{pemain.id_pemain:<12}"
        f"{pemain.role:<12}"
        f"{pemain.hitung_skor_akhir():<12.2f}"
        f"{pemain.status_performa()}"
    )

print("-" * 80)