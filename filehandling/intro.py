
with open("transactions.txt","r") as f:
    for i in f:
        l=i.split(",")
        # print(l)
        if len(l)==3:
            if l[1].isdigit() and l[0]!="" and l[2]!=" " and "-" not in l[1]:
                with open("clean.txt","a") as a:
                    a.write(f"{i}")
            else:
                with open("invalid.txt", "a") as a:
                    a.write(f"{i}")
        # else:
        #     with open("invalid.txt","a") as a:
        #         a.write(i)
is_sum=0
valid_records=0
invalid_records=0
with open("report2.txt","x+") as f:
    with open("clean.txt","r") as c:
        for i in c:
            valid_records+=1
            l=i.split(",")
            is_sum+=int(l[1])
    with open("invalid.txt","r") as i:
        for _ in i:
            invalid_records+=1
    f.write(f"total records: {valid_records+invalid_records}\n")
    f.write(f"valid records: {valid_records}\n")
    f.write(f"invalid records: {invalid_records}\n")
    f.write(f"total revenue: {is_sum}\n")
d={}
with open("clean.txt","r") as f:
    for i in f:
        l=i.split(",")
        print(l)
        if l[2] not in d:
            d[l[2]]=int(l[1])
        else:
            d[l[2]]+=int(l[1])
with open("report2.txt","a") as f:
    for i,j in d.items():
        f.write(f"{i}:{j}\n")




