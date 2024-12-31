import numpy as np

def padding(Array: np.ndarray,Filas_Array:int, Columnas_Array: int ,Kernel_size: int =3 ) -> np.ndarray:
    """
      Summary
    -------
    Realiza el Padding de la Matriz de la imagen(Array) en base al tamaño de la Matriz de la imagen y el tamaño del Kernel.
    El Padding utiliza los valores vecinos para rellenar las nuevas filas y columnas.
    
    Parameters
    ----------
    Array : np.ndarray
            Matriz de la imagen sin paddear.
    Filas_Array y Columnas_Array :  int
                                    Es el tamaño en filas y columnas de la Matriz de la imagen.

    Kernel_size : int, opcional
                  Tamaño del Kernel con el cual se va a realizar la convolucion. (Default: 3)
    
    Returns
    -------
    Devuelve una nueva Matriz con el Padding(relleno).

    """
    Aumento_Padding = Kernel_size - 1
    Mitad_Padding = Aumento_Padding // 2  #Medio Padding
    Array_Padding_Shape = np.array(Array.shape)
    Array_Padding_Shape[:2] += Aumento_Padding  #Agregandole el Aumento a la Matriz

    Matriz_Padding = np.zeros(Array_Padding_Shape) #Matriz Padding Base  
    Matriz_Padding[Mitad_Padding : Filas_Array + Mitad_Padding , Mitad_Padding : Columnas_Array + Mitad_Padding] = Array  #Centro
    Matriz_Padding[0 : Mitad_Padding , Mitad_Padding : Columnas_Array + Mitad_Padding] = Array[0]  #Borde Superior
    Matriz_Padding[Filas_Array + Mitad_Padding : , Mitad_Padding : Columnas_Array + Mitad_Padding] = Array[-1] #Borde Inferior
    Matriz_Padding[Mitad_Padding : Filas_Array + Mitad_Padding, 0 : Mitad_Padding] = Array[:, 0:1]  #Borde Izquierdo
    Matriz_Padding[Mitad_Padding : Filas_Array + Mitad_Padding , Columnas_Array + Mitad_Padding :] = Array[:, -1:] #Borde Derecho
    Matriz_Padding[0 : Mitad_Padding , 0 : Mitad_Padding] = Array[0][0] #Esquina Superior Izquierda
    Matriz_Padding[0 : Mitad_Padding , Columnas_Array + Mitad_Padding :] = Array[0][-1] #Esquina Superior Derecha
    Matriz_Padding[Filas_Array + Mitad_Padding : , 0 : Mitad_Padding] = Array[-1][0] #Esquina Inferior Izquierda
    Matriz_Padding[Filas_Array + Mitad_Padding : , Columnas_Array + Mitad_Padding :] = Array[-1][-1] #Esquina Inferior Derecha
    return Matriz_Padding


def convolucion(foto:np.ndarray, foto_padeada: np.ndarray, kernel:np.ndarray)-> np.ndarray:
    """
    Summary
    -------
    Esta funcion realiza la convolución entre el kernel(filtro) que se le desea aplicar a una imagen padeada.
    Considera 2 casos, por un lado las fotos con 2 dimensiones o axes, es decir las blanco y negro; por otro lado
    las fotos que tienen 3 dimensiones (filas, columnas , canales) canales siendo los arrays R,G,B

    Parameters
    ----------
    foto: np.ndarray
                    Este parámetro indica el tamaño de la matriz resultante de la convolucion ya que es deseado que la
                    foto filtrada sea del mismo tamaño que la foto sin el filtro
    
    foto_padeada: np.ndarray
                        Este parámetro es el array sobre el cual se va convolucionar el kernel
    
    Kernel: np.ndarray
                    Este parámetro es el filtro el cual se quiere convolucionar con la imagen padeada
    
    Returns
    --------
    Foto_filtrada: np.ndarray
                            Devuelve un array de dimensión identíca al de la foto original, que es la foto orginal
                            con el filtro del kernel aplicado

    """
    
    filas_foto, columnas_foto = foto.shape[:2]
    filas_kernel , columnas_kernel = kernel.shape
    foto_filtrda = np.zeros(foto.shape)
    if foto.ndim > 2:
        canales = foto.shape[2]
        for canal in range(canales):
            for filas in range(filas_foto):  
                for columnas in range(columnas_foto):  
                    submatriz = foto_padeada[filas: filas + filas_kernel, columnas:columnas + columnas_kernel, canal]
                    foto_filtrda[filas,columnas,canal] = np.sum([submatriz*kernel])

    else:
        for filas in range(filas_foto):  
            for columnas in range(columnas_foto):  
                submatriz = foto_padeada[filas: filas + filas_kernel, columnas:columnas + columnas_kernel]
                foto_filtrda[filas,columnas] = np.sum([submatriz*kernel])


    return foto_filtrda


def normalizado(Array: np.ndarray) -> np.ndarray:
    """
    Summary
    -------
    Normaliza los valores de los pixeles de una imagen, es decir los acota a [0,255]

    Parameters
    ---------

    Array: np.ndarray
                    Es la matriz de la imagen la cual se le normalizarán los valores 
    
    Returns
    --------
    """
    Maximo = np.amax(Array)
    Minimo = np.amin(Array)
    try:
        foto_normalizada= ((Array - Minimo)/(Maximo - Minimo)) * 255
    except:
        foto_normalizada = Array % 255 
        
    #En el caso de que el valor máx sea igual al valor min, sabemos que todos los valores de la matriz son iguales 
    # y nos interesa que la imagen este acotada en [0,255] usamos el % 255 para acotar, caso de que sean negativos
    # el % nos devuelve el resto en valor absoluto por lo que no tenemos que preocuparnos por ese caso
    
    return foto_normalizada