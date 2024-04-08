import json

# 导入field.json
json_file = './predefined_symbols.json'

# 打开并读取JSON文件
with open(json_file, 'r') as file:
    json_str = file.read()

class SymbolTable:
    def __init__(self):
        self.symbols = json.loads(json_str)
    
    def addEntry(self, symbol, address):
        self.symbols[symbol] = address
    
    def contains(self, symbol):
        return symbol in self.symbols
    
    def getAddress(self, symbol):
        return self.symbols[symbol]