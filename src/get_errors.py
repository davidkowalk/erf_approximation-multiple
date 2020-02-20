import pandas

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

best_accuracy = []

def hyperbolic():
    global best_accuracy

    df = pandas.read_csv("./data/hyperbolic.csv")
    data = df.tail(1)

    i = data.index.stop-1

    error = data["error"].get(i)
    value = data["b"].get(i)

    best_accuracy.append(("hyperbolic", value, error))

def logarithmic():
    global best_accuracy

    df = pandas.read_csv("./data/log.csv")
    data = df.tail(1)

    i = data.index.stop-1

    error = data["error"].get(i)
    value = data["b"].get(i)

    best_accuracy.append(("logaritmic", value, error))


def algebraic():
    for name in names:
        df = pandas.read_csv(f"./data/algebraic{name}.csv")

        data = df.tail(1)

        i = data.index.stop-1

        error = data["error"].get(i)
        value = data["b"].get(i)

        best_accuracy.append((f"algebraic (a={name})", value, error))


def main():
    global best_accuracy

    logarithmic()
    hyperbolic()
    algebraic()

    df = pandas.DataFrame(best_accuracy)
    df.to_csv(f"./error/errors.csv", header=["name", "value", "error"], index = False)


if __name__=="__main__":
    main()
