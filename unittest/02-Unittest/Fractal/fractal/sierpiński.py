"""Draw Sierpiński fractals

Unlike some other fractals, evaluating a single point for membership 
is dramatically inefficient.  Creating an entire canvas is more direct
"""

def gasket(pixels=800, N=5)
    """Draw a Sierpiński gasket of `N` iterations on canvas of size `pixels`
    
    More than 255 iterations are not be legible, and are not allowed.
    For this implementation, a different value is given for each removal.
    
    Encode points inside the gasket as 0.  
    Encode points removed from gasket at iteration n as value n.
    
    >>> canvas = gasket(500, N=6)
    >>> canvas.shape
    (500, 500)
    """ 
    assert N < 256
    canvas = np.zeros(shape=(pixels, pixels), dtype=np.uint8)
    # Implementation here...
    return canvas


def carpet(pixels=800, N=5)
    """Draw a Sierpiński carpet of `N` iterations on canvas of size `pixels`
    
    More than 255 iterations are not be legible, and are not allowed.
    For this implementation, a different value is given for each removal.
    
    Encode points inside the carpet as 0.  
    Encode points removed from carpet at iteration n as value n.
    
    >>> canvas = carpet(500, N=6)
    >>> canvas.shape
    (500, 500)
    """ 
    assert N < 256
    canvas = np.zeros(shape=(pixels, pixels), dtype=np.uint8)
    # Implementation here...
    return canvas
