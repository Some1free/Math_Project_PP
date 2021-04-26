

def read_config(file_name = " ")
    
    file.open(file_name)
    lines = file.readlines()

    dic = {}

    for line in lines:
        data = line.strip().replace(" ","").split("=")
        print(data)

        if(len(data) == 2 and data[1])
            try:
                dic[data[0].upper()] = float(data[1])
            except:
                print("Podano źle skonfigurowane dane")

    return dic

