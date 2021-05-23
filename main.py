INPUT_FILE = "config.cfg"
OUTPUT_FILE = "results.txt"
HELP_TEXT = "help.txt"

CFG_SEPARATOR_1 = "="
CFG_SEPARATOR_2 = ","

CFG_TITLE_1 = "DL"
CFG_TITLE_2 = "SILA"
CFG_TITLE_3 = "MOMENT"
CFG_TITLE_4 = "OB"

from getch import pause_exit
import getopt, sysconfig, sys
import json

def command_menager(argv):
    HELP_STATUS = False
    SHOW_CALC = False
    ERROR = False
    try:
        options, args = getopt.getopt(sys.argv[1:], "hi:o:c", ["help", "input=", "output="])
        
        for opt, arg in options:
            if opt == "-c":
                SHOW_CALC = True
            elif opt in ('-h', '--help'):
                global HELP_TEXT
                help(HELP_TEXT)
                HELP_STATUS = True
                #pause_exit()
            if opt in ('-o', '--output'):
                global OUTPUT_FILE
                OUTPUT_FILE = arg
            elif opt in ('-i', '--input'):
                global INPUT_FILE
                INPUT_FILE = arg
            
    except getopt.GetoptError as err:
        print("Nie rozpoznano poprawnie arguemntów. Użyj -h aby uzyskać pomoc")
        print(err)
        ERROR = True
    
    return HELP_STATUS, SHOW_CALC, ERROR

def show_help(help_file):
    try:
        file = open(help_file)
        lines = file.readlines()
        for l in range(len(lines)):    
            print(lines[l])
        ##pause_exit()
    except:
        print("No help file has been found")
        ##pause_exit()

def read_config(file_name):  
    dic = {}
    status = False
    try:
        file = open(file_name)
        lines = file.readlines()   

        for line in lines:
            line = line.upper()
            data = line.strip().replace(" ","").split(CFG_SEPARATOR_1)
            name = data[0]
            data = data[1].split(CFG_SEPARATOR_2)
            
            data = [float(x) for x in data]

            dic[name] = data
        status = True
    except:
        print("Błąd wczytywania pliku / niepoprawny format danych w pliku", file_name)

    return dic, status
 
def get_value_from_config(cfg, name):
    name = name.upper()
    results = []
    for n in cfg:
        if name in n:
            results.append(cfg[n])
    return results

def get_values(filename, title_1, title_2, title_3, title_4):
    total_length = get_value_from_config(filename, title_1)
    force_table = get_value_from_config(filename, title_2)
    torque_table = get_value_from_config(filename, title_3)
    continuous_load_table = get_value_from_config(filename, title_4) 

    return total_length, force_table, continuous_load_table, torque_table

def check_table(table, nr_of_inputs, can_be_empty):
    status = True
    if len(table) == 0 and can_be_empty:
        status = True
    elif len(table) == 0:
        status = False
    else:    
        for i in range(len(table)):
            if len(table[i])<(nr_of_inputs):
                status = False
            # else:     
            #     for n in range(nr_of_inputs):
            #         if table[i][n]: 
            #             status = False
    return status

def check_values(total_length, force_table, continuous_load_table, torque_table):
    status = False

    tl_status = check_table(total_length, 1, 0)
    ft_status = check_table(force_table, 2, 1)
    clt_status = check_table(continuous_load_table, 3,1)
    tt_status = check_table(torque_table, 1, 1)
    
    if tl_status and ft_status and clt_status and tt_status:
        status = True
    
    return status

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
       
def equations_1(total_length, force_table, continuous_load_table, torque_table):
    sum1 = total_y_force(force_table, continuous_load_table)
    sum2 = total_tourge(force_table,continuous_load_table,torque_table)
    
    return sum1, sum2

def equations_final(sum1, sum2, total_length):
    rb = count_rb(sum2, total_length)
    ra = count_ra(sum1, rb)

    return ra, rb

def write_results_to_file(filename, ra, rb):
    try:
        f = open(filename, "w")
        lines = ["Reakcje\n Ra: ", str(ra), "\n Rb: ", str(rb)]
        f.writelines(lines)
        f.close()
        print("Pomyślnie zapisano wyniki w pliku ", filename)
    except:
        print("Wystąpił problem z zapisaniem pliku (wyniki)")
        #pause_exit()

def write_calc_to_file(filename, input, total_length, force_table, continuous_load_table, torque_table, sum1, sum2):
    try:
        file = open(filename, "a")
        lines = ["\ninput\n", json.dumps(input),
                "\ndlugosc belki\n", str(total_length),
                "\nsily\n", json.dumps(force_table), 
                "\nobciazenia\n", json.dumps(continuous_load_table),
                "\nmomenty\n", json.dumps(torque_table),
                "\nsuma sil i obciazen\n", str(sum1),
                "\ncalkowity moment\n", str(sum2)]
        file.writelines(lines)
        file.close()
        print("Pomyślnie zapisano obliczenia w pliku ", filename)
    except:
       print("Wystąpił problem z zapisaniem obliczeń")

def program(hlp, calculations, err):
    if not err:
        if hlp:
            show_help(HELP_TEXT)
        else:
            input, load_complete = read_config(INPUT_FILE)
            if load_complete:
                total_length, force_table, continuous_load_table, torque_table = get_values(input, CFG_TITLE_1, CFG_TITLE_2, CFG_TITLE_3, CFG_TITLE_4)
                is_good = check_values(total_length, force_table, continuous_load_table, torque_table)

                if is_good:
                    sum1, sum2 = equations_1(total_length, force_table, continuous_load_table, torque_table)
                    ra, rb = equations_final(sum1, sum2, total_length)
                    write_results_to_file(OUTPUT_FILE, ra, rb)
                    if calculations:
                        write_calc_to_file(OUTPUT_FILE, input, total_length, force_table, continuous_load_table, torque_table, sum1, sum2)
                else:
                    print("Blad podanych wartosci / za malo danych")

def main():
    hlp, calculations, err = command_menager(sys.argv[1:])
    program(hlp, calculations, err)

if __name__ == "__main__":
   main()  
