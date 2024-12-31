import numpy as np
from PIL import Image as img
import kernels as kernel
import processing as edit
from processing import convolucion 
from processing import padding
import os

def kernels (operacion:int)->np.ndarray:
    """
    Summary
    ---------
    contiene un diccionario de funciones que cada funcion tiene el array de un kernel asociado al ser llamada,
    pide el filtro que se le quiere aplicar a la imagen y devuelve este mismo (kernel)
    
    Parameters
    ----------
    operacion: int
                operacion es un numero entero entre [1,12] que determina el kernel 
                con el cual se va filtrar la imagen 
    
    Returns
    ---------
    diccionario_kernels[operacion]: callable
                                    Devuelve una funcion que llamando a su clave asociada
                                    en un diccionario de funciones, este funcion al llamarse ()
                                    devuelve el array asociado a cada kernel
    """
    
    diccionario_kernels = {1: kernel.umbralizar, 2:kernel.identidad, 3:kernel.negativo,
            4:kernel.sobel_Vertical, 5:kernel.kernel_Sobel_horizontal, 6:kernel.sharpen, 7:kernel.gaussian_5x5,
            8:kernel.unsharpen_5x5, 9:kernel.boxBlur_11x11 , 10:kernel.lens_blur_11x11,
            11:kernel.motionBlur_11x11, 12:kernel.kernel_personalizado
            }
    try:
        return diccionario_kernels[operacion]
    except:
            return "Operación inválida"

    
    
def menu_opciones():

    print("")
    print("OPERACIONES")
    print("-----------")
    print(f"1. Umbralizar\n2. Identidad\n3. Negativo\n4. Sobel vertical\n5. Sobel horizontal\n6. Sharpen\n7. Gaussian\n8. Unsharpen\n9. Box blur\n10. Lens blur\n11. Motion blur\n12. Kernel personalizado\n")


def main():
    imagen_a_editar = input("Ingrese el nombre de la imagen: ") 
    try:
        imagen = img.open(os.path.join("test_images", imagen_a_editar))
        imagen_array = np.array(imagen) 
        menu_opciones()
        operacion = int(input("Ingrese número de la operación: "))
        filtro = kernels(operacion)
        if filtro == "Operación inválida":
            print("Operación inválida")
        elif operacion <= 3:
            imagen_editada = filtro(imagen_array)
        else:
            filas, columnas = imagen_array.shape[:2]
            kernel = filtro()
            tamaño_kernel = kernel.shape[0]
            imagen_padeada = padding(imagen_array,filas,columnas,tamaño_kernel)
            imagen_convolucionada = convolucion(imagen_array,imagen_padeada,kernel)
            imagen_editada = edit.normalizado(imagen_convolucionada)

        if filtro == "Operación inválida":
            pass
        else:
            nombre_salida = input("Ingrese el nombre de salida de la imagen: ")
            imagen_editada = img.fromarray(imagen_editada.astype("uint8"), imagen.mode)
            try:
                imagen_editada.save(os.path.join("output_images", nombre_salida))
                print("")
                print("Operacion realizada con exito!")
            except:
                print(f"{nombre_salida} es inválido")
    except:
         print("imagen no encontrada")    
    
    
if __name__ == "__main__":
    main()