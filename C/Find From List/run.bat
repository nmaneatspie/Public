@echo off
setlocal enabledelayedexpansion

set filename="answer.txt"
if exist %filename% goto delete_file
if not exist %filename% goto run_prog

:delete_file
del "%~dp0%filename%"

goto run_prog

:run_prog
:: create blank file
@echo. >NUL>%filename%

set /p num=Number of inputs:
:: for hold for later use in loops
set /a temp=%num%

:: check validity of inputs
if %num% LEQ 0 goto error_module
if not %num% LEQ 0 goto initial_loop_input

:initial_loop_input
set inputs=

:loop_input
:: Gather all inputs in list
if %num%==0 (
	set /a num=%temp%
	cmd /c "cd /d %~dp0"
	goto exitloop_input
)

set /p word=Input word:
set inputs[%num%]=%word%
set /a num-=1

goto loop_input

:exitloop_input
if %num%==0 (
	Notepad %filename%
	pause
	exit
)

::run program with inputs as parameter
rem cmd /c "a.exe !inputs[%num%]!"
set /a num-=1

goto exitloop_input

:error_module
@echo Too few inputs (needs to be at least 1)
goto run_prog
