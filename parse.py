def parse(lst):
    result = '[['
    count = 0
    for i in lst:
        if(i == ' 'and (count % 16 == 15) and (count!= 0)):
            result += '],\n['
            count += 1
        elif(i == ' '):
            result += ','
            count += 1
        elif(i != ' '):
            result += i
        # print("count : " + str(count))
    result += "]]"
    return result

a = parse('14 4 13 1 2 15 11 8 3 10 6 12 5 9 0 7 0 15 7 4 14 2 13 1 10 6 12 11 9 5 3 8 4 1 14 8 13 6 2 11 15 12 9 7 3 10 5 0 15 12 8 2 4 9 1 7 5 11 3 14 10 0 6 13')
b = parse('13 2 8 4 6 15 11 1 10 9 3 14 5 0 12 7 1 15 13 8 10 3 7 4 12 5 6 11 0 14 9 2 7 11 4 1 9 12 14 2 0 6 10 13 15 3 5 8 2 1 14 7 4 10 8 13 15 12 9 0 3 5 6 11')
print(b)