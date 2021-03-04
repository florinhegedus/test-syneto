import psutil

def power(cpu_max_power, ram_max_power):
	psutil.virtual_memory() 
	dict(psutil.virtual_memory()._asdict())
	power = psutil.cpu_percent(1)*cpu_max_power/100.0 + psutil.virtual_memory().percent*ram_max_power/100.0
	return power

print("Power usage: " + str(power(400,200)) + "W")