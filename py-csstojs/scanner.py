class Scanner:
    # Class variables
    file = None
    ch = None
    line_number = 1
    column_number = 0
    # Constructor (initialises)
    def __init__(self, file):
        try:
            self.file = open(file, "r")
        except:
            print("[E] file error.")
            exit()
    # Does the scanning
    def read(self):
        while(True):
            ch = self.file.read(1)
            self.column_number += 1
            if (not ch):
                print("\n[F] EOF reached")
                break
            elif (ch == "\t" or ch == " "):
                continue
            elif (ch == "\n"):
                self.column_number += 1
            else:
                # process possible characters
                pass


if __name__ == "__main__":
    sc = Scanner(input("Enter the file to be scanned-->"))
    sc.read()