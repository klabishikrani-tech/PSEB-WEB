votes = ("A", "B", "A", "C", "A", "B")

a = votes.count("A")
b = votes.count("B")
c = votes.count("C")

print(f"A={a}")
print(f"B={b}")
print(f"C={c}")

first_c = votes.index("C")

print(f"First C at index {first_c}")


