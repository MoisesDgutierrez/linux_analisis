import os 

class Sysinfo:
    #constructor de la clase
    def __init__(self):

        self.date = "date"
        self.info_system = "lsb_release -a"
        self.hostName = "hostnamectl"
        self.Ram = "free -h"
        print("clse info system corriendo correctamente")

    def fecha_hora(self):
        salida = os.popen(self.date).read()
        salida = str(salida).split(" ")
        salida = salida[0] + " "+ salida[1]+ " " + salida[2] + " " + salida[3] + " " + salida[4]
        return salida

    def operative_system(self):
        salida = os.popen(self.info_system).read()
        salida = str(salida).split("\n")
        salida = salida[1] + "\n" + salida[2] + "\n" + salida[3] + "\n" + salida[4]
        return salida

    def host_name(self):
        salida = os.popen(self.hostName).read()
        salida = str(salida).split("\n")
        salida = salida[0] + "\n" + salida[5] + "\n" + salida[6] + "\n" + salida[7] + "\n" + salida[8] + "\n" + salida[9]
        return salida

    def ram(self):
        salida = os.popen(self.Ram).read()
        return str(salida)

myobjetoinstancia = Sysinfo()
print(myobjetoinstancia.ram())
