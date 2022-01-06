machine_data = {10:"Large",20:"XLarge",40:"2XLarge",80:"4XLarge",160:"8XLarge",320:"10XLarge"}
city = ["New York","India","China"]
nmap = {10:120,20:230,40:450,80:774,160:1400,320:2820}
imap = {10:140,20:0,40:413,80:890,160:1300,320:2970}
cmap = {10:110,20:200,40:0,80:670,160:1180,320:0}
map = [nmap,imap,cmap]

# from line 10 to line 31 we obtain 3 arrays ndata,idata,cdata which stores unit in ascending order of money required per unit

machine_val = [10,20,40,80,160,320]
money_data = [[120,140,110,0],[230,0,200,1],[450,413,0,2],[774,890,670,3],[1400,1300,1180,4],[2820,2970,0,5]]
multiplier = [32,16,8,4,2,1]
newyork = []
india = []
china = []
ndata,idata,cdata = [],[],[]
for i in range(6):
    money_data[i][0] = money_data[i][0]*multiplier[i] 
    money_data[i][1] = money_data[i][1]*multiplier[i]
    money_data[i][2] = money_data[i][2]*multiplier[i] 
for i in money_data:
    newyork.append([i[0],i[3]])
    india.append([i[1],i[3]])
    china.append([i[2],i[3]])
india.sort()
newyork.sort()
china.sort()
for i in range(6):
    ndata.append(machine_val[newyork[i][1]])
    idata.append(machine_val[india[i][1]])
    cdata.append(machine_val[china[i][1]])
units = [ndata,idata,cdata]

# this functions gives us the required output

def myfunction():
    print("No of hours machine is required to run:")
    hours = int(input())
    print("No of units are required:")
    capacity = int(input())
    print()

    for i in range(3):
        left = capacity
        sm = 0
        res = {}
        for j in range(6):
            if units[i][j] <= left and map[i][units[i][j]] >0:
                num = left//units[i][j]
                left = left - num*units[i][j]
                sm += map[i][units[i][j]]*num*hours
                res[machine_data[units[i][j]]] = num

        print(f"Region:{city[i]}")
        print(f"Total cost:{sm}")
        print(f"Machines:{res}")
        print()
    
myfunction()



