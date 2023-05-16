import time, sys, getopt, os, pyautogui as pg

def main(argv):
   inputfile = ''
   texto = ''
   try:
      opts, args = getopt.getopt(argv,"p:t:")
      for opt, arg in opts:
         print(str(arg))
         if opt == '-p':
            print('opción -p')
            inputfile = arg
         elif opt == '-t':
            texto = str(arg)
   except Exception as e:
      print(str(e))
   print(os.path.exists(inputfile))
   print(len(texto))
   if os.path.exists(inputfile) and len(texto) >0:
      location = pg.locateCenterOnScreen(inputfile, confidence=0.9)
      while (location==None):
         location = pg.locateCenterOnScreen(inputfile, confidence=0.9)
      if not (location==None):
         print(location)
         pg.moveTo(location, duration=0.1)
         pg.leftClick()
         time.sleep(1)
         pg.typewrite(texto)
         print(texto)
         time.sleep(1)
         pg.press('enter')
         print('luego de enter')

if __name__ == "__main__":
   main(sys.argv[1:])
