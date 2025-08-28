"""
Librería de Álgebra Lineal (LAC)
================================

Una librería personalizada para operaciones de álgebra lineal con vectores y matrices.

Módulos disponibles:
- Vector: Clase para trabajar con vectores
- Matrix: Clase para trabajar con matrices
- Funciones de vector: Operaciones con vectores
- Funciones de matriz: Operaciones con matrices
"""

from .linAlg import Vector, Matrix
from .linAlg import (
    # Funciones de vector
    dot_product,
    magnitude,
    normalize,
    cross_product,
    angle_between,
    
    # Funciones de matriz
    scale,
    add,
    subtract,
    vector_multiply,
    matrix_multiply,
    transpose,
    determinant,
    inverse
    
)

__version__ = "1.0.0"
__author__ = "Andrés Mateus Taborda"
__all__ = [
    'Vector',
    'Matrix',
    'dot_product',
    'magnitude',
    'normalize',
    'cross_product',
    'angle_between',
    'scale',
    'add',
    'subtract',
    'vector_multiply',
    'matrix_multiply',
    'transpose',
    'determinant',
    'inverse'
]