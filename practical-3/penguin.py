import time

def shiftImage(numberOfspaces, image):
  shift = " " * numberOfspaces
  return shift.join(image.splitlines(True))

def clearScreen():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')

penguin = """
                     xxxxx
                  xXXXXXXXXXx
                 XXXXXXXXXXXXX
                xXXXXXXXX  XXXx
                XXXXXXXXX 0XXXX\\\\\\
               xXXXXXXXXXxxXXXX\\\\\\\\
               XXXXX|\XXX/|XXXXX
               XXXXX| \-/ |XXXXX
              xXXXXX| [ ] |XXXXXx
            xXXXX   | /-\ |   XXXXx
         xXXXXX     |/   \|     XXXXXx
       xXXXXXX                   XXXXXXx
      xXXXXXXX         I         XXXXXXXx
     xXXXXXXXX                   XXXXXXXXx
    xXXXXXXXXX         ♥         XXXXXXXXXx
   xXXXXXXXXXX                   XXXXXXXXXXx
  xXXXXXXXXXXX         N         XXXXXXXXXXXx
 xXXXXXXXX XXX         I         XXX XXXXXXXXx
 XXXXXXXX  XXX         A         XXX  XXXXXXXX
xXXXXXXX   XXX         M         XXX   XXXXXXXx
XXXXXX     XXX         H         XXX     XXXXXX
XXXX       XXX                   XXX       XXXX
 XX        XXX                   XXX        XX
           XXX                   XXX
           XXX                   XXX
           XXX                   XXX
           XXX                   XXX
           XXXx                 xXXX
           XXXXXXXXXXXXXXXXXXXXXXXXX
           XXXXXXX           XXXXXXX
       ____XXXXXX             XXXXXX____
      /________/               \________\\
"""

clearScreen()
print (shiftImage(0, penguin))

for spaces in range(1, 70):
  time.sleep(0.05)
  clearScreen()
  print (shiftImage(spaces, penguin))
