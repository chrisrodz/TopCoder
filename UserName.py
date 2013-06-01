def newMember(existingNames, newName):
    if newName not in existingNames:
        return newName
    changed = newName
    variant = '1'
    original = newName
    while not changed not in existingNames:
        changed = original+variant
        variant = str(int(variant)+1)
    return changed

e = ["Bart4", "Bart5", "Bart6", "Bart7", "Bart8", "Bart9", "Bart10","Lisa", "Marge", "Homer", "Bart", "Bart1", "Bart2", "Bart3","Bart11", "Bart12"]
n = "Bart"

print newMember(e,n)