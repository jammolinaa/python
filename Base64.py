import base64
import os
import glob

def image_to_base64(image_path):
    """
    Convierte una imagen a una cadena en Base64.

    :param image_path: Ruta de la imagen a convertir.
    :return: Cadena en Base64 que representa la imagen.
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return encoded_string
    except Exception as e:
        print(f"Ocurrió un error al convertir la imagen: {e}")
        return None

def save_base64_to_txt(image_path, output_directory):
    """
    Convierte una imagen a Base64 y la guarda en un archivo .txt con el mismo nombre en el directorio especificado.

    :param image_path: Ruta de la imagen a convertir.
    :param output_directory: Directorio donde se guardará el archivo .txt.
    :return: None
    """
    # Obtener el nombre de archivo sin la extensión
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    # Crear el nombre del archivo .txt en el directorio de salida
    output_path = os.path.join(output_directory, f"{file_name}.txt")
    
    # Convertir imagen a Base64
    base64_string = image_to_base64(image_path)
    
    if base64_string:
        try:
            # Guardar la cadena Base64 en un archivo .txt
            with open(output_path, "w") as text_file:
                text_file.write(base64_string)
            
            print(f"Imagen convertida y guardada en {output_path}")
        
        except Exception as e:
            print(f"Ocurrió un error al guardar el archivo: {e}")

def process_images_in_directory(directory, output_directory):
    """
    Busca y procesa todas las imágenes en el directorio especificado.

    :param directory: Ruta del directorio donde buscar las imágenes.
    :param output_directory: Directorio donde se guardarán los archivos .txt.
    :return: None
    """
    # Buscar todas las imágenes en el directorio (extensiones comunes: jpg, png, bmp, gif)
    image_paths = glob.glob(os.path.join(directory, "*.[jJpPbBgG][pPnNmMiIfF]*"))
    
    for image_path in image_paths:
        save_base64_to_txt(image_path, output_directory)

# Ruta del directorio donde buscar imágenes
directory_path = r"C:\Users\NCPAPRACTIGH\Pictures\Screenshots"

# Directorio donde se guardarán los archivos .txt (misma carpeta que el archivo .py)
output_directory = os.path.dirname(os.path.abspath(__file__))

# Procesar las imágenes en el directorio especificado
process_images_in_directory(directory_path, output_directory)
