import matplotlib.pyplot as plt
import time
class LinearGenerator:
	def __init__(self, A, C, M, seed):
		self.A = A
		self.C = C
		self.M = M
		self.previous = seed % self.M
	def next(self):
		self.previous = (self.A * self.previous + self.C) % self.M
		return (self.previous) / self.M

class ShiftRegisterGenerator:
	def __init__(self, seed):
		self.previous = seed
	def next(self):
		new = self.previous[0] ^ self.previous[1]
		self.previous = self.previous[1:] + [new]
		return new
  

if __name__ == '__main__':
	A = 16807
	C = 0
	M = 2**31 - 1
	N = 10000
	print("1. ")
	linear_generator = LinearGenerator(A, C, M, int(time.time()))
	gen = []
	for i in range(N):
		num = linear_generator.next()
		gen.append(num)
		print(num, end=', ')
	print("Mean: ", sum(gen) / N)
	plt.hist(gen, bins=100, edgecolor='black')
	plt.title("Linear Generator")
	plt.show()
	
	print("2. ")
	shift_register_generator = ShiftRegisterGenerator(list(map(int, bin(int(time.time()))[2:])))
	gen = []
	for i in range(N):
		num = shift_register_generator.next()
		gen.append(num)
		print(num, end=', ')
	print("Mean: ", sum(gen) / N)
	plt.title("Shift Register Generator")
	plt.hist(gen, bins=2, edgecolor='black')
	plt.show()