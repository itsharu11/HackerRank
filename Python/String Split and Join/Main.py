

def split_and_join(line):
    line = line.split(" ")
    #print(line)
    line = "-".join(line)
    #print(line)
    result = line
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)