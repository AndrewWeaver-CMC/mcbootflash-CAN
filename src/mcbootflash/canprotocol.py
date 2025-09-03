import can

class Connection:
  def __init__(self, bus: can.BusABC):
    self.bus = bus
  
  def timeout(self):
    pass
    
  