#Created By: Milad Khoshdel
#Special Thanks: Mikili
#Blog: https://blog.regux.com
#Email: miladkhoshdel@gmail.com
#Telegram: @miladkho5hdel

import socket
import subprocess
import ipaddress

def banner():
	print (' ')
	print ('###################################################################################################')
	print ('##                                                                                               ##')
	print ('##     /\  \                                   /\  \         /\  \                     /|  |     ##')
	print ('##    |::\  \       ___                       /::\  \       |::\  \       ___         |:|  |     ##')
	print ('##    |:|:\  \     /\__\                     /:/\:\  \      |:|:\  \     /\__\        |:|  |     ##')
	print ('##  __|:|\:\  \   /:/__/      ___     ___   /:/ /::\  \   __|:|\:\  \   /:/__/      __|:|  |     ##')
	print ('## /::::|_\:\__\ /::\  \     /\  \   /\__\ /:/_/:/\:\__\ /::::|_\:\__\ /::\  \     /\ |:|__|____ ##')
	print ('## \:\~~\  \/__/ \/\:\  \__  \:\  \ /:/  / \:\/:/  \/__/ \:\~~\  \/__/ \/\:\  \__  \:\/:::::/__/ ##')
	print ('##  \:\  \        ~~\:\/\__\  \:\  /:/  /   \::/__/       \:\  \        ~~\:\/\__\  \::/~~/~     ##')
	print ('##   \:\  \          \::/  /   \:\/:/  /     \:\  \        \:\  \          \::/  /   \:\~~\      ##')
	print ('##    \:\__\         /:/  /     \::/  /       \:\__\        \:\__\         /:/  /     \:\__\     ##')
	print ('##     \/__/         \/__/       \/__/         \/__/         \/__/         \/__/       \/__/     ##')
	print ('##                                                                                               ##')
	print ('##                                                                                               ##')
	print ('##                                                                BY: Milad Khoshdel | Mikili    ##')
	print ('##                                                                Blog: https://blog.regux.com   ##')
	print ('##                                                                                               ##')
	print ('###################################################################################################')
	print (' ')
	
banner()
port = raw_input('Enter port > ')
range_host = raw_input('Enter IP Range > ')

net1 = unicode(range_host)
net2 = ipaddress.ip_network(net1)

counting_open = []
counting_close = []

for x in net2.hosts():

	sock = socket.socket()
	sock.settimeout(0.5)
	result = sock.connect_ex((str(x),int(port)))
	
	if result == 0:
		print 'Port ' + str(port) + " is OPEN on " + str(x)
		sock.close()
	else:
		print 'Port ' + str(port) + " is CLOSE on " + str(x) 
		sock.close()
