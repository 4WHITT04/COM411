#first function
def search (filename):

  print("searching through the books....")

  sections = []

  bookname = []

  with open(filename) as filename:
    
    for line in filename:

      if line.startswith("Section"):
        
        secname = line.slit(":"[1])
        
        sections.append(secname.strip())
      else: 
        bookname.append(line.strip())

  print("Done searching!!!")

  return(sections, bookname)

  def save (filename, datastore):

    print("Saving information....")

    with open(filename, "w") as filename:

      filename.write("section: {}\n" .format(datastore[0]))
      
      filename.write("book: {}\n" .format(datastore[1]))
    
    print("Process complete!!!!")

def run():
  
  dataname = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt", dataname)

run()