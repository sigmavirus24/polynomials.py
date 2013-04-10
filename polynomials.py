from collections import defaultdict


class Polynomial(object):
    def __init__(self, *args):
        self.p = defaultdict(int)
        self.sorted = list(enumerate(args))
        self.p.update(self.sorted)

    def __repr__(self):
        return 'Polynomial%s' % self.sorted

    def __call__(self, x):
        return sum([a*(x**i) for i, a in self.p.items()])

    def __iadd__(self, other):
        for k, v in other.p.items():
            self.p[k] += v
        self.sorted = sorted(self.p.items())
        return self

    def __isub__(self, other):
        for k, v in other.p.items():
            self.p[k] -= v
        self.sorted = sorted(self.p.items())
        return self

    def __add__(self, other):
        new_p = self.p.copy()
        for k, v in other.p.items():
            new_p[k] += v
        poly = Polynomial()
        poly.p = new_p
        return poly

    def __sub__(self, other):
        new_p = self.p.copy()
        for k, v in other.p.items():
            new_p[k] -= v
        poly = Polynomial()
        poly.p = new_p
        return poly

    def __eq__(self, other):
        return self.p == other.p

    def __ne__(self, other):
        return self.p != other.p


if __name__ == '__main__':
    # p(x) := 3x^2 + 2x + 1
    p = Polynomial(1, 2, 3)
    # 6 = p(1)
    assert p(1) == 6

    # q(x) := 5x^2 + 1
    q = Polynomial(1, 0, 5)
    # 6 = q(1)
    assert q(1) == 6

    # r(x) := p(x) + q(x) = 8x^2 + 2x + 1
    r = p + q
    # 12 = r(1) = q(1) + p(1)
    assert r(1) == p(1) + q(1)

    assert r == (p + q)

    p += q

    assert r == p
    assert r != q

    p -= q

    assert r != p
    assert r == (p + q)
