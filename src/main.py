from fractions import Fraction

IMPOSSIBLE = [-1, -1]


def solution(pegs):
	if not isinstance(pegs, list):
		return IMPOSSIBLE
	n = len(pegs)
	if n <= 1:
		return IMPOSSIBLE
	R = 0
	if n % 2 == 0:
		R = (- pegs[0] + pegs[n - 1])
	else:
		R = (- pegs[0] - pegs[n - 1])
	for index in range(1, n - 1):
		R += 2 * (-1) ** (index + 1) * pegs[index]
	fraction = Fraction(2 * (float(R) / 3 if n % 2 == 0 else R)).limit_denominator()
	if fraction < 2:
		return IMPOSSIBLE
	radius = fraction
	for i in range(n - 2):
		distance = pegs[i + 1] - pegs[i]
		next_radius = distance - radius
		if radius < 1 or next_radius < 1:
			return IMPOSSIBLE
		else:
			radius = next_radius
	return [fraction.numerator, fraction.denominator]


def main():
	pegs = [4, 30, 50, 200, 400]
	print solution(pegs)
	P0, P1, P2, P3, P4 = pegs
	print 2 * (-P0 + 2 * (P1 - P2 + P3) - P4)


if __name__ == '__main__':
	main()
