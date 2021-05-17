INPUT_FILE = "config.cfg"
OUTPUT_FILE = "results.txt"
SHOW_CALC = False
HELP_TEXT = "help.txt"

CFG_SEPARATOR_1 = "="
CFG_SEPARATOR_2 = ","

CFG_TITLE_1 = "DL"
CFG_TITLE_2 = "SILA"
CFG_TITLE_3 = "MOMENT"
CFG_TITLE_4 = "OB" #co z polskimi znakami i jeśli mam OBCIĄŻENIE _CIĄGŁE, OB CIAGŁE, OBCIĄŻENIE_C

from getch import pause_exit
import getopt, sysconfig, sys

def help(help_file):
    try:
        file = open(help_file)
        lines = file.readlines()
        for l in range(len(lines)):    
            print( lines[l])
        ##pause_exit()
    except:
        print("No help file has been found")
        ##pause_exit()

def read_config(file_name):  
    try:
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
            return dic
    except:
        print("Błąd wczytywania pliku", file_name)
        #pause_exit()

   

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

def write_results_to_file(filename, ra, rb):
    try:
        f = open(filename, "w")
        lines = ["Reakcje\n Ra: ", str(ra), "\n Rb: ", str(rb)]
        f.writelines(lines)
        print("Pomyślnie zapisano wyniki w pliku ", filename)
    except:
        print("Wystąpił problem z zapisaniem pliku")
        #pause_exit()

def calc(input, total_length, force_table, continuous_load_table, torque_table, sum1, sum2):
    try:
        f = open(filename, "a")
        lines = ["input", input, "długość belki\n", str(total_length),"siły\n", force_table, "obciążenia\n", continuous_load_table,
                "momenty\n", torque_table, "suma sił i obciążeń\n", str(sum1), "całkowity moment\n", str(sum2)]
        f.writelines("\n", lines)
        print("Pomyślnie zapisano wyniki w pliku ", filename)
    except:
        print("Wystąpił problem z zapisaniem pliku")
        #pause_exit()   

def command_menager(argv):
    try:
        options, args = getopt.getopt(sys.argv[1:], "hi:o:c", ["help", "input=", "output="])

        for opt, arg in options:
            if opt in ('-h', '--help'):
                global HELP_TEXT
                help(HELP_TEXT)
                # #pause_exit()
            if opt in ('-o', '--output'):
                global OUTPUT_FILE
                OUTPUT_FILE = arg
            elif opt in ('-i', '--input'):
                global INPUT_FILE
                INPUT_FILE = arg
            elif opt == '-c':
                global SHOW_CALC
                SHOW_CALC = True
    except getopt.GetoptError:
        print("Nie rozpoznano poprawnie arguemntów. Użyj -h aby uzyskać pomoc")
        #pause_exit()

def main():
    input = read_config(INPUT_FILE)
    
    total_length = get_value_from_config(input, CFG_TITLE_1)
    force_table = get_value_from_config(input, CFG_TITLE_2)
    continuous_load_table = get_value_from_config(input, CFG_TITLE_4) 
    torque_table = get_value_from_config(input, CFG_TITLE_3)
    
    sum1 = total_y_force(force_table, continuous_load_table)
    sum2 = total_tourge(force_table,continuous_load_table,torque_table)
    rb = count_rb(sum2, total_length)
    ra = count_ra(sum1, rb)

    write_results_to_file(OUTPUT_FILE, ra, rb)
    if SHOW_CALC:
        calc()

if __name__ == "__main__":
   main()  

# print("input \n", input)
# print("długość belki\n", total_length)
# print("siły\n",force_table)
# print("obciążenia\n", continuous_load_table)
# print("momenty\n", torque_table)
# print("suma sił i obciążeń\n", sum1)
# print("całkowity moment\n", sum2)



