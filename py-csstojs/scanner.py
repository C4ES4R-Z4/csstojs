

class Scanner:
    # Class variables
    file = None
    ch = None
    table = {}
    line_number = 1
    column_number = 0

    # Constructor (initialises)
    def __init__(self, file):
        try:
            self.file = open(file, "r")
        except:
            print("[E] file error.")
            exit()

    # reads a single character
    def read_char(self):
        self.ch = self.file.read(1)
        self.column_number += 1
        if (self.ch == "\t" or self.ch == " "):
            self.column_number += 1
            self.read_char()
        elif (self.ch == "\n"):
            self.line_number += 1
            self.column_number = 0
            self.read_char()

    # parse through the file
    def scan(self, *args):
        while (True):
            self.read_char()
            # Process the symbols/tokens
            if (self.ch.isalpha() or self.ch == "." or self.ch == "#"):
                self.process_identifier()
            # When EOF break
            if (self.ch == ""):
                break

    # porcessing an identifier
    def process_identifier(self):
        identity = []
        while(self.ch != "{" and self.ch != ""):
            identity.append(self.ch)
            self.read_char()
            if (self.ch == "" or not self.ch.isalnum):
                print(f"[E] at (Ln:{self.line_number},Col:{self.column_number}) expected 1")
        self.read_char()
        identifier = "".join(identity)
        print(identifier)
        # skip the properties for now (testing)
        # TODO: remove later
        legal = ["-", ":", ";", "%"]
        while(self.ch != "}"):
            if (self.ch == "" or not (self.ch.isalnum() or self.ch in legal)):
                print(f"[E] at (Ln:{self.line_number},Col:{self.column_number}) expected 2")
            self.read_char()




if __name__ == "__main__":
    sc = Scanner(input("Enter the file to be scanned -->"))
    identifier = input("which identifier? -->")
    sc.scan(identifier)