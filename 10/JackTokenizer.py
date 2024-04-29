import re
import consts
import time

class JackTokenizer:
    def __init__(self, file_path):
        self.text = file_path.read()
        self.token = ""
        self.type = None
        self.sanitize()

    def sanitize(self):
        # Remove comments
        self.text = re.sub(consts.REGEX_COMMENTS, consts.EMPTY, self.text)

    def keyword(self):

        return self.token.upper()
    
    def symbol(self):

        return self.token
    
    def identifier(self):

        return self.token
    
    def int_val(self):

        return int(self.token)
    
    def string_val(self):

        return self.token
    
    def tokenType(self):

        return self.type

    

    def has_more_tokens(self):
        if re.fullmatch(consts.REGEX_EMPTY_TEXT, self.text):
            return False
        return True

    def advance(self):
        if self.has_more_tokens():
            REGEX_TO_ACTION = [
                (consts.REGEX_KEYWORD, self._set_keyword_props),
                (consts.REGEX_SYMBOL, self._set_symbol_props),
                (consts.REGEX_DIGIT, self._set_digit_props),
                (consts.REGEX_STRING, self._set_string_props),
                (consts.REGEX_IDENTIFIER, self._set_identifier_props)
            ]

            for regex, action in REGEX_TO_ACTION:
                match = re.match(regex, self.text)
                if match:
                    action(match)
                    return
                
    def _set_general_props(self, match, regex, tokenType):
        self.token = match.group(1)
        if tokenType == consts.SYMBOL and self.token in consts.OPERATORS_MAP:
            self.token = consts.OPERATORS_MAP[self.token]

        self.type = tokenType
        self.text = re.sub(regex, consts.EMPTY, self.text)

    def _set_keyword_props(self, match):
        self._set_general_props(match, consts.REGEX_KEYWORD, consts.KEYWORD)

    def _set_symbol_props(self, match):
        self._set_general_props(match, consts.REGEX_SYMBOL, consts.SYMBOL)

        
    def _set_digit_props(self, match):
        self._set_general_props(match, consts.REGEX_DIGIT, consts.INT_CONST)

    def _set_string_props(self, match):
        self._set_general_props(match, consts.REGEX_STRING, consts.STRING_CONST)

        
    def _set_identifier_props(self, match):
        self._set_general_props(match, consts.REGEX_IDENTIFIER, consts.IDENTIFIER)


if __name__ == "__main__":

    # 打开一个文件，向其写入
    res = open("./res/MainT.xml", "w")
    res.write("<tokens>\n")
    with open("./ArrayTest/Main.jack", "r") as file:
        jt = JackTokenizer(file)
        while jt.has_more_tokens():
            jt.advance()
            print(jt.token)
            res.write(f"<{jt.tokenType()}> {jt.token} </{jt.tokenType()}>\n")
    res.write("</tokens>")
    res.close()
