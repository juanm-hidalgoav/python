def add_dots(text):

  # Split the text into a list of words
  words = text.split()
  print(" ".join(words))
  # Add a dot to each word and join them back with spaces
  dotted_text = ". ".join(words)
  
  return dotted_text

# Example usage
text =  """
This function takes a 
string as input and returns a new string 
with a dot appended to each word.
 """

dotted_text = add_dots(text)

print(dotted_text)