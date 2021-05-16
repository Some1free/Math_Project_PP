CFG_SEPARATOR_1 = "="
CFG_SEPARATOR_2 = ","



def read_config(file_name):  
    file = open(file_name)
    lines = file.readlines()

    dic = {}

    for line in lines:
        line = line.upper()
        data = line.strip().replace(" ","").split(CFG_SEPARATOR_1)
        name = data[0]
        data = data[1].split(CFG_SEPARATOR_2)
        
        data = [float(x) for x in data]

        dic[name] = data
    
    print("dic \n", dic)

    return dic

def get_value_from_config(cfg, name):
    name = name.upper()
    results = []
    for n in cfg:
        if name in n:
            results.append(cfg[n])
    return results 

def total_y_force(forces, loads):
    total = 0
    for i in range(len(forces)):
        total = total + forces[i][0]
    for n in range(len(loads)):
        total = total + (loads[n][0]*loads[n][1])
    return total

def total_tourge(forces, loads, torques):
    force_torque = 0
    load_torque = 0
    momentum = 0
    for i in range(len(forces)):
        force_torque = force_torque + forces[i][0]*forces[i][1]
    for n in range(len(loads)):
        load_torque = load_torque + (loads[n][0]*loads[n][1])*(loads[n][2]-loads[n][2]/2)
    for k in range(len(torques)):
        momentum = momentum + torques[k][0]

    return force_torque + load_torque - momentum

def count_rb(torque, length):
    return torque/float(length[0][0])

def count_ra(y_force, Rb):
    return y_force - Rb 

def main():
    file_name = ".\config.txt"

    input = read_config(file_name)

    total_length = get_value_from_config(input, "DL")
    force_table = get_value_from_config(input, "SILA")
    continuous_load_table = get_value_from_config(input, "OB") #co z polskimi znakami i jeśli mam OBCIĄŻENIE _CIĄGŁE, OB CIAGŁE, OBCIĄŻENIE_C
    torque_table = get_value_from_config(input, "MOMENT")

    print("długość belki\n", total_length)
    print("siły\n",force_table)
    print("obciążenia\n", continuous_load_table)
    print("momenty\n", torque_table)

    sum1 = total_y_force(force_table, continuous_load_table)
    print("suma sił i obciążeń\n", sum1)

    sum2 = total_tourge(force_table,continuous_load_table,torque_table)
    print("całkowity moment\n", sum2)

    rb = count_rb(sum2, total_length)
    ra = count_ra(sum1, rb)
    print("Reakcje\n Ra:", ra, "\n Rb:", rb)



main()    

