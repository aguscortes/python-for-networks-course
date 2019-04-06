#!/bin/python
import subprocess
import optparse

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC Address')
	parser.add_option('-m', '--mac', dest='new_mac', help='Interface to change its MAC Address')
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error('Please specify an interface, use --help form more info')
	elif not options.new_mac:
		parser.error('Please specify a new mac, use --help form more info')
	return options

def change_mac(interface, new_mac):
	print('Changing MAC address for: ' + interface + ' to ' +  new_mac)
	subprocess.call(['ifconfig', interface, 'down'])
	subprocess.call(['ifconfig', interface, 'hw', 'ether',new_mac])
	subprocess.call(['ifconfig', interface, 'up'])

def validate_mac(interface, new_mac):
	subprocess.call(['ifconfig', '|' 'grep','-A1', interface, '|', 'tail','-1'])


options = get_arguments()
change_mac(options.interface, options.new_mac)
validate_mac(options.interface, options.new_mac)
