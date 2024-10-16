def printing_numbers(n):
    for i in range(1,n):
        num=""
        if i%2==0:
            num="even"
        else:
            num="odd"
        print(i,num)
printing_numbers(20)