# coding: utf-8

#!/usr/bin/env python
#Dependencies check
import os
errors = 0
if version_compare("7.0", PHP_VERSION) > 0:
	print("[CRITICAL] Use PHP >= 7.0" + PHP_EOL)
	++errors

if not extension_loaded("sockets"):
	print("[CRITICAL] Unable to find the Socket extension." + PHP_EOL)
	++errors

if not extension_loaded("pthreads"):
	print("[CRITICAL] Unable to find the pthreads extension." + PHP_EOL);
	++errors;
else:
	pthreads_version = phpversion("pthreads")
	if substr_count(pthreads_version, ".") < 2:
		pthreads_version = "0.$pthreads_version"
	
	if version_compare(pthreads_version, "3.0.0") < 0:
		print("[CRITICAL] pthreads >= 3.0.0 is required, while you have $pthreads_version.")
		++errors
	

if errors > 0:
	exit(1) #Exit with error

unset(errors)
class RakLib:
	VERSION = "0.8.0"
	PROTOCOL = 6
	MAGIC = "\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"
	PRIORITY_NORMAL = 0
	PRIORITY_IMMEDIATE = 1
	FLAG_NEED_ACK = 0b00001000
	'''
	 * Internal Packet:
	 * int32 (length without this field)
	 * byte (packet ID)
	 * payload
	 */
	/*
	 * ENCAPSULATED payload:
	 * byte (identifier length)
	 * byte[] (identifier)
	 * byte (flags, last 3 bits, priority)
	 * payload (binary internal EncapsulatedPacket)
	 */'''
	PACKET_ENCAPSULATED = 0x01
	'''
	/*
	 * OPEN_SESSION payload:
	 * byte (identifier length)
	 * byte[] (identifier)
	 * byte (address length)
	 * byte[] (address)
	 * short (port)
	 * long (clientID)
	 */
	 '''
	PACKET_OPEN_SESSION = 0x02
	'''
	/*
	 * CLOSE_SESSION payload:
	 * byte (identifier length)
	 * byte[] (identifier)
	 * string (reason)
	 */
	 '''
	PACKET_CLOSE_SESSION = 0x03
	'''
	/*
	 * INVALID_SESSION payload:
	 * byte (identifier length)
	 * byte[] (identifier)
	 */
	 '''
	PACKET_INVALID_SESSION = 0x04
	'''
	/* TODO: implement this
	 * SEND_QUEUE payload:
	 * byte (identifier length)
	 * byte[] (identifier)
	 */
	 '''
	PACKET_SEND_QUEUE = 0x05
	'''
	/*
	 * ACK_NOTIFICATION payload:
	 * byte (identifier length)
	 * byte[] (identifier)
	 * int (identifierACK)
	 */
	 '''
	PACKET_ACK_NOTIFICATION = 0x06
	'''
	/*
	 * SET_OPTION payload:
	 * byte (option name length)
	 * byte[] (option name)
	 * byte[] (option value)
	 */
	 '''
	PACKET_SET_OPTION = 0x07
	'''
	/*
	 * RAW payload:
	 * byte (address length)
	 * byte[] (address from/to)
	 * short (port)
	 * byte[] (payload)
	 */
	 '''
	PACKET_RAW = 0x08
	'''
	/*
	 * RAW payload:
	 * byte (address length)
	 * byte[] (address)
	 * int (timeout)
	 */
	 '''
	PACKET_BLOCK_ADDRESS = 0x09
	'''
	/*
	 * RAW payload:
	 * byte (address length)
	 * byte[] (address)
	 */
	 '''
	PACKET_UNBLOCK_ADDRESS = 0x0a
	'''
	/*
	 * No payload
	 *
	 * Sends the disconnect message, removes sessions correctly, closes sockets.
	 */
	 '''
	PACKET_SHUTDOWN = 0x7e
	'''
	/*
	 * No payload
	 *
	 * Leaves everything as-is and halts, other Threads can be in a post-crash condition.
	 *'''
	PACKET_EMERGENCY_SHUTDOWN = 0x7f
	def bootstrap(loader):
		os.chdir(loader)
	#hmmm this is almost certianly wrong not surr hoe this is to be done though sorry :(p)
