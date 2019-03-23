import re



def filter_lines(filename, regexp):
    result = []
    f = open(filename)
    lines = f.readline()
    while lines:
        if re.match(regexp, lines):
            print(f"line {lines} don't match")
        lines = f.readline()
    f.close()
    return []


if __name__ == "__main__":
    filename = "coverage-error.log"
    regexp = r"\[\d\d\d\d\.\d\d\.\d\d \d\d:\d\d:\d\d\].+"
    print("Author is Dmitry.Shapovalov")
    print(filter_lines(filename, regexp))
