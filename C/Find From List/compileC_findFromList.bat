@echo off

set filename="findFromList"

if exist %filename%.c goto compile
if not exist %filename%.c goto error

:compile

cmd /c "gcc -o %filename% %filename%.c"
@echo compilation complete
pause
exit

:error
@echo file %filename%.c does not exist
pause
exit
