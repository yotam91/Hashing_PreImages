import hashlib

#import random


def hash_preimage(target_string):
    result = 0
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        nonce = b'\x00'

    intTarget_string = int(target_string)
    i = 0
    while True:
        x = i
        xBytes = bytes(x)
        h_hex = hashlib.sha256( xBytes ).hexdigest()
        
        #convert to binary
        h_bin = bin( int( h_hex, base=16 ) )[2:]
        end = len(h_bin)
        extractedBits = h_bin[end-len(target_string): end]


        if extractedBits==target_string:
            
            return(bytes(x))
        else:
            #print('Retrying')
            i = i+1


# Enter any binary value here
target_hash = '100'


print(hash_preimage(target_hash))

