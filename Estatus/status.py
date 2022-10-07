import time
import psutil
def checkIfProcessRunning(processName):
        '''Los procesos activos y verificados se deben visualizar en CMD con el comando tasklist'''
        print('Verificando si la aplicacion esta en ejecucion...')
        for proc in psutil.process_iter():
                try:
                        # Check if process name contains the given name string.
                        if processName.lower() in proc.name().lower():
                                return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
        return False;

BraveRunning = True
while BraveRunning:
    if checkIfProcessRunning('brave.exe'): #Nombre del proceso activo o inactivo
        print('El proceso esta activo y en ejecucion...')
        time.sleep(30) # Se espera 30 segundos para volver a realizar el chequeo 
        print('Volviendo a evaluar el proceso...')
    else:
        print('El proceso esta inactivo y no se encuentra en ejecucion.')
        BraveRunning = False # Sets chromeRunning False to exit loop