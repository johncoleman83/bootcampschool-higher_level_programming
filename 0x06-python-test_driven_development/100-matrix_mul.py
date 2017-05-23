#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if type(m_a) is not list or type(m_b) is not list:
        raise TypeError('{:} must be a list'.format('m_b' if type(m_a) is list
                                                    else 'm_a'))
    if not m_a or not m_b:
        raise ValueError("{:} can't be empty".format('m_b' if m_a else 'm_a'))
    for row in m_a:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
        if len(row) != len(row[0]):
            raise TypeError('each row of m_a must should be of the same size')
    for row in m_b:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError('m_b should contain only integers or floats')
        if len(row) != len(row[0]):
            raise TypeError('each row of m_b must should be of the same size')
    a_cols = len(m_a[0])
    b_rows = len(m_b)
    if a_cols != b_rows:
        raise ValueError("m_a and m_b can't be multiplied")
    a_rows = len(m_a)
    b_cols = len(m_b[0])
    product = []
    for i in range(a_rows):
        product.append([])
    for 
