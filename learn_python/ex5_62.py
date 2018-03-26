from ex5_6 import displayInventory
def addToInventory(inv, addItems):
    
    for k in addItems:
        if k in inv.keys():
            inv[k] += 1
        else:
            inv[k] = 1

inv = {'gold coin': 42, 'rope': 1}
dragonloot = ['gold coin', 'dagger', 'gold coin', 'ruby']

addToInventory(inv, dragonloot)
displayInventory(inv)
