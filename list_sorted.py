word=input("adjalszot")
word=word.split()

for i in word:
    if len(i)==5: print(i,end=', ')

print()

if "romejo" in word:
    print("van romejo, dikk man hol van ez a devla:", word.index("romejo"))
else:
    print("esku nem lattam romejot")

print(sorted(word))
print(word)
word.sort()
print(word)