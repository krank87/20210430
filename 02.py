

cost = int(input("請輸入度數"))

if cost <=120:
    summer=cost*2.1
    nosummer=cost*2.1
    print("Summer months"+str(summer),"Non-Summer months"+str(nosummer))

elif cost <=330:
    summer=2.1*120+(cost-120)*3.02
    nosummer=2.1*120+(cost-120)*2.68
    print("Summer months"+str(summer),"Non-Summer months"+str(nosummer))

elif cost <=500:
    summer=2.1*120+(330-120)*3.02+(cost-330)*4.39
    nosummer=2.1*120+(330-120)*2.68+(cost-330)*3.61
    print("Summer months"+str(summer),"Non-Summer months"+str(nosummer))

elif cost <=700:
    summer=2.1*120+(330-120)*3.02+(500-330)*4.39+(cost-500)*4.97
    nosummer=2.1*120+(330-120)*2.68+(500-330)*3.61+(cost-500)*4.01
    print("Summer months"+str(summer),"Non-Summer months"+str(nosummer))
elif cost >700:
    summer=2.1*120+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97+(cost-700)*5.63
    nosummer=2.1*120+(330-120)*2.68+(500-330)*3.61+(700-500)*4.01+(cost-700)*4.5
    print("Summer months"+str(summer),"Non-Summer months"+str(nosummer))