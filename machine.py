class Machine:
    def __init__(self, wheels, board, reflector):
        self.wheels = wheels
        self.plugBoard = board
        self.reflector = reflector

    def iterateState(self):

        self.wheels[0].iterateState()
        i = 0
        while self.wheels[i].getState() == self.wheels[i].getNotch() and i < len(self.wheels) - 1:
            self.wheels[i + 1].iterateState()
            i += 1

    def encryptLetter(self, letter):
        wheels = self.wheels
        letter = ord(letter) - 97
        #print([wheel.getState() for wheel in self.wheels])
        # letter = self.plugBoard.encryptLetter(letter)

        for wheel in self.wheels:
            letter = wheel.convertSignal(letter)
            #print(chr(letter + 97))
        letter = self.reflector.get(letter)

        letter = wheels[2].convertSignalBackward(letter)
        letter = wheels[1].convertSignalBackward(letter)
        letter = wheels[0].convertSignalBackward(letter)

        self.iterateState()
        return letter

    def encryptText(self, text):
        str1 = ""
        return str1.join([chr(self.encryptLetter(letter) + 97) for letter in text.strip(" ").lower()])

    def getWheels(self):
        return self.wheels

    def getPlugBoard(self):
        return self.board

    def reflect(self, value):
        return self.reflector.get(value)

    def decrypt(self, wheelStates, plugboard, message):
        for position, wheel in enumerate(self.wheels):
            wheel.setState(wheelStates[position])

        self.plugBoard = plugboard

        return self.encryptText(message)



