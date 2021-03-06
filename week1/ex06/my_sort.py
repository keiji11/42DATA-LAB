"""
Integrate the following dictionary in your code. Then
write a program that displays the names of the musicians
sorted by year in ascending order, then in alphabetic
order for similar years. One per line, without showing
the year.

(d dict down below)
"""

d = {
'Hendrix' : '1942',
'Allman' : '1946',
'King' : '1925',
'Clapton' : '1945',
'Johnson' : '1911',
'Berry' : '1926',
'Vaughan' : '1954',
'Cooder' : '1947',
'Page' : '1944',
'Richards' : '1943',
'Hammett' : '1962',
'Cobain' : '1967',
'Garcia' : '1942',
'Beck' : '1944',
'Santana' : '1947',
'Ramone' : '1948',
'White' : '1975',
'Frusciante': '1970',
'Thompson' : '1949',
'Burton' : '1939',
}

s = list((dict(sorted(d.items(), key=lambda x: (x[1],x[0])))).keys())
for i in s:
  print(i)