''' Roman Numerals to integer'''

def integer_to_roman(num:int):
    symbols=[ ["I",1],
              ["IV",4],
              ["V",5],
              ["IX",9],
              ["X",10],
              ["XL",40],
              ["L",50],
              ["XC",90],
              ["C",100],
              ["CD",400],
              ["D",500],
              ["CM",900],
              ["M",1000],
            ]
    
    result=''
    
    for symbol,value in reversed(symbols):
        if num//value > 0:
            no_of_times = num//value
            result= result + (symbol*no_of_times)
            num = num % value
    print(result)

convert=input('Enter a Number: ')
integer_to_roman(int(convert))
