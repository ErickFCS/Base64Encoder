import base64, os

class Encoder:
    def __init__(self) -> None:
        self.invalid = "Invalid Input, Try Again"
        self.output(self.process(self.getInput()))

    def defaultInput(self, prompt, default):
        temp = input(prompt)
        return temp if temp else default

    def getInput(self):
        while True:
            inputType = self.defaultInput("File Or Text? > ", "f").lower()
            if inputType in ["file", "f"]:
                while True:    
                    fileLocation = self.defaultInput("File Location? > ", "res")
                    try:
                        with open(fileLocation, "rb") as file:
                            data = file.read()
                            break
                    except: print(self.invalid) ; continue
                break
            elif inputType in ["text", "t"]: data = self.defaultInput("> ", "entirely").encode() ; break
            else: print(self.invalid) ; continue
        return data
    
    def process(self, data):
        while True:
            task = input("Encode or Decode? > ").lower()
            if task in ["encode", "e"]: result = base64.a85encode(data) ; break
            elif task in ["decode", "d"]:
                try:
                    result = base64.a85decode(data)
                    break
                except:
                    print("No encoded text")
                    exit()
            else: print(self.invalid) ; continue
        return result

    def output(self, result):
        while True:
            outputTo = self.defaultInput("Print of Save? > ", "p").lower()
            if outputTo in ["save", "s"]:
                with open("res", "wb")as file:
                    file.write(result)
                    break
            elif outputTo in ["print", "p"]:
                os.system("color 4")
                print(result.decode())
                break
            else: print(self.invalid) ; continue

a = Encoder()