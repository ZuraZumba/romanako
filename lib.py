# pytest_passed_black_passed
class QuadraticEquationSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        d = self.b**2 - 4 * self.a * self.c

        if d < 0:
            return []

        if d == 0:
            return [-self.b / (2 * self.a)]

        return [
            (-self.b + d**0.5) / (2 * self.a),
            (-self.b - d**0.5) / (2 * self.a),
        ]


# 5522168977305710661

# 3584168977305715778
