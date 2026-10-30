import libreria
import time

a = libreria.AlphaBot()
a.forward()
time.sleep(2)
a.stop()

a.right()
time.sleep(0.4)
a.stop()

a.left()
time.sleep(0.8)
a.stop()

a.forward()
time.sleep(2)
a.stop()