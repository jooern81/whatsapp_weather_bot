:loop
start chrome https://web.whatsapp.com/
timeout /t 60 /nobreak
"C:\Users\joo\Anaconda3\python.exe" "C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS PATCH 1\AUTO_WEATHER_WHATSAPP_sort.py"
%windir%\system32\rundll32.exe advapi32.dll,ProcessIdleTasks
timeout /t 500 /nobreak
taskkill /F /IM chrome.exe /T
goto :loop