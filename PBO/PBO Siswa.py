class Siswa:
	'''Dasar kelas untuk semua siswa'''
	jumlah_siswa = 0
	
	def __init__(self, nama, NIS):
		self.nama = nama
		self.NIS = NIS
		Siswa.jumlah_siswa += 1
		
	def tampilkan_jumlah(self):
		print("Total siswa:", Siswa.jumlah_siswa)
		
	def tampilkan_profil(self):
		print("Nama :", self.nama)
		print("NIS :", self.NIS)
		
# Membuat objek pertama dari kelas Siswa
siswa1 = Siswa("Nuril Karyamin", 16243)
# Membuat objek kedua dari kelas Siswa
siswa2 = Siswa("Fauzan", 16244)

siswa1.tampilkan_profil()
siswa2.tampilkan_profil()
print("Total siswa :", Siswa.jumlah_siswa)
