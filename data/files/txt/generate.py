#first function.
def search (fileN):

  print("Searching the books....")

  #dict for book data
  bookdata = {}

  #open file
  with open(fileN) as fileName:
  
    sectionN = ""

    #for loop for lines. 
    for line in fileName:

      #if statements for section names  
      if (line.startswith("Section")):

        partN = line.split(":")

        sectionN = partN[1].strip()

      elif (sectionN in bookdata):

        bookdata[sectionN].append(line.strip())

      else:

        bookdata[sectionN] = [line.strip()]

  print("Search complete!")

  #return value
  return bookdata

#second function
def run():

  #bookdata variable for second function.
  bookdata = search("data/files/txt/books.txt")

  #open CSV file.
  with open ("data/files/txt/generating.csv", "w") as file: 
    for section, titles in bookdata.items():
      for bookname in titles:
        file.write("{}, {}\n" .format(section, bookname))

run()