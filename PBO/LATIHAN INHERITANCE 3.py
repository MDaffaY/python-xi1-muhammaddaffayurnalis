# INHERITANCE / PEWARISAN
# super class / parent class
class Manusia:
	# konstruktor
	def __init__(self, nama, jk, usia):
		self.nama = nama
		self.jk = jk
		self.usia = usia
		
	def info(self):
		print("Nama: {}\nJenis Kelamin : {}\nUsia : {}".format(self.nama, self.jk, self.usia))
		print("------------------------")
		
	def makan(self):
		print("Sedang makan nasi")
		print("------------------------")
		
# sub class / child class
class Pelajar(Manusia):
	def belajar(self):
		print("{} Sedang belajar".format(self.nama))
		print("------------------------")
		
	# methode overriding
	def makan(self):
		print("{} sedang sarapan pagi dengan nasi". format(self.nama))
		print("------------------------")
		
#sub class / child class
class Pekerja(Manusia):
	# konstruktor anak
	def bekerja(self):
		print("{} sedang bekerja".format(self.nama))
		print("------------------------")
		
#instansiasi objek
Rudi = Pelajar("Rudianto", "Laki-laki", 16)
Wawan = Pekerja("Iwan", "Laki-laki", 29)

#pemanggilan
Rudi.info()
Rudi.belajar()
Rudi.makan() #memanggil methode anak
Wawan.info()
Wawan.bekerja()
Wawan.makan() # memanggil methode induk