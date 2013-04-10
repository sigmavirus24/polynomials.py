polynomials.py
==============

I was sitting in lecture talking about polynomials, fields, etc and wondered 
how hard it could really be to construct a polynomial. This little toy came 
out of it. I'm sure for polynomials of large enough degree, this would perform 
awfully, but it's fine for small ones.

Usage
-----

.. code-block:: python

    from polynomials import Polynomial

    # p(x) := 1 + 2x + 3x^2
    p = Polynomial(1, 2, 3)
    print('p(2) = {0}'.format(p(2)))

    # r(x) := 2 + 2x + 8x^2
    r = p + Polynomial(1, 0, 5)
    print('r(2) = {0}'.format(r(2)))

    # r(x) := 1 + 5x^2
    r -= p
    print('r(2) = {0}'.format(r(2)))

    print('r == p is {0}'.format(r == p))


License
-------

`Modified BSD License <./LICENSE>`_
