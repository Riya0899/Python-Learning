import os

def generateTable(n):
    table = ""

    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    os.makedirs("table", exist_ok=True)  # ✅ creates folder if missing

    with open(f"table/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generateTable(i)
