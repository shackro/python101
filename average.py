num=[2,5,6,3,5]
def numb():
    print(num)

    for k in num:
        count=len(num)
        average=sum(num)/count
        print(count)
        print(average)
        break
numb()

look=["hello","should he be out there",]
def long():
    max_len = +1
    for ele in look:
        if (len(ele) >max_len ):
         max_len = len(ele)
        res = ele

long()