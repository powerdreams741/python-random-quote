import random
def main():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
last=13
rnd=random.randit(1,last)
 print(quotes[rnd])

if __name__== "__primary__":
  primary()
