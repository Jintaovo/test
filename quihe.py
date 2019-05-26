list=[]#定义列表
for i in range(1,1001):#遍历1-1000 得到值（i）
    if i%3==0 and i%5!=0 and i%2!=0:#判断1-1000中那个数可以同时除3且不被5整除的奇数
        list.append(i)#把的的到数添加到列表里面
        a=sum(list)#列表里面的值相加
print(a)#输出和
