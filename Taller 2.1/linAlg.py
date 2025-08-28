"""
Módulo principal de la librería de álgebra lineal
=================================================

Este módulo contiene las implementaciones de las clases Vector y Matrix,
así como las funciones de álgebra lineal asociadas.
"""

import math
from typing import List, Union, Tuple, Optional


class Vector:
    """
    Clase para representar y manipular vectores.
    
    Un vector es una lista de números que puede representar
    puntos en el espacio, direcciones, o cualquier secuencia ordenada de valores.
    """
    
    def __init__(self, components: List[Union[int, float]]):
        """
        Inicializa un vector con sus componentes.
        
        Args:
            components: Lista de números que representan las componentes del vector
        """
        self.components = components
    
    def __str__(self) -> str:
        """Representación en string del vector."""
        return f"{self.components}"
    
    def __iter__(self):
        """
            Hace que el objeto sea iterable, permitiendo su uso en bucles for, etc.
        """
        return iter(self.components)
    
    def __repr__(self) -> str:
        """Representación detallada del vector."""
        pass
    
    def __len__(self) -> int:
        """Retorna la dimensión del vector."""
        return len(self.components)
    
    def __getitem__(self, index: int) -> Union[int, float]:
        """Permite acceder a los componentes del vector usando índices."""
        return self.components[index]
    
    def __setitem__(self, index: int, value: Union[int, float]):
        """Permite modificar componentes del vector usando índices."""
        self.components[index] = value
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """Suma de vectores usando el operador +."""
        
        if len(self.components) != len(other):
            return "La dimension de los vectores debe ser igual para hacer la operación"
        else: 
            suma = [self.components[i] + other.components[i] for i in range(len(self.components))]
            return suma
        
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        """Resta de vectores usando el operador -."""

        if len(self.components) != len(self.components):
            return "La dimension de los vectores debe ser igual para hacer la operación"
        else: 
            resta = [self.components[i] - other[i] for i in range(len(self.components))]
            return resta
    
    def __mul__(self, scalar: Union[int, float]) -> 'Vector':
        """Multiplicación por escalar usando el operador *."""
        prodesc = [self.components[i] * scalar for i in range(len(self.components))]
        return (prodesc)
    
    def __rmul__(self, scalar: Union[int, float]) -> 'Vector':
        """Multiplicación por escalar (orden invertido)."""

        return self.__mul__(scalar)
    
    def __truediv__(self, scalar: Union[int, float]) -> 'Vector':
        """División por escalar usando el operador /."""
        
        if scalar == 0:
            return "No se puede divir un vector por 0"
        else:
            divesc = [self.components[i] / scalar for i in range(len(self.components))]
            return divesc
    
    def __eq__(self, other: 'Vector') -> bool:
        """Igualdad entre vectores usando el operador ==."""
        pass
    
    def __ne__(self, other: 'Vector') -> bool:
        """Desigualdad entre vectores usando el operador !=."""
        pass
    
    @property
    def magnitude(self) -> float:
        """Calcula y retorna la magnitud (norma) del vector."""
        return math.sqrt(sum([x ** 2 for x in self.components]))
    
    @property
    def unit_vector(self) -> 'Vector':
        """Retorna el vector unitario (normalizado)."""
        
        if self.magnitude == 0:
            return "No existe un vector unitario para un vector con magnitud 0"
        else:
            return normalize(self)
    
    def dot(self, other: 'Vector') -> float:
        """
        Calcula el producto punto con otro vector.
        
        Args:
            other: Otro vector para el producto punto
            
        Returns:
            El producto punto como un número
        """
        if len(self) != len(other):
            return "Los dos vectores ingresados tienen diferente dimensión"
        else:
            _prod = 0
            for i in range(len(self)):
                _prod += self.components[i] * other[i]
            return _prod
    
    def cross(self, other: 'Vector') -> 'Vector':
        """
        Calcula el producto cruz con otro vector (solo para vectores 3D).
        
        Args:
            other: Otro vector para el producto cruz
            
        Returns:
            Un nuevo vector resultado del producto cruz
        """
        return cross_product(self, other)
    
    def angle_with(self, other: 'Vector') -> float:
        """
        Calcula el ángulo entre este vector y otro.
        
        Args:
            other: Otro vector
            
        Returns:
            El ángulo en radianes
        """
        return angle_between(self, other)


