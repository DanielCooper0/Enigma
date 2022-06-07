class RotorWheel:
    def __init__(self, state, connections, notch):
        self.state = state
        self.connections = connections
        self.notch = notch
        self.reversedConnections = {v: k for k, v in connections.items()}

    def getConnections(self):
        return self.connections

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def getNotch(self):
        return self.notch

    def iterateState(self):
        self.state = (self.state + 1) % len(self.connections.keys())

    def convertSignal(self, value):
        state = self.state

        value = (value + state) % len(self.connections.keys())

        return self.connections.get(value)

    def convertSignalBackward(self, value):
        state = self.state

        #value = (value - state) % len(self.reversedConnections.keys())

        return (self.reversedConnections.get(value) - state) % len(self.reversedConnections.keys())
