set pagination off
set logging on

set $start_address = 0x0804840c
set $target_range = (unsigned int)($start_address & 0xffff0000)
b *$start_address
run

while 1
   set $x = ((unsigned int)$eip) & 0xffff0000
   if $x == $target_range
      printf "=> 0x%08x\n", $eip
      si
   else
      finish
   end
end
