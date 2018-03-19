def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    Mlist=['','M','MM',"MMM"]
    Clist=['',"C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    Xlist=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    Ilist=['','I','II','III','IV','V','VI','VII','VIII','IX']

    return Mlist[num//1000]+Clist[(num%1000)//100]+Xlist[(num%100)//10]+Ilist[(num%10)]

print(intToRoman(10))