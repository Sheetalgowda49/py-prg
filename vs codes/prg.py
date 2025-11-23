"""Simple interactive calculator.

Supports: addition (+), subtraction (-), multiplication (*), division (/).
Enter `q` or `quit` to exit.
"""

def get_number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Invalid number, try again.")


def main():
	print("Simple Calculator — enter q to quit")
	while True:
		op = input("Choose operation (+, -, *, /) or q to quit: ").strip().lower()
		if op in ("q", "quit", "exit"):
			print("Goodbye")
			break
		if op not in ("+", "-", "*", "/"):
			print("Unknown operation — choose +, -, *, or /")
			continue

		a = get_number("Enter first number: ")
		b = get_number("Enter second number: ")

		if op == "+":
			c = a + b
		elif op == "-":
			c = a - b
		elif op == "*":
			c = a * b
		else:  # op == '/'
			if b == 0:
				print("Error: division by zero")
				continue
			c = a / b

		print(f"Result: {c}")


if __name__ == "__main__":
	main()