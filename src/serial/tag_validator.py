"""
"<DIV>  unmatched <  </DIV>"
"<A></A><B></B>"
"<A"
"""
class Solution:
    def isValid(self, code: str) -> bool:
        return len(code) == self.consume_closed(0, code) 

    def consume_closed(self, pos, code):
        # print('closed', code[pos:])
        pos, ltag = self.consume_ltag(pos, code)
        if pos < 0:
            return -1
        
        pos = self.consume_content(pos, code)
        if pos < 0:
            return -1
        
        pos, rtag = self.consume_rtag(pos, code)
        # print('ltag vs rtag', ltag, rtag)
        if ltag != rtag:
            return -1

        return pos
    
    def consume_ltag(self, pos, code):
        # print('ltag', code[pos:])
        if code[pos] != '<':
            return -1, None
        
        pos, tag = self.consume_tagname(pos + 1, code)

        if pos < 0:
            return -1, None
        
        if pos < len(code) and code[pos] == '>':
            return pos + 1, tag
        # print('fetched', pos, code[pos], tag)
        return -1, None
    
    def consume_content(self, pos, code):
        # print('content', code[pos:])
        while pos < len(code) and code[pos] != '<':
            pos += 1
            
        if pos == len(code):
            return -1
        
        if code[pos:pos+2] == '</':
            return pos
        
        if code[pos:pos+2] == '<!':
            pos = self.consume_cdata(pos, code)
            if pos < 0:
                return False
            return self.consume_content(pos, code)
 
        pos = self.consume_closed(pos, code)
        if pos < 0:
            return False
        
        return self.consume_content(pos, code)

    def consume_rtag(self, pos, code):
        # print('rtag', code[pos:])
        if code[pos:pos+2] != '</':
            return -1, None
        
        pos, tag = self.consume_tagname(pos+2, code)

        if pos < len(code) and code[pos] == '>':
            return pos + 1, tag
        
        return -1, None

    def consume_tagname(self, pos, code):
        # print('tagname', code[pos:])

        tag = []
        
        while pos < len(code) and code[pos] != '>':
            if not code[pos].isupper():
                # raise RuntimeError(pos, code[pos:])
                return -1, None
            
            tag.append(code[pos])
            pos += 1
        
        if pos < len(code) and code[pos] == '>' and 1 <= len(tag) <= 9:
            return pos, ''.join(tag)
        
        return -1, None
        
    def consume_cdata(self, pos, code):
        # print('cdata', code[pos:])
        if not code[pos:].startswith("<![CDATA["):
            return -1
        pos += len("<![CDATA[")
        while pos < len(code) and code[pos:pos+3] != ']]>':
            pos += 1
        
        if code[pos:pos+3] == ']]>':
            return pos + 3
        
        return -1
