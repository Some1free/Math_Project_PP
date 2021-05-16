import re

file_name = "config.cfg"


def read_config(file_name):
    {     
        my_file = file.open(file_name)
        lines = file.readlines()

        force = {}
        continuous_force = {}
        momentum = {}
            
        f=0           
        cf=0
        m=0


        for line in lines:
        {   
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

            if(len(data) == 4 and data[1] and data[2] and data[3])
                try:
                    continuous_force[cf,0] = float(data[1]*data[2])
                    continuous_force[cf,1] = float(data[3]-(data[2]/2))
                    cf++
                except:
                    print("Podano źle skonfigurowane dane obciążenia ciągłego")
        }

        return force, continuous_force, momentum
    }


# co jest zwracane i jak się odwołać
# czy on zwraca macierz 2 wymiarową? (force, itd...) 
# jak sobie zrobić podsumy, albo sumowanie zależne od ilości 

# force_total = sum(i: (force[i, 0]*force[i,1]))
# momnetum_total = sum(i: (momentum[i, 0]*momentum[i,1]))
# continuous_force_total = sum(i: (continuous_force[i, 0]*continuous_force[i,1]))

def total(table_name, x):
        {
            for i in x
                total = total + table_name[i,0]*table_name[i,1]
            return total
        }

def count_rb(force_total, momentum_total,total_length):
            {
                Rb = (force_total+momentum_total)/total_length
                return Rb
            }


def count_ra(force_total, continuous_force_total, Rb):
    {
        Ra = force_total + continuous_force_total - Rb 
        return Ra
    }


def counting_values(force, continuous_force, momentum):
    {
        force_total = total(force, f)
        momentum_tota = total(momentum, m)
        ontinuous_force_total = total(continuous_force, cf)

        count_rb(force_total, momentum_total,total_length)
        count_ra(force_total, continuous_force_total, Rb)

    }


def main():
    {
        file_name = "config.cfg"
        read_config(file_name)
        counting_values()




    }
