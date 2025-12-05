# 15. Pengenalan String
print("15. PENGENALAN STRING")
print("")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Membuat string dengan single quote '...'
data = 'Menggunakan single quote'
print(data)

## Membuat string dengan double quote "..."
data = 'Menggunakan double quote'
print(data)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Menggunakan tanda \ 
### Tanda (') menjadi string (\')
print("G\'day")

### Backlash (\\)
print("C:\\user\\Good Morning")

### Tab (\t)
print("Good\tMorning")

### Backspace (\b)
print("Good \bMorning")

### Newline (\n) dan (\r)
print("Good \nMorning")   # LF   = Line Feed                 -> unix, macos, linux
print("Good \rMorning")   # CR   = Carriege Return           -> comodore, acorn, lisp
print("Good \r\nMorning") # CRLF = Line Feed Carriege Return -> windows

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## String Literal atau raw
### Hati-Hati
print("C:\new dolder") # Akan salah pathnya

### Menggunakan raw string
print("r'C:\new folder")

### Menggunakan multiline literal string
print("""
Nama : Baby Boba
Umur : 1 bulan
""")

### Menggunakan multiline literal string dan raw
print(r"""
Nama    : Baby Boba
Umur    : 1 bulan \baby
Website : www.BabyBoba.com/newID
""")
