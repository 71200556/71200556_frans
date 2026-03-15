def perkalian(a, b):
    hasil = 0
    
    for i in range(a):
        hasil = hasil + b
        if i < a-1:
            print(b, end=" + ")
        else:
            print(b, end="")
    
    print(" =", hasil)


# Contoh 
perkalian(6, 5)
perkalian(7, 10)