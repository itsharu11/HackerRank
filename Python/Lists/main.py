if __name__ == '__main__':
    N = int(input())
    i=0
    myList = []
    while i < N:
        option = input()
        if option == 'print':
            print(myList)
        
        if option == 'sort':
            myList = sorted(myList)
        
        if option == 'pop':
            myList.pop()
        
        if option == 'reverse':
            myList = myList[::-1]
            
        if option.startswith("remove"):
            element = int(option.split()[1])
            myList.remove(element)
            
        if option.startswith("append"):
            element=int(option.split()[1])
            myList.append(element)
            
        if option.startswith("insert"):
            position, element = int(option.split()[1]), int(option.split()[2])
            myList.insert(position, element)
        
        i+=1
