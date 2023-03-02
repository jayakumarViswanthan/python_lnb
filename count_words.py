String = """Nory was34 a Catholic because her mother was a Catholic, and Nory's mother was a Catholic because her father was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been."""
new_String=[]

for i in (String):
        if ord(i) >= 48 and ord(i) < 123:
            if ord(i)>=65 or ord(i)<=57:
                print(i)
                if ord(i) in (range(91,97)):
                    continue
                else:
                    new_String.append(i)
print("".join(new_String))
