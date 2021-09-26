:loop
start chrome https://web.whatsapp.com/
timeout /t 60 /nobreak
"C:\Users\joo\Anaconda3\python.exe" "C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS\AUTO_WEATHER_WHATSAPP.py"
%windir%\system32\rundll32.exe advapi32.dll,ProcessIdleTasks
timeout /t 500 /nobreak
taskkill /F /IM chrome.exe /T
goto :loop