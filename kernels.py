import numpy as np

def umbralizar(Array: np.ndarray) -> np.ndarray:

    Umbral = int(input("Ingrese un umbral: "))
    Array[Array>Umbral] = 255
    Array[Array<=Umbral] = 0
    return Array

def identidad(Array: np.ndarray) -> np.ndarray:
  
    return Array * 1

def negativo(Array: np.ndarray) -> np.ndarray:
    
    return Array * -1

def sobel_Vertical()->np.ndarray:
    
    Sobel_Vertical = np.array([[-1,-2,-1],
                               [ 0, 0, 0],
                               [ 1, 2, 1]])
    return Sobel_Vertical

def kernel_Sobel_horizontal()->np.ndarray:
    
    Sobel_horizontal = np.array([[-1,0,1],
                                 [-2,0,2],
                                 [-1,0,1]])
    
    return Sobel_horizontal

def sharpen()->np.ndarray:
    
    Sharpen = np.array([[-1,-1,-1],
                        [-1, 8,-1],
                        [-1,-1,-1]])
    
    return Sharpen

def gaussian_5x5()->np.ndarray:

    gaussian_5x5 = np.array([[1,4,6,4,1],
                             [4,16,24,16,4],
                             [6,24,36,24,6],
                             [4,16,24,16,4],
                             [1,4,6,4,1]])
    
    return gaussian_5x5

def unsharpen_5x5()->np.ndarray:
    
    Unsharpen_5x5 = np.array([[-1,-4 ,-6 ,-4 ,-1],
                              [-4,-16,-24,-16,-4],
                              [-6,-24,476,-24,-6],
                              [-4,-16,-24,-16,-4],
                              [-1,-4 ,-6 ,-4 ,-1]])

    return Unsharpen_5x5

def boxBlur_11x11()->np.ndarray:

    Box_Blur = np.ones((11, 11))

    return Box_Blur

def lens_blur_11x11()->np.ndarray:
    
    Lens_blur_11x11 = np.array([[0,0,0,0,0,1,0,0,0,0,0],
                                [0,0,0,1,1,1,1,1,0,0,0],
                                [0,0,1,1,1,1,1,1,1,0,0],
                                [0,1,1,1,1,1,1,1,1,1,0],
                                [0,1,1,1,1,1,1,1,1,1,0],
                                [1,1,1,1,1,1,1,1,1,1,1],
                                [0,1,1,1,1,1,1,1,1,1,0],
                                [0,1,1,1,1,1,1,1,1,1,0],
                                [0,0,1,1,1,1,1,1,1,0,0],
                                [0,0,0,1,1,1,1,1,0,0,0],
                                [0,0,0,0,0,1,0,0,0,0,0]])
    
    return Lens_blur_11x11

def motionBlur_11x11()->np.ndarray:

    Motion_blur = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    return Motion_blur


def chequeo_Numerico(Texto_Num:str) -> bool:   
    """
    Summary
    -------
    Chequea que un String que esta separado con espacios, este compuesto de Numeros Enteros o Flotantes (Positivos o Negativos).
    Se utiliza para chequear los valores ingresados en el Kernel Personalizado.

    Parameters
    ----------
    Texto_Num : str
                Los valores ingresados por el usuario de la Fila n.

    Returns
    -------
    Bool
        True si la Lista contiene solamente Numeros Enteros o Flotantees.

        False si se ingresa cualquier otra cosa que no sea un Numero Entero o Flotante.

    """
    Lista_Num = Texto_Num.split()
    Chequeo = 0
    for elemento in Lista_Num:
        if elemento.replace(".", "",1).isdecimal() or (elemento[0] == "-" and elemento[1:].replace(".", "",1).isdecimal()):
            Chequeo += 1
    if Chequeo == len(Lista_Num):
        return True
    else: 
        return False
    

def kernel_personalizado() -> np.ndarray:
    """
     Summary
    -------
    Crea un Kernel Personalizado. 
    Pidiendole al usuario el tamaño del Kernel y los valores de cada fila. 
    En caso de ingresar valores invalidos, se le pedira al usuario que vuelva a ingresarlos.

    Returns
    -------
    np.ndarray
        Devuelve el Kernel Personalizado con el tamaño y los valores ingresados por el usuario.

    """
    tamaño = int(input("Ingrese el tamaño del Kernel: "))
    while tamaño % 2 == 0 or tamaño < 0: #Chequea que el Kernel sea impar y positivo.
        tamaño =  int(input("El tamaño del Kernel es invalido. \nIngrese el tamaño del Kernel: "))
    kernel = np.zeros((tamaño,tamaño))
    for fila in range(tamaño):
        valores_fila = input(f"Ingrese los valores de la fila {fila} separados por espacios: ")
        while len(valores_fila.split()) != tamaño or not chequeo_Numerico(valores_fila): #Chequea que se ingresen la misma cantidad de valores que el kernel y que no se puedan ingresar strings u otras cosas.
            valores_fila = input(f"Valores de Fila {fila} invalidos. \nVuelva a Ingresar los valores de la fila {fila} separados por espacios: ")
        fila_a_editar = valores_fila.split()
        fila_editada = np.array([float(elemento) for elemento in fila_a_editar])
        kernel[fila] = fila_editada
    return kernel