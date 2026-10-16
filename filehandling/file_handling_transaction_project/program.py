# PROJECT 1: TRANSACTION DATA PIPELINE
# 1. Read transactions.txt line by line
# 2. Validate each row
# 3. Write valid rows to clean.txt
# 4. Write invalid rows with reason to error.log
# 5. Use flush() for logs
# 6. Generate report.txt with:
#    - Total Records
#    - Valid Records
#    - Invalid Records
#    - Total Revenue
#    - Category-wise Revenue
# 7. Use seek() or tell() somewhere in the program


# from webbrowser import open_new

# Open the error.txt file along with your transaction file
with open("transactions.txt","r") as f, open("error.txt", "w") as error_file:
    for i in f:
        if not i.strip():  # Skip completely empty lines to prevent crashes
            continue
            
        original_row = i.strip()
        l = i.strip().split(",")
        
        if len(l) == 3:
            # Check for specific real-time errors
            reason = None
            if l[0] == "":
                reason = "Missing user ID"
            elif l[1] == "":
                reason = "Missing amount"
            elif "-" in l[1]:
                reason = "Negative amount"
            elif not l[1].isdigit():
                reason = "Non-numeric amount"
            elif l[2].strip() == "":
                reason = "Missing or empty category"
                
            # Route based on validation
            if reason is None:
                with open("clean.txt","a") as a:
                    a.write(f"{i}")
            else:
                # Log the error in real-time to error.txt
                error_file.write(f"{original_row} -> {reason}\n")
                error_file.flush()
                
                with open("invalid.txt", "a") as a:
                    a.write(f"{i}")
        else:
            # Handle structurally broken rows (e.g., missing columns entirely)
            error_file.write(f"{original_row} -> Invalid row format (must have 3 parts)\n")
            error_file.flush()
            with open("invalid.txt","a") as a:
                a.write(i)

is_sum=0
valid_records=0
invalid_records=0

with open("report2.txt","w+") as f:
    with open("clean.txt","r") as c:
        for i in c:
            if not i.strip():
                continue
            valid_records+=1
            l=i.strip().split(",")
            is_sum+=int(l[1])
    with open("invalid.txt","r") as i:
        for _ in i:
            if not _.strip():
                continue
            invalid_records+=1
    f.write(f"total records: {valid_records+invalid_records}\n")
    f.write(f"valid records: {valid_records}\n")
    f.write(f"invalid records: {invalid_records}\n")
    f.write(f"total revenue: {is_sum}\n")

d={}
with open("clean.txt","r") as f:
    for i in f:
        if not i.strip():
            continue
        l=i.strip().split(",")
        print(l)
        if l[2] not in d:
            d[l[2]]=int(l[1])
        else:
            d[l[2]]+=int(l[1])

with open("report2.txt","a") as f:
    for i,j in d.items():
        f.write(f"{i}:{j}\n")
