import pandas

def main():
  a = 2
  max = 10
  names = [
  "2","2.25","2.5","2.75",
  "3","3.25","3.5","3.75",
  "4","4.25","4.5","4.75",
  "5","5.25","5.5","5.75",
  "6","6.25","6.5","6.75",
  "7","7.25","7.5","7.75",
  "8","8.25","8.5","8.75",
  "9","9.25","9.5","9.75",
  "10"
  ]

  for name in names:
    csv = pandas.read_csv(f"algebraic{name}.csv")
    tail = csv.tail(2)

    pos = tail["b"]
    ers = tail["error"]

    p1 = tail.index.start
    p2 = tail.index.stop-1

    db = pos.get(p2)-pos.get(p1)
    de = ers.get(p2)-ers.get(p1)

    print(f"At {name} the last rate of change is {de/db}")

if __name__=="__main__":
    main()
