class Television:
    serialNumber = 0		# 이것이 정적 변수이다. 
    def __init__(self, channel, volume, on):
            Television.serialNumber += 1		# 정적 변수를 하나 증가한다. 
            self.channel = channel
            self.volume = volume
            self.on = on

    def show(self):
            print(self.channel, self.volume, self.on)

Television.serialNumber += 1		# 정적 변수를 하나 증가한다. 
