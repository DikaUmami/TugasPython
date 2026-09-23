# Menentukan Tipe Data dengan Constructor Function di Python

x = str("Hello World")
print(x, type(x))          # str

x = int(20)
print(x, type(x))          # int

x = float(20.5)
print(x, type(x))          # float

x = complex(1j)
print(x, type(x))          # complex

x = list(("apple", "banana", "cherry"))
print(x, type(x))          # list

x = tuple(("apple", "banana", "cherry"))
print(x, type(x))          # tuple

x = range(6)
print(x, type(x))          # range

x = dict(name="John", age=36)
print(x, type(x))          # dict

x = set(("apple", "banana", "cherry"))
print(x, type(x))          # set

x = frozenset(("apple", "banana", "cherry"))
print(x, type(x))          # frozenset

x = bool(5)
print(x, type(x))          # bool

x = bytes(5)
print(x, type(x))          # bytes

x = bytearray(5)
print(x, type(x))          # bytearray

x = memoryview(bytes(5))
print(x, type(x))          # memoryview