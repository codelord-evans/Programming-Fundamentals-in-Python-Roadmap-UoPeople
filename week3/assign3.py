#Write a new recursive function countup that expects a negative argument and counts “up” from that number. Output from running the function should look something like this: 
# >>> countup(-3) 
# -3 
# -2 
# -1 
# Blastoff! 

def countup(n):
    print(n)
    return "Blastoff!" if n >= -1 else countup(n + 1)

result = countup(-3)
print(result)

