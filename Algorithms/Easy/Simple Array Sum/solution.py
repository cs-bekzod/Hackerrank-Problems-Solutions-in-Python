# solution 1
def simpleArraySum(ar):
    return sum(ar)

#---------------------------------->

# solution 2
def simpleArraySum(ar):
    summ = 0
    for i in range(sum(ar)):
        summ += i
    return summ
