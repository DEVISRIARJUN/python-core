# --- STEP 1: Filter raw transactions into clean and invalid files ---
# We open clean.txt and invalid.txt in "w" mode to clear out old runs
with open("transaction.txt", "r") as f, \
     open("clean.txt", "w") as clean_file, \
     open("invalid.txt", "w") as invalid_file:
     
    for i in f:
        l = i.strip().split(",")
        
        if len(l) == 3:
            # Fixed a slight check: ensure the category is not empty at all
            if l[1].isdigit() and l[0] != "" and l[2].strip() != "" and "-" not in l[1]:
                clean_file.write(f"{i}")
            else:
                invalid_file.write(f"{i}")
        else:
            invalid_file.write(f"{i}")

# --- STEP 2: Generate initial metrics report ---
is_sum = 0
valid_records = 0
invalid_records = 0

with open("report2.txt", "w") as f:
    with open("clean.txt", "r") as c:
        for i in c:
            valid_records += 1
            l = i.strip().split(",")  # Added .strip() to safely isolate the number
            is_sum += int(l[1])
            
    with open("invalid.txt", "r") as inv:
        for _ in inv:
            invalid_records += 1
            
    f.write(f"total records: {valid_records + invalid_records}\n")
    f.write(f"valid records: {valid_records}\n")
    f.write(f"invalid records: {invalid_records}\n")
    f.write(f"total revenue: {is_sum}\n")

# --- STEP 3: Aggregate Category spending and append to report ---
d = {}
with open("clean.txt", "r") as f:
    for i in f:
        l = i.strip().split(",")  # ⭐ CRITICAL FIX: Added .strip() to clean 'l[2]' line breaks
        print(l)  # Shows you the clean output list in terminal
        
        category = l[2]
        amount = int(l[1])
        
        if category not in d:
            d[category] = amount
        else:
            d[category] += amount

with open("report2.txt", "a") as f:
    for i, j in d.items():
        f.write(f"{i}:{j}\n")
