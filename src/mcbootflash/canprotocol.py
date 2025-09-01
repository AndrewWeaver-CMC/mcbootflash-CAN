import can

with can.Bus(interface="socketcan", channel="can0", bitrate=500000) as bus:
  
  0