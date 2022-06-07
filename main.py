import numpy as np
import machine
import plugBoard
import rotorWheel
import Enigma_1_properties


def main():
    wheel1 = rotorWheel.RotorWheel(0, Enigma_1_properties.wheel1, Enigma_1_properties.wheel1Notch)
    wheel2 = rotorWheel.RotorWheel(0, Enigma_1_properties.wheel2, Enigma_1_properties.wheel2Notch)
    wheel3 = rotorWheel.RotorWheel(0, Enigma_1_properties.wheel3, Enigma_1_properties.wheel3Notch)
    wheel4 = rotorWheel.RotorWheel(0, Enigma_1_properties.wheel4, Enigma_1_properties.wheel4Notch)
    wheel5 = rotorWheel.RotorWheel(0, Enigma_1_properties.wheel5, Enigma_1_properties.wheel5Notch)

    reflectorA = Enigma_1_properties.reflectorA
    reflectorB = Enigma_1_properties.reflectorB
    reflectorC = Enigma_1_properties.reflectorC

    EnigmaEncode = machine.Machine([wheel1, wheel2, wheel3], None, reflectorA)
    EnigmaDecode = machine.Machine([wheel1, wheel2, wheel3], None, reflectorA)

    output = EnigmaEncode.encryptText("")
    print(output)
    #print(EnigmaDecode.decrypt([0, 0, 0], None, output))


main()
