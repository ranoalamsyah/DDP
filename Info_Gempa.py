# info_gempa.py
from Gempa import Gempa

# Membuat objek gempa
gempa_banten = Gempa("Banten", 1.2)
gempa_palu = Gempa("Palu", 6.1)
gempa_cianjur = Gempa("Cianjur", 5.6)
gempa_jayapura = Gempa("Jayapura", 3.3)
gempa_garut = Gempa("Garut", 4.0)

# Memanggil fungsi dampak() untuk masing-masing objek gempa
gempa_banten.dampak()
gempa_palu.dampak()
gempa_cianjur.dampak()
gempa_jayapura.dampak()
gempa_garut.dampak()
