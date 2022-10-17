""" P7... Reverse Integer """

def reverse(num: int):
        y = str(abs(num))
        y = y.strip()
        y = y[::-1]
        output = int(y)
        if output >= 2** 31 -1 or output <= -2** 31:
            print( 0 )
        elif num < 0:
            print( -1 * output )
        else:
            print( output )
reverse(500)
