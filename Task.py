# In the Provided array, check if "Alice" exist. If she does, automatically remove her from the Array
# If she does no exist, promt user to enter a new name to add to the array. 
# Finally, print the array to display any changes made, either by removing "Alice" or by adding a new name.

# Copy the provided Array
names = [
    ['Alice', 'Bob', 'Charlie'],
    ['David', 'Eve', 'Frank'],
    ['Grace', 'Heldi', 'Ivan'],
    ['Judy,', 'Ken', 'Laura']
]
#Variable to track if alice was found
alice_found = False

# Check if "Alice" exist in names and remove her
for sublist in names:
  if 'Alice' in sublist:
    sublist.remove('Alice') 
    alice_found = True  # A mark that alice was found
# If alice no found in names ask for input
if alice_found == False: # Check if alice is found
  new = input("Enter a new name to add:")
  names.append(new)   # Add the new name to the new sublist
  
# Print the updated list
print("Updated List of Names")
for sublist in names:
    print(sublist)    

