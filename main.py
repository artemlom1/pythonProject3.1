#Проверить, что строка является синтаксически корректным цветом в формате HEX 18
import re

def hex_color(color):
    pattern = r'^#([A-F a-f 0-9]{2})([A-F a-f 0-9]{2})([A-F a-f 0-9]{2})$'
    return bool(re.match(pattern, color))

print("#0000FF", hex_color('#0000FF'))

print('#000FF', hex_color('#000FF'))
print('#AF00AE', hex_color('#AF00AE'))