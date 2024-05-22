import numpy as np



def readin():

    init = open("source/temp.init")

    
    layer = ''
    friqrt = ''
    profile = ''
    inangle = ''
    hw0 = ''
    hw1 = ''
    hws = ''
    h_nm = ''
    
    
    # search start name layer
    char = init.read(1)
    while (char != "\'"):
        char = init.read(1)
        
    # read name layer   
    char = init.read(1)    
    while (char != "\'"):
        layer = layer + char
        char = init.read(1)
        
    # search start name friqrt
    char = init.read(1)
    while (char != "\'"):
        char = init.read(1)
        
    # read name friqrt   
    char = init.read(1)    
    while (char != "\'"):
        friqrt = friqrt + char
        char = init.read(1)
    
    # search start name profile
    char = init.read(1)
    while (char != "\'"):
        char = init.read(1)
        
    # read name profile   
    char = init.read(1)    
    while (char != "\'"):
        profile = profile + char
        char = init.read(1)
    
    # search start incidence angle
    char = init.read(1) 
    while (char != "\n"):
        char = init.read(1)
    
    # read incidence angle 
    char = init.read(1) 
    while (char != " "):
        inangle =  inangle + char
        char = init.read(1)   
    inangle = float(inangle) 
    
    # search start photon energy 0
    char = init.read(1) 
    while (char != "\n"):
        char = init.read(1)
    
    # read photon energy 0 
    char = init.read(1)
    while (char != ","):
        hw0 =  hw0 + char
        char = init.read(1)    
    hw0 = float(hw0)
    
    # search start photon energy 1
    char = init.read(1)
    while (char == " "):
        char = init.read(1)    
    
    # read photon energy 0 
    while (char != " "):
        hw1 =  hw1 + char
        char = init.read(1) 
    hw1 = float(hw1)  
      
    # search step hw
    char = init.read(1) 
    while (char != "\n"):
        char = init.read(1)
    
    # read step hw
    char = init.read(1)
    while (char != " "):
        hws =  hws  + char
        char = init.read(1) 
    hws  = float(hws) 
    
    # search start step z
    char = init.read(1) 
    while (char != "\n"):
        char = init.read(1)
    
    # read step z
    char = init.read(1)
    while (char != " "):
        h_nm =  h_nm  + char
        char = init.read(1) 
    h_nm  = float(h_nm ) 

    init.close
    
    return layer, friqrt, profile, inangle, hw0, hw1, hws, h_nm

def readlayer(layer1):
    
    layer = open('source/temp.str')
    
    NL = ''
    L = [0]
    n = []
    
    # search NL
    char = layer.read(1)
    while (char != "\n"):
        char = layer.read(1)    
        
    # read NL  
    char = layer.read(1)
    while (char != " "):
        NL = NL + char
        char = layer.read(1)
    NL = int(NL)  
    
    # search n0
    char = layer.read(1)
    while (char != "("):
        char = layer.read(1) 
    
    # read n0
    nn = ''    
    char = layer.read(1)
    while (char != ","):
        nn = nn + char
        char = layer.read(1)
    nre = (float(nn))
    nn = ''
    char = layer.read(1)
    while (char != ")"):
        nn = nn + char
        char = layer.read(1)
    nim = (float(nn))   
    n.append(nre + 1j*nim)
    
    # read L n
    char = layer.read(1)
    while (char != "\n"):
        char = layer.read(1)  
        
    for i in range (NL):
        char = layer.read(1)
        while (char != " "):
            char = layer.read(1)
    
        ll = ''
        char = layer.read(1)
        while (char != "("):
            ll = ll + char
            char = layer.read(1)
        L.append(float(ll))      
        
        nn = ''    
        char = layer.read(1)
        while (char != ","):
            nn = nn + char
            char = layer.read(1)
        nre = (float(nn))
        nn = ''
        char = layer.read(1)
        while (char != ")"):
            nn = nn + char
            char = layer.read(1)
        nim = (float(nn))   
        n.append(nre + 1j*nim)
        
        char = layer.read(1)
        while (char != "\n"):
            char = layer.read(1) 
        
    # read nN
    char = layer.read(1)
    while (char != "("):
        char = layer.read(1) 
         
    nn = ''    
    char = layer.read(1)
    while (char != ","):
        nn = nn + char
        char = layer.read(1)
    nre = (float(nn))
    nn = ''
    char = layer.read(1)
    while (char != ")"):
        nn = nn + char
        char = layer.read(1)
    nim = (float(nn))   
    n.append(nre + 1j*nim)        

    layer.close
    
    return NL, L, n
    

def writefriqrt(friqrt, E0, El, r1, t1, rs1, ts1, eigenfreq):
    f = open("data/" + friqrt, 'w')
        
    f.write('hw ')
    for i in eigenfreq:
        f.write('(')
        for item in"".join(str(np.real(i))):    
           f.write(item)
        f.write(',')    
        for item in"".join(str(np.imag(i))):    
            f.write(item)
        f.write(')')      
        f.write(' ')   
    f.write('\n') 
        
    f.write('r1 ')
    for i in r1:
        f.write('(')
        for item in"".join(str(np.real(i))):    
           f.write(item)
        f.write(',')    
        for item in"".join(str(np.imag(i))):    
            f.write(item)
        f.write(')')      
        f.write(' ')   
    f.write('\n')
    
    f.write('t1 ')
    for i in t1:
        f.write('(')
        for item in"".join(str(np.real(i))):    
           f.write(item)
        f.write(',')    
        for item in"".join(str(np.imag(i))):    
            f.write(item)
        f.write(')')      
        f.write(' ')   
    f.write('\n')
    
    f.write('r2 ')
    for i in rs1:
        f.write('(')
        for item in"".join(str(np.real(i))):    
           f.write(item)
        f.write(',')    
        for item in"".join(str(np.imag(i))):    
            f.write(item)
        f.write(')')      
        f.write(' ')
    f.write('\n')
    
    f.write('t2 ')    
    for i in ts1:
        f.write('(')
        for item in"".join(str(np.real(i))):    
           f.write(item)
        f.write(',')    
        for item in"".join(str(np.imag(i))):    
            f.write(item)
        f.write(')')      
        f.write(' ')
    f.write('\n')    
    
    f.write('E(0)+ ')
    for i in E0:
        f.write('(')
        for item in"".join(str(np.real(i))):    
           f.write(item)
        f.write(',')    
        for item in"".join(str(np.imag(i))):    
            f.write(item)
        f.write(')')      
        f.write(' ')
    f.write('\n')    
    
    f.write('E(L)- ')
    for i in El:
        f.write('(')
        for item in"".join(str(np.real(i))):    
           f.write(item)
        f.write(',')    
        for item in"".join(str(np.imag(i))):    
            f.write(item)
        f.write(')')      
        f.write(' ')
    f.write('\n')    
        
    f.close()
    
    
    