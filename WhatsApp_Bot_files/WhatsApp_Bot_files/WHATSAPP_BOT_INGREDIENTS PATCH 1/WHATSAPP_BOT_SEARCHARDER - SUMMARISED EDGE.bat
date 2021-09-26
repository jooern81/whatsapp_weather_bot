:loop
start https://web.whatsapp.com/
timeout /t 60 /nobreak
"C:\Users\joo\Anaconda3\python.exe" "C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS PATCH 1\AUTO_WEATHER_WHATSAPP_SEARCHARDER2.py"
timeout /t 500 /nobreak
taskkill /F /IM MicrosoftEdge.exe /T 
@call cscript "%~dp0FREEMEM.vbs"
@call cscript "%~dp0FREEMEM2.vbs"
goto :loop