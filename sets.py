# Create a empty sets
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) #set doesn't allow duplicate numbers

# Remove elements of the set
s.remove(2)
s.print(s)

print(f"The set has {len(s)} elements.")