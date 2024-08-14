import os
import glob

def delete_txt_files(directory):
    """
    Borra todos los archivos .txt en el directorio especificado.

    :param directory: Ruta del directorio donde se borrarán los archivos .txt.
    :return: None
    """
    try:
        # Buscar todos los archivos .txt en el directorio
        txt_files = glob.glob(os.path.join(directory, "*.txt"))
        
        # Borrar cada archivo .txt encontrado
        for txt_file in txt_files:
            os.remove(txt_file)
            print(f"Archivo eliminado: {txt_file}")
        
        print("Proceso de eliminación completado.")
    
    except Exception as e:
        print(f"Ocurrió un error al eliminar los archivos: {e}")

# Ruta del directorio donde se eliminarán los archivos .txt
directory_path = r"C:\Users\NCPAPRACTIGH\Desktop\PYTHON"

# Ejecutar la función para borrar los archivos .txt
delete_txt_files(directory_path)
