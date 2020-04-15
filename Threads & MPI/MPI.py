from mpi4py import MPI
import time
import random as random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

diagnosis = "Belum ada" #Kondisi diagnosis awal
suhu = "Belum ada"

if rank == 0:
    print ("rank:",rank,"first condition:",diagnosis)
    
    suhu = round(random.uniform(30,40), 2) # Proses random suhu 30~40
    comm.send(suhu, dest=1) # mengirim suhu ke rank 1

    diagnosis = comm.recv(source=1) # mengambil data dari rank 1
    print("rank",rank,"after condition:",diagnosis)

elif rank == 1:
    print ("rank:",rank,"first condition:",suhu)

    suhu = comm.recv(source=0) # mengambil data dari rank 0
    print ("rank:",rank,"after condition:",suhu)

     # Cek cek suhu
    if suhu < 35.5:
        diagnosis = "Hipotermia"
    elif (suhu >= 35.5) and (suhu <= 37.5):
        diagnosis = "Normal"
    elif suhu > 37.5:
        diagnosis = "Demam"    
    comm.send(diagnosis, dest=0) # mengirim data ke rank 0
