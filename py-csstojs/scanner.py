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
            self.read_char()

    # Process class names
    def process_class(self):
        identifer = []
        while (self.ch.isalnum() or self.ch == "." and self.ch):
            identifer.append(self.ch)
            self.read_char()
        self.table["".join(identifer)] = ""
        self.process_properties("".join(identifer))

    # Process properties and settings
    def process_properties(self, identifier):
        properties = []
        if (self.ch != "{"):
            print(f"[E] (Ln:{self.line_number}, Col:{self.column_number}) {'{'} expected")
            exit()
        while (True):
            if (not self.ch):
                print(f"[E]")
            properties.append(self.ch)
            if (self.ch == "}"):
                break
            self.read_char()
        self.table[identifier] = "".join(properties)[1:-1].split(";")
        
    # loop through file
    def read_all(self, id):
        while (True):
            self.read_char()
            if (not self.ch):
                break
            elif (self.ch == "."):
                self.process_class();
        print(self.table)
        


if __name__ == "__main__":
    sc = Scanner(input("Enter the file to be scanned -->"))
    identifier = input("which identifier? -->")
    sc.read_all(identifier)