class Matrix:
    """
    Clase para representar y manipular matrices.
    
    Una matriz es una colección rectangular de números organizados en filas y columnas.
    """
    
    def __init__(self, data: List[List[Union[int, float]]]):
        """
        Inicializa una matriz con sus datos.
        
        Args:
            data: Lista de listas que representa las filas de la matriz
        """
        self.data = data
    
    def __str__(self) -> str:
        """Representación en string de la matriz."""
        return f"{self.data}"
        #filas_formateadas = [str(fila) for fila in self.data]
        #return "\n".join(filas_formateadas)


    def __iter__(self):
        """
            Hace que el objeto sea iterable, permitiendo su uso en bucles for, etc.
        """
        return iter(self.data)

    def __repr__(self) -> str:
        """Representación detallada de la matriz."""
        return f"matriz: {self.data}"
    
    def __len__(self) -> int:
        """Retorna la dimensión del vector."""
        return len(self.data)    

    def __getitem__(self, key: Union[int, Tuple[int, int]]) -> Union[List[Union[int, float]], Union[int, float]]:
        """Permite acceder a filas o elementos específicos de la matriz."""
        
        return self.data[key]
    

        #if isinstance(key, int):
            #return self.data[key]
        #elif isinstance(key, tuple) and len(key) == 2:
            #fila, columna = key
            #return self.data[fila][columna]
        #else:
            #return "Índice de matriz no válido. Usa un int o una tupla (int, int)"

    
    def __setitem__(self, key: Union[int, Tuple[int, int]], value: Union[List[Union[int, float]], Union[int, float]]):
        """Permite modificar filas o elementos específicos de la matriz."""

        self.components[key] = value
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Suma de matrices usando el operador +."""
        
        if self.shape != other.shape:  #Verificando que el orden de las matrices son iguales
            return "Las matrices deben tener la misma dimension para poder operar"
        else:
            suma = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))] #ciclo for que suma cada el componente de una matriz por el correspondiente de la otra matriz
            return suma
    
    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """Resta de matrices usando el operador -."""
        
        if self.shape != other.shape:  #Verificando que el orden de las matrices son iguales
            return "Las matrices deben tener la misma dimension para poder operar"
        else:
            resta = [[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]  #ciclo for que resta cada el componente de una matriz por el correspondiente de la otra matriz
            return resta
    
    def __mul__(self, other: Union['Matrix', 'Vector', int, float]) -> Union['Matrix', 'Vector']:
        """Multiplicación de matrices/vectores/escalares usando el operador *."""
        
        if type(other) == int or type(other) == float:
            mulEsc = [[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))] # multiplicando la matriz por un escarlar
            return mulEsc
        else:
            if type(other) == Vector:
                if self.num_columns != len(other):
                    return "No se puede operar ya que el numero de columnas de la matriz es diferente al tamaño del vector"
                else:
                    return vector_multiply(self, other)
            else:
                if  type(other) == Matrix:
                        if other.shape != self.shape:
                            return "Las matrices tiene diferente dimension"
                        else:
                            return matrix_multiply(self, other)
        
    
    def __rmul__(self, scalar: Union[int, float]) -> 'Matrix':
        """Multiplicación por escalar (orden invertido)."""
        return  self * scalar 
    
    def __eq__(self, other: 'Matrix') -> bool:
        """Igualdad entre matrices usando el operador ==."""
        if self.num_rows != other.num_rows and self.num_columns != other.num_columns:
            return False
    
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                if self.data[i][j] != other.data[i][j]:
                    return False
        else: return True    
            
    
    def __ne__(self, other: 'Matrix') -> bool:
        """Desigualdad entre matrices usando el operador !=."""
        return not self == other
    
    @property
    def num_rows(self) -> int:
        """Retorna el número de filas de la matriz."""
        
        if len(self.data) == 0:
            return (0,0)
        else:
            return len(self.data)
    
    @property
    def num_columns(self) -> int:
        """Retorna el número de columnas de la matriz."""
        
        if len(self.data) == 0:
            return (0,0)
        else:
            return len(self.data[0])
    
    @property
    def shape(self) -> Tuple[int, int]:
        """Retorna las dimensiones de la matriz como (filas, columnas)."""
        
        if len(self.data) == 0:
            return (0,0)
        else:
            return (len(self.data), len(self.data[0]))
    
    @property
    def T(self) -> 'Matrix':
        """Retorna la transpuesta de la matriz."""
        trans = [[self.data[i][j] for i in range(len(self.data))] for j in range(len(self.data[0]))] 
        return trans
    
    @property
    def trace(self) -> Union[int, float]:
        """Calcula y retorna la traza de la matriz (suma de elementos diagonales)."""
        if self.num_rows == self.num_columns:
            tr = 0
            for i in range(len(self.data)):
                tr += self.data[i][i]
            return tr
        else:
           return "Debe ingresar una matriz cuadrada"
    
    
    @property
    def determinant(self) -> Union[int, float]:
        """Calcula y retorna el determinante de la matriz."""
        n = len(self.data)

        if any(len(row) != n for row in self.data):
            raise ValueError("La determinante solo se puede calcular para matrices cuadradas.")
        
        if n == 1:
            return self.data[0][0]
        
        if n == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        det = 0
        for j in range(n):
            
            submatrix_data = [row[:j] + row[j+1:] for row in self.data[1:]]
            
            submatrix = Matrix(submatrix_data)
            
            sign = (-1) ** j
            
            det += sign * self.data[0][j] * submatrix.determinant
            
        return det
    
    @property
    def inverse(self) -> 'Matrix':
        """Calcula y retorna la matriz inversa."""
        #return #(1/(self.determinant))  
        return Matrix((get_cofactors_matrix(self.data)).T) * (1/(self.determinant))
    
    def is_square(self) -> bool:
        """Verifica si la matriz es cuadrada."""
        
        if self.shape[0] == self.shape[1]:
            return True
        else:
            return False
    
    def is_symmetric(self) -> bool:
        """Verifica si la matriz es simétrica."""
        
        if self.T == self:
            return True
        else:
            False
    
    def is_diagonal(self) -> bool:
        """Verifica si la matriz es diagonal."""
        tr = 0
        for i in range(len(self.data)):
                tr *= self.data[i][i] 
        if tr == self.determinant:
            return True
        else:
            return False
    
    def get_row(self, index: int) -> 'Vector':
        """
        Obtiene una fila específica como vector.
        
        Args:
            index: Índice de la fila
            
        Returns:
            Vector con los elementos de la fila
        """
        if self.num_rows < index or index < 0:
            raise TypeError("El valor ingresadono esta en fuera del rango de la cantidad de filas de la matrix")
        else:
            return Vector(self[index])
    
    def get_column(self, index: int) -> 'Vector':
        """
        Obtiene una columna específica como vector.
        
        Args:
            index: Índice de la columna
            
        Returns:
            Vector con los elementos de la columna
        """
        if self.num_columns < index or index < 0:
            raise TypeError("El valor ingresadono esta en fuera del rango de la cantidad de columnas de la matrix")
            
        else:
            a = []
            for i in range(self.num_rows):
                a.append(self[i][index])
            return Vector(a)


# =============================================================================
# FUNCIONES DE VECTOR
# =============================================================================

def dot_product(v1: Vector, v2: Vector) -> float:
    """
    Calcula el producto punto entre dos vectores.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        El producto punto como un número
    """
    
    if len(v1) != len(v2):
        return "Los dos vectores ingresados tienen diferente dimensión"
    else:
        _prod = 0
        for i in range(len(v1)):
            _prod += v1[i] * v2[i]
        return _prod


def magnitude(v: Vector) -> float:
    """
    Calcula la magnitud (norma) de un vector.
    
    Args:
        v: El vector
        
    Returns:
        La magnitud del vector
    """
    
    return (sum([x ** 2 for x in v])) ** 0.5
    
    


def normalize(v: Vector) -> Vector:
    """
    Normaliza un vector (lo convierte en vector unitario).
    
    Args:
        v: El vector a normalizar
        
    Returns:
        Un nuevo vector normalizado
    """
    if v.magnitude == 0:
        return "No existe un vector unitario para un vector con magnitud 0"
    else:
        return [(i/v.magnitude) for i in v]


def cross_product(v1: Vector, v2: Vector) -> Vector:
    """
    Calcula el producto cruz entre dos vectores 3D.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        Un nuevo vector resultado del producto cruz
    """
    if len(v1) != 3 or len(v2) != 3:
        return "Los vectores o algunos de los vectores tienen dimension diferente a 3"
    else:
         if v1.dot(v2) == 0:
             return "No existe angulo entre los dos vectores ya que uno de ellos tiene magnitud 0"
         else:
             return [(v1[1] * v2[2]) - (v1[2] * v2[1]), (((v1[0] * v2[2]) - (v1[2] * v2[0])) * -1), (v1[0] * v2[1]) - (v1[1] * v2[0])]


def angle_between(v1: Vector, v2: Vector) -> float:
    """
    Calcula el ángulo entre dos vectores.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        El ángulo en radianes
    """
    if len(v1) != len(v2):
        return "Los dos vectores ingresados tienen diferente dimensión"
    else:
        if v1.dot(v2) == 0:
            return "No existe angulo entre los dos vectores ya que uno de ellos tiene magnitud 0"
    return f"El angulo entre los dos vectores es {math.acos(v1.dot(v2)/(v1.magnitude * v2.magnitude))}"


# =============================================================================
# FUNCIONES DE MATRIZ
# =============================================================================

def scale(matrix: Matrix, scalar: Union[int, float]) -> Matrix:
    """
    Multiplica una matriz por un escalar.
    
    Args:
        matrix: La matriz
        scalar: El escalar
        
    Returns:
        Una nueva matriz escalada
    """
    sc = matrix * scalar
    return sc
    
    #mulEs = [[matrix[i][j] * scalar for j in range(len(matrix[0]))] for i in range(len(matrix))] 
    #return mulEs


def add(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Suma dos matrices.
    
    Args:
        m1: Primera matriz
        m2: Segunda matriz
        
    Returns:
        Una nueva matriz resultado de la suma
    """
    su = m1 + m2
    return su



