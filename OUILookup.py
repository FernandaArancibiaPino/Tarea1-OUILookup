#Python 3.8  Windows 10
import sys, getopt

Lista=list(); Ip=['192', '168', '1', '30']

def Main():
	try:
		#para tener opciones largas, es necesario colocar las opciones cortas respectivas,
		#aunque no se utilicen. En este caso: -r y -m
		options, args = getopt.getopt(sys.argv[1:],"i,m",['ip=','mac=','help'])
	except:
		print("\nError: Parametros incorrectos.\n")
		Uso()

	IP = ''
	MAC  = ''

	for opt, arg in options:
		if opt in ('--help'):
			Uso()
		if opt in ('--ip'):
			IP = arg
		elif opt in ('--mac'):
			MAC = arg

	#RATE y MAX_TIME deben estar ingresadas.
	if IP == '' and MAC == '':
		print("\nError: Faltan parametros obligatorios.\n")
		Uso()
	elif IP != '' and MAC != '':
		print("\nError: No puede ingresar ambos parametros.\n")
		Uso()

	Separar(Entrada("manuf.txt"))
	ip= IP.split('.')
	Comparar(ip, 3, 1)

def Uso():
	print("Uso:\n	test.py --ip <IP> || --mac <MAC> [--help]")
	print("\nParametros:")
	print("	--ip: direccion IP. Obligatorio")
	print("	--mac: direccion MAC. Obligatorio")
	print("	--help: muestra esta pantalla y termina. Opcional")
	exit(1)

def Entrada(archivo):
	arch = open(archivo, 'r', encoding='utf-8')
	lineas = arch.readlines()
	return lineas
	arch.close()

def Separar(l):
	cont=0
	for linea in l:
		linea=linea.strip('\n')
		lineas=linea.split('\t')
		if len(lineas)==3:
			cont+=1
			if cont!=1:
				Lista.append(lineas)

def Comparar(dir, num, caso):
	cont=0
	if caso==1: #Se trabaja con la direccion Ip
		for i in range(0,num):
			if Ip[i]==dir[i]:
				cont+=1
		if cont==num:
			pass
			#MAC address : b4:b5:fe:92:ff:c5
			#Vendor      : Hewlett Packard
		else:
			print("\nError: ip esta fuera de la red de host")
	if caso==2: #Se trabaja con la direccion Mac
		pass

#------------------MAIN------------------
if __name__ == '__main__':
	Main()