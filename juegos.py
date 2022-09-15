from machine import Pin as pin,ADC,I2C
from utime import sleep_ms
from ssd1306 import SSD1306_I2C
import framebuf
sensorx = ADC(pin(32))   # pines usados el 35,34,33,36, 39 , 32, 
sensory = ADC(pin(33))  # pines usados el 35,34,33,36, 39 , 32, 
pulsadorj = pin(12,pin.IN)
leda = pin(18,pin.OUT)
sensorx.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensorx.width(ADC.WIDTH_12BIT) # establecer resolución
sensory.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensory.width(ADC.WIDTH_12BIT) # establecer resolución
ancho = 128
alto = 64
i2c = I2C(0, scl=pin(22), sda=pin(23))
oled = SSD1306_I2C(ancho, alto, i2c)
#print(i2c.scan())

def triki():
      oled.text("  Bienvenido  ", 0, 16,0)
      oled.text("      a       ", 0, 24,0)
      oled.text("    Triki     ", 0, 32,0)

posicion = 40


def arriba(mover):
  subir = posicion + 16
  if subir >= 40:
    subir = 40
  return(subir)

def abajo(mover):
  bajar = posicion - 16
  if bajar <= 24:
    bajar = 24
  return(bajar)


while True:

  print (posicion)
  sleep_ms(150)
  oled.fill(1)

  x=sensorx.read()
  y=sensory.read()
  oled.text("---------------*", 0, 00,0)
  oled.text("[  Start Menu  ]", 0, 8,0)
  oled.text("[              ]", 0, 16,0)
  oled.text("[    Triki     ]", 0, 24,0)
  oled.text("[              ]", 0, 32,0)
  oled.text("[    Snake     ]", 0, 40,0)
  oled.text("[              ]", 0, 48,0)
  oled.text("*--------------*", 0, 56,0)

  # print (x)
#POSISION DE EL JOYSTICK
  if x>3600:
    print ("izquierda")
    

  elif x<150:
    print ("derecha")
    
  
  # print (x)
  if y>3600:
    print ("arriba ")
    posicion = arriba(posicion)
    
    

  elif y<150:
    print ("Abajo")
    posicion = abajo(posicion)
    
    
 #POSISION DE EL JOYSTICK

 #PRUEBA DE BOTON
  if pulsadorj.value()==0:
    leda.value(1)
    sleep_ms(300)
    leda.value(0)
 #PRUEBA DE BOTON

 #flecha para indicar posision 

  if posicion == 24:
    oled.text("  >", 0, 40,0)
  
  if posicion == 40:
    oled.text("  >", 0, 24,0)

 #flecha para indicar posision

 #Entrar a juegos

  if pulsadorj.value()==1 and posicion == 24:
    triki()
  
  oled.show()
  oled.fill(0)
  sleep_ms(100)

