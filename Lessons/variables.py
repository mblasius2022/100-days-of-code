first_name = "Black"
last_name = "Knight"
full_name = f"{first_name} {last_name}"
quote = "It's only a flesh wound"
quote2 = "Come back here ... I'll bite your ankles"
text_with_whitespace = "  hello world   "
n1,n2,n3 = 2,2,4

# print quotes
print(f"{full_name.upper()}: {quote}")
print(f"{full_name}: {quote2}")

print("\n")

# trim whitespace
print(f"Text: {text_with_whitespace.lstrip()} <<")
print(f"Text: {text_with_whitespace.rstrip()} <<")
print(f"Text: {text_with_whitespace.strip()} <<")

print("\n")

#print calculations to 8
print(n1*n2+n3)
print(n2*n3)

print(f"Hello {full_name.upper()}")


