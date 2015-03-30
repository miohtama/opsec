# Laptops and workstations

## Hard disk encryption

Don't use SSHD hybrid drives which combine a traditional mechanical hard drive with a small SSD cache.  It's unclear/unconfirmed if full disk encryption supports these drives and even if you format the hard drive the cache may still leak plain text data.


### Linux

BIOS password
LUKS

### OSX

EFI password

### Windows

BIOS password

## Sleep and password

## Physical security


Kensington Lock

Simple way to prevent opportunistic theft from cafe or trade show.  Does not work with Apple laptops released over the last few years as they removed the Kensington lock beginning with some/all Unibody machines.

Disable ports
- Someone could plug in a USB flash drive to damage your computer e.g. "Killer USB"
  - http://kukuruku.co/hub/diy/usb-killer
- Someone could plug in a USB flash drive to infect your operating system with malware
- Someone could plug a device into the Firewire or Thunderbolt port to launch a DMA attack of 
 - https://github.com/carmaa/inception
 - https://www.youtube.com/watch?v=q0HthE3qDMw
 - One solution is to block unused ports which may be vulnerable e.g. use epoxy or putty from a hardware store.  This of course will affect the resale value of your laptop unless there is a non-permanent solution.


Power Down Machine
- If you must leave laptop unattended e.g. in a hotel room, at an exhibition, even in the office when popping out for lunch
- When travelling
