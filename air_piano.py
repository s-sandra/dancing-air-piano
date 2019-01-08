import wiringpi as wp
import pygame.midi
import os, sys, select

if wp.wiringPiSetup() == -1:
	print "set up failed."

pygame.midi.init() # initializes pygame midi synthesizer
player = pygame.midi.Output(3) # pipes output to timidity-daemon
player.set_instrument(0)

signal_c = 0 # GPIO pin 17
signal_d = 1 # GPI0 pin 18
signal_e = 2 # GPIO pin 27
signal_f = 3 # GPIO pin 22
signal_g = 4 # GPIO pin 23
signal_a = 5 # GPIO pin 24
signal_b = 6 # GPIO pin 25
signal_c_2 = 7 # GPIO pin 4

c = 59
d = 61
e = 63
f = 64
g = 66
a = 68
b = 70
c2 = 71

# sets signal wires to receive input
wp.pinMode(signal_a, 0)
wp.pinMode(signal_b, 0)

print "Press enter to quit."

isOnC = False
isOnD = False
isOnE = False
isOnF = False
isOnG = False
isOnA = False
isOnB = False
isOnC2 = False

while True:
	# checks if user pressed enter.
	os.system('clear') # clears terminal.
	if sys.stdin in select.select([sys.stdin], [], [], 0)[0]: # reads from standard input.
		line = raw_input()
		break
	
	if wp.digitalRead(signal_c) == 1: # 1 is HIGH, 0 is LOW
		if isOnC == False:
			player.note_on(c, 127)
			isOnC = True
	elif wp.digitalRead(signal_c) == 0:
			player.note_off(c, 127)
			isOnC = False
	
	if wp.digitalRead(signal_d) == 1:
		if not isOnD:
			player.note_on(d, 127)
			isOnD = True
	elif wp.digitalRead(signal_d) == 0:
		player.note_off(d, 127)
		isOnD = False
	
	if wp.digitalRead(signal_e) == 1:
		if not isOnE:
			player.note_on(e, 127)
			isOnE = True
	elif wp.digitalRead(signal_e) == 0:
		player.note_off(e, 127)
		isOnE = False
	
	if wp.digitalRead(signal_f) == 1:
		if not isOnF:
			player.note_on(f, 127)
			isOnF = True
	elif wp.digitalRead(signal_f) == 0:
		player.note_off(f, 127)
		isOnF = False
	
	if wp.digitalRead(signal_g) == 1:
		if not isOnG:
			player.note_on(g, 127)
			isOnG = True
	elif wp.digitalRead(signal_g) == 0:
		player.note_off(g, 127)
		isOnG = False
	
	if wp.digitalRead(signal_a) == 1:
		if not isOnA:
			player.note_on(a, 127)
			isOnA = True
	elif wp.digitalRead(signal_a) == 0:
		player.note_off(a, 127)
		isOnA = False
	
	if wp.digitalRead(signal_b) == 1:
		if not isOnB:
			player.note_on(b, 127)
			isOnB = True
	elif wp.digitalRead(signal_b) == 0:
		player.note_off(b, 127)
		isOnB = False
		
	if wp.digitalRead(signal_c_2) == 1:
		if not isOnC2:
			player.note_on(c2, 127)
			isOnC2 = True
	elif wp.digitalRead(signal_c_2) == 0:
		player.note_off(c2, 127)
		isOnC2 = False
		
del player
pygame.midi.quit()