def subtract(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Resta dos matrices.
    
    Args:
        m1: Primera matriz
        m2: Segunda matriz
        
    Returns:
        Una nueva matriz resultado de la resta
    """
    res = m1 - m2
    return res


def vector_multiply(matrix: Matrix, vector: Vector) -> Vector:
    """
    Multiplica una matriz por un vector.
    
    Args:
        matrix: La matriz
        vector: El vector
        
    Returns:
        Un nuevo vector resultado de la multiplicación
    """
    if matrix.num_columns != len(vector): 
        return "El numero de filas de la matriz debe ser igual al numero de elementos del vector"
    else:
        mulvec = []
        for i in range(len(matrix)):
            suma = 0
            for j in range(len(matrix[0])):
                suma += matrix[i][j] * vector[j]
            mulvec.append(suma)
    
    return mulvec
    
    #mulvec = [[matrix.data[i][j] * vector[i] for j in range(len(matrix.data[0]))] for i in range(len(matrix.data))] # multiplicando la matriz por un escarlar
    #return mulvec


def matrix_multiply(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Multiplica dos matrices.
    
    Args:
        m1: Primera matriz
        m2: Segunda matriz
        
    Returns:
        Una nueva matriz resultado de la multiplicación
    """
    matmul =[]
    m2 = m2.T
    for i in m2:
        matmul.append(vector_multiply(m1, i)) 
    
    return Matrix(matmul).T


def transpose(matrix: Matrix) -> Matrix:
    """
    Calcula la transpuesta de una matriz.
    
    Args:
        matrix: La matriz
        
    Returns:
        Una nueva matriz transpuesta
    """
    return matrix.T


def determinant(matrix: Matrix) -> Union[int, float]:
    """
    Calcula el determinante de una matriz cuadrada.
    
    Args:
        matrix: La matriz cuadrada
        
    Returns:
        El determinante
    """
    pass


def inverse(matrix: Matrix) -> Matrix:
    """
    Calcula la matriz inversa.
    
    Args:
        matrix: La matriz cuadrada invertible
        
    Returns:
        Una nueva matriz inversa
    """
    pass


def identity_matrix(size: int) -> Matrix:
    """
    Crea una matriz identidad de tamaño especificado.
    
    Args:
        size: El tamaño de la matriz (size x size)
        
    Returns:
        Una nueva matriz identidad
    """
    pass


def zeros_matrix(rows: int, columns: int) -> Matrix:
    """
    Crea una matriz de ceros con las dimensiones especificadas.
    
    Args:
        rows: Número de filas
        columns: Número de columnas
        
    Returns:
        Una nueva matriz llena de ceros
    """
    pass


def ones_matrix(rows: int, columns: int) -> Matrix:
    """
    Crea una matriz de unos con las dimensiones especificadas.
    
    Args:
        rows: Número de filas
        columns: Número de columnas
        
    Returns:
        Una nueva matriz llena de unos
    """
    pass


# Las siguientes funciones que no fueron solicitadas en el taller fueron obtenidas con ayuda de AI

def get_det(matrix):
    """Calcula el determinante de una matriz de forma recursiva."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    
    det = 0
    # Expansión por cofactores en la primera fila
    for j in range(n):
        sign = (-1) ** (0 + j)
        minor_matrix = get_minor(matrix, 0, j)
        det += sign * matrix[0][j] * get_det(minor_matrix)
    return det



def get_minor(matrix, row, col):
    """Devuelve la submatriz que resulta de eliminar una fila y columna."""
    return [row_elem[:col] + row_elem[col+1:] for row_elem in (matrix[:row] + matrix[row+1:])]


def get_cofactors_matrix(matrix):
    """
    Calcula la matriz de cofactores a partir de una matriz cuadrada.
    
    Args:
        matrix (list of lists): La matriz de entrada.
    
    Returns:
        list of lists: La matriz de cofactores.
    """
    n = len(matrix)
    cofactors = []
    
    for i in range(n):
        row_cofactors = []
        for j in range(n):
            # Obtener el menor (la submatriz)
            minor = get_minor(matrix, i, j)
            
            # Calcular el cofactor: (-1)^(i+j) * determinante del menor
            cofactor = ((-1) ** (i + j)) * get_det(minor)
            row_cofactors.append(cofactor)
        cofactors.append(row_cofactors)
    
    return Matrix(cofactors)



