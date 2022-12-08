import abc

## Invoker
class RemoteControl:
  def __init__(self):
    self.onCommand = []
    self.offCommand = []

  def setCommand(self, onCommand, offCommand):
    self.onCommand.append(onCommand)
    self.offCommand.append(offCommand)

  def onButtonWasPushed(self, slot):
    self.onCommand[slot].execute()

  def offButtonWasPushed(self, slot):
    self.offCommand[slot].execute()

## Receiver
class LightObj:
  def on(self):
    print ("Light ON")

  def off(self):
    print ("Light OFF")

class TvObj:
  def on(self):
    print ("TV ON")

  def off(self):
    print ("TV OFF")

class AudioObj:
  def on(self):
    print ("Audio ON")

  def off(self):
    print ("Audio OFF")

## Command
class Command:
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def execute(self):
    pass

class LightOnCommand(Command):
  def __init__(self, lightObject):
    self.light = lightObject

  def execute(self):
    self.light.on()

class LightOffCommand(Command):
  def __init__(self, lightObject):
    self.light = lightObject

  def execute(self):
    self.light.off()

class TVOnCommand(Command):
  def __init__(self, tvObject):
    self.tv = tvObject

  def execute(self):
    self.tv.on()

class TVOffCommand(Command):
  def __init__(self, tvObject):
    self.tv = tvObject

  def execute(self):
    self.tv.off()

class AudioOnCommand(Command):
  def __init__(self, audioObject):
    self.audio = audioObject

  def execute(self):
    self.audio.on()

class AudioOffCommand(Command):
  def __init__(self, audioObject):
    self.audio = audioObject

  def execute(self):
    self.audio.off()


# Invoker
remoteContoller = RemoteControl()

# Reciever
lightObj = LightObj()
tvObj = TvObj()
audioObj = AudioObj()

# Command
lightOnButton = LightOnCommand(lightObj)
lightOffButton = LightOffCommand(lightObj)
tvOnButton = TVOnCommand(tvObj)
tvOffButton = TVOffCommand(tvObj)
audioOnButton= AudioOnCommand(audioObj)
audioOffButton = AudioOffCommand(audioObj)

# SetCommand
remoteContoller.setCommand(lightOnButton, lightOffButton)
remoteContoller.setCommand(tvOnButton, tvOffButton)
remoteContoller.setCommand(audioOnButton, audioOffButton)

# Execute
remoteContoller.onButtonWasPushed(0)
remoteContoller.onButtonWasPushed(1)
remoteContoller.onButtonWasPushed(2)

remoteContoller.offButtonWasPushed(0)
remoteContoller.offButtonWasPushed(1)
remoteContoller.offButtonWasPushed(2)