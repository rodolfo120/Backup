import shutil , zipfile, os

def mover(Directorio_Origen,Directorio_Destino):
   for archivo in os.listdir(Directorio_Origen):
      os.rename(Directorio_Origen+"/"+archivo,Directorio_Destino+"/"+archivo)
        

def copy(Directorio_Origen,Directorio_Destino):
    destino = Directorio_Destino + "/Contenido"
    shutil.copytree(Directorio_Origen,destino)
        
