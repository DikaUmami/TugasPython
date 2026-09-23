# Escape Characters di Python

# \' -> Single Quote
x = 'It\'s a lovely day'
print(x)

# \\ -> Backslash
x = "Ini adalah tanda backslash: \\"
print(x)

# \n -> New Line
x = "Baris pertama\nBaris kedua"
print(x)

# \r -> Carriage Return
x = "Halo\rDunia"
print(x)

# \t -> Tab
x = "Halo\tDunia"
print(x)

# \b -> Backspace
x = "Halo \bDunia"
print(x)

# \f -> Form Feed
x = "Halo\fDunia"
print(x)

# \ooo -> Octal value
x = "\110\145\154\154\157"   # akan menghasilkan "Hello"
print(x)

# \xhh -> Hex value
x = "\x48\x65\x6c\x6c\x6f"   # akan menghasilkan "Hello"
print(x)