def split_list(l: list = None, n: int = None, new_list: list = []):
    if len(l) <= n:
        new_list.append(l)
        return new_list
    else:
        new_list.append(l[:n])
        return split_list(l[n:], n)

alist = [1,2,3,4,5,6,7,8,9,10,11,12]
split_list(alist,int(len(alist)/2))


i = [(2,6),(3,8)]
print(i[0][1])