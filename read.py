import re

def read_config(file_name = "config.cfg")
    
    file.open(file_name)
    lines = file.readlines()

    force = {}
    constant_force = {}
    momentum = {}
        
    f=0           
    cf=0
    m=0


    for line in lines:
        data = line.strip().replace(" ","").split(";")
        data.upper()
        print(data)

        if (len(data)==1 and not data[1]) #line==0
            try:
                total_length = float(data[0])
            except:
                print("Podano źle skonfigurowane dane") # w lini 1. Należy podać wyłącznie całkowitą dłuość belki bez jednostki ani znaków specjalnych")

        if(len(data) == 3 and data[1] and data[2])
            try:
                if re.match("MOMENT(.*)", data[0])
                        momentum[m,0] = float(data[1])
                        momentum[m,1] = float(data[2)])
                        m++
                if re.match("SILA(.*)", data[0])
                        force[f,0] = float(data[1])
                        force[f,1] = float(data[2])
                        f++
            except:
                print("Podano źle skonfigurowane dane momnetów lub sił")

        if(len(data) == 4 and data[3])
            try:
                constant_force[cf,0] = float(data[1]*data[2])
                constant_force[cf,1] = float(data[3]-(data[2]/2))
                cf++
            except:
                print("Podano źle skonfigurowane dane obciążenia ciągłego")

    return [force, constant_force, momentum]

# kjghsdkghl

def count_rby()
    {

    }