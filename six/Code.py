import json

# 导入field.json
json_file = './fields.json'

# 打开并读取JSON文件
with open(json_file, 'r') as file:
    json_str = file.read()

class Ccode:
    def __init__(self):
        # 将JSON字符串解析为Python字典
        self.fields = json.loads(json_str)
        self.binary = ""
        self.dest = ""
        self.comp = ""
        self.jump = ""

    def getDest(self, dest):
        if len(dest) > 0:
            self.dest = self.fields["dest"][dest]
        else:
            self.dest = self.fields["dest"]["null"]

    def getComp(self, comp):
        self.comp = self.fields["comp"][comp]
    
    def getJump(self, jump):
        if len(jump) > 0:
            self.jump = self.fields["jump"][jump]
        else:
            self.jump = self.fields["jump"]["null"]
    def getBinary(self):
        self.binary = f"111{self.comp}{self.dest}{self.jump}\n"
        return self.binary

class Acode:
    def __init__(self):
        self.fields = json.loads(json_str)
        self.binary = ""
    def getBinary(self, symbol):
        # symbol参数是字符串形式的十进制的数，将其转成二进制的字符串
        symbol = bin(int(symbol))[2:].zfill(15)
        self.binary = f"0{symbol}\n"
