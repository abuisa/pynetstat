## TENTANG TOOL INI 
Tool/Script ini adlah tool untuk melihat aktifitas koneksi dan port yang terbuka menggunakan netstat 
yang dieksekusi menggunakan python untuk mendapatkan format output yang sesuai dengan keinginan, 
dilengkapi dengan filter yang lebih memudahkan

## KETERANGAN FILE dan HOW TO 
Terdapat 4 (empat) file python `.py`: 
1.	file `getappname.py` untuk menampilkan aktifitas koneksi dan port yang digunakan, 
	- HOW TO: 
		
		tulis perintah di terminal/CMD : `python getappname.py` lalu ENTER
		![Tampilah Awal](img_exp/exp0.JPG "Tampilan Awal")
		langsung tekan ENTER untuk menampilkan semua, atau tulis string untuk filter output,
	- Berikut contoh hasil screenshot menggunakan filter : 
		![Filter Contoh Awal](img_exp/exp1.JPG "Filter Contoh Awal")

2.	file `getappname_table_output.py` untuk menampilkan aktifitas koneksi dan port yang digunakan dengan output dalam format tabel,
	- HOW TO:
		
		pertama, install dulu module `terminaltables` dengan perintah : `pip install terminaltables`
		setelah itu perintah sama dengan perintah pada `getappname.py`
	- Contoh screenshot menggunakan filter, output dalam format tabel : 
		![Tampilah empat](img_exp/exp3.JPG "Tampilan empat")
3.	file `getappname_to_listver.py` = `getappname-table-output.py`, bedanya `getappname-to-listver.py` menggunakan manajement list tanpa simpan ke file.
4.	file `test.py` adalah file untuk test panggil fungsi yang terdapat pada file `getappname_to_listver.py` dan `getappname_table_output.py`,
	ketika dijalankan, akan diminta memilih 1 dari 2 pilihan, `1. menampilkan tanpa DOMAIN NAME` dan, `2. menampilkan lengkap dengan DOMAIN NAME`.
	- Contoh screenshot : 
	![Tampilah lima](img_exp/exp41.JPG "Tampilan lima")
	
## CONTOH OUTPUT 
1. Contoh keSatu, tampilah awal setelah perintah `python getappname.py`, langsung ENTER akan menampilkan semua, atau input string untuk filter : 
![Tampilah satu](img_exp/exp0.JPG "Tampilan satu")
2. Contoh keDua, menggunakan filter `fire`, menampilkan aktifitas koneksi yang mengandung string `fire`: 
![Tampilah dua](img_exp/exp1.JPG "Tampilan dua")
3. Contoh keTiga, menggunakan filter `tele`, menampilkan aktifitas koneksi yang mengandung string `tele`: 
![Tampilah tiga](img_exp/exp2.JPG "Tampilan tiga")
4. Contoh keEmpat, menggunakan filter `tele` dan filter `fire` dalam satu frame screenshot :
![Tampilah empat](img_exp/exp3.JPG "Tampilan empat")
5. Contoh keLima, output dengan menyertakan DOMAIN NAME :
![Tampilah lima](img_exp/exp4.JPG "Tampilan lima")