#! /usr/bin/env python

# By Eudis Duran
# July 2010

import sys
import getopt
import string

VERSION = '0.0.1'
tmp2 = ''
table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def base64_encode(string, string2):
    """ Basic strategy: Get 3 bytes, and carry out binary
        shifting operations (instead of divisions), as it is much faster.

        This works perfectly for base64, because 2**6 == 64, so
        there is no loss of precision. """

    # Precondition:
    # Postconditions:

    global tmp2
    tmp = ''

    I = open(string, 'rb')
    o = open(string2, 'wb')
        
    text = I.read()
    x = 0
    data = []
    t_len = len(text)
    
    while(x < t_len):
  
        t = text[x:x+3]
        data = []
   
        tmp = int(to_hex(t), 16)
 
        if x + 3 >= t_len:
            if t_len % 3 == 1:
               
                t = text[x: t_len];
                
                tmp = (int(to_hex(t), 16)* (16**4)) # Pad 4 zeros here

                data.append((tmp >> 18) & 0x3f)
                data.append(((tmp >> 12) & 0x0f) | ((tmp >> 12) & 0x30))
                
                for i in range(len(data)):
                    tmp2 = tmp2 + table[data[i]]
                    
                tmp2 = tmp2 + '='
                tmp2 = tmp2 + '='
                
                
            elif t_len % 3 == 2:
                
                t = text[x: t_len];
    
                tmp = (int(to_hex(t), 16)* (16**2)) # Pad 2 zeros here

                data.append((tmp >> 18) & 0x3f)
                data.append(((tmp >> 12) & 0x0f) | ((tmp >> 12) & 0x30))
                data.append(((tmp >> 6) & 0x03) | ((tmp >> 6) & 0x3f))
             
                for i in range(len(data)):
                    tmp2 = tmp2 + table[data[i]]
                    
                tmp2 = tmp2 + '='
                
            break
                                   
        x = x + 3

        data.append((tmp >> 18) & 0x3f)
        data.append(((tmp >> 12) & 0x0f) | ((tmp >> 12) & 0x30))
        data.append(((tmp >> 6) & 0x03) | ((tmp >> 6) & 0x3f))
        data.append(tmp & 0x3f)
        
        for i in range(len(data)):
            tmp2 = tmp2 + table[data[i]]
    
    o.write(tmp2)
    o.close();
    I.close()
    return



def base64_decode(string, string2):
    
    global tmp2
    tmp2 = ''
    I = open(string, 'rb')
    o = open(string2, 'wb')

    binary = I.read();

    b_len = len(binary);

    #print get_pos('i')

    x = 0
    while (x < b_len):
        
        x = x + 1

    o.write(tmp2)
    
    o.close();
    I.close()
    return

def main(argv):
    if(len(argv) != 0):
        try:
            opts, args = getopt.getopt(argv, "ed", ["--encode", "--decode"])
            if argv[0] == '-e':
                if len(argv) < 2:
                    usage();
                elif len(argv) == 2:
                    base64_encode(argv[1], "a.out")
                elif len(argv) == 3:
                    base64_encode(argv[1], argv[2])
                else:
                    print "Wrong Input Format!  Try Again.";
                    
            elif argv[0] == '-d':
                if len(argv) < 2:
                    usage();
                elif len(argv) == 2:
                    base64_decode(argv[1], "a.out")
                elif len(argv) == 3:
                    base64_decode(argv[1], argv[2])
                else:
                    print "Wrong Input Format!  Try Again.";
        except getopt.GetoptError:
            usage()
            sys.exit(2)
    else:
        usage();
        
    return


def usage():
    usage = "Base64 codec \n" \
            "By Eudis Duran (http://ccny.cuny.edu)" \
            "\nVersion: " + VERSION +\
            "\n\n" \
            "Usage:\n" \
            " filter [-command] [input file] [output file]\n" \
            "\nCommands:\n"\
            "       -e , --encode64 : encode binary file to base64 MIME CTE\n" \
            "       -d , --decode64 : decode ASCII file to binary from MIME CTE\n" 
            
    print usage
    
    return

def to_hex(string):
    ls = []
    for c in string:
        ls.append(hex(ord(c)).replace('0x', ''));
        if len(ls[len(ls) - 1]) == 1:
            ls[len(ls) - 1] = '0' + ls[len(ls) - 1]
            
            
    return ''.join(ls)

def get_pos(c):
    n = 0
    for i in table:
        if c == i:
            return n
        n = n + 1
        
    return -1

def to_hex_from_text(tuple_4):
    t = ''
    for i in tuple_4:
        n = get_pos(i);
        if n < 10 and n > -1:
            t = t + '0' + str(n)
        else:
            t = t + str(n);    
        
    return t

if __name__ == '__main__':
    main(sys.argv[1:])
