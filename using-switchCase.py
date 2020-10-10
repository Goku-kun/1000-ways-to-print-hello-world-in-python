def Switch(case): 
    switcher = { 
        0: "Hello,", 
        1: " ", 
        2: "World!", 
    } 
  
    return switcher.get(case, " ") 
print(Switch(0)+Switch(1)+Switch(2))