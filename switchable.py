from nanpy import ArduinoApi, SerialManager
arduino = ArduinoApi(connection=SerialManager())


class Switchable():
    def __init__(self, pin):
        self.pin = pin
        self.state = False

    def on():
        arduino.digitalWrite(self.pin, arduino.HIGH)
        self.state = True

    def off():
        arduino.digitalWrite(self.pin, arduino.LOW)
        self.state = False

    def toggle():
        arduino.digitalWrite(self.pin, !self.state)
        self.state = !self.state
        print "toggled to {}".format(self.state)

    def dim(dimVal):
        arduino.analogWrite(self.pin, dimVal)
        self.state = dimVal

    def getState():
        return self.state

    def setState(state):
        arduino.digitalWrite(self.pin, state)
        self.state = state
