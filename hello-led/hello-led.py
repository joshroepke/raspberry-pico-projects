import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)

print("Flashing Light from Eli!")
while True:
    try: 
      led.value(1)
      utime.sleep(2)
      led.value(0)
      utime.sleep(2)
    except KeyboardInterrupt:
        break
led.off()
print("Done")