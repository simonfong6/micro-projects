from compression import Compression

class RunLength(Compression):
    def encode(self,bytes):
        num_bytes_array = []
        bytes_array = []
        
        num_bytes = 0
        old_c = None
        
        for c in bytes:
            # Second condition to handle when sequence is longer than 255.
            if((c != old_c) or (num_bytes == 255)):
                if(old_c != None):  
                    num_bytes_array.append(num_bytes)
                    bytes_array.append(old_c)
                    num_bytes = 0
            
            num_bytes += 1
            old_c = c
            
        num_bytes_array.append(num_bytes)
        bytes_array.append(old_c)
        
        
        
        num_bytes_array = ''.join([chr(i) for i in num_bytes_array])
        bytes_array = ''.join(bytes_array)
        
        encoded_bytes = ''
        
        for num,c in zip(num_bytes_array,bytes_array):
            encoded_bytes += num + c

        return encoded_bytes
        
    def decode(self,bytes):
        decoded_bytes_array = []
        
        for num, c in zip(bytes[0::2], bytes[1::2]):
            num = ord(num)
            decoded_bytes_array.extend([c for i in range(num)])
            
        decoded_bytes = ''.join(decoded_bytes_array)
        
        return decoded_bytes

