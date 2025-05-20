Set WshShell = CreateObject("WScript.Shell")
WshShell.Popup "正在启动CHARLS数据可视化系统，请稍候...", 2, "CHARLS数据可视化系统", 64

' 获取当前脚本所在目录
strScriptPath = Replace(WScript.ScriptFullName, WScript.ScriptName, "")

' 静默启动应用
WshShell.Run "cmd /c cd /d """ & strScriptPath & """ && pip install -r requirements.txt && streamlit run app.py", 0, False

' 告知用户
MsgBox "CHARLS数据可视化系统已在浏览器中启动！", 64, "CHARLS数据可视化系统" 