
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        counter = 0
        buf4 = [None, None, None, None]
        
        while True:
            num_read = read4(buf4)
            if num_read == 0:
                return counter
            for i in range(num_read):
                buf[counter] = buf4[i]
                counter += 1
                if counter == n:
                    return counter
