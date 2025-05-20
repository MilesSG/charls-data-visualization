@echo off
echo 正在启动CHARLS数据可视化系统...
echo 请稍候，系统正在加载中...

REM 尝试激活虚拟环境（如果存在）
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
)

REM 安装必要的依赖（如果尚未安装）
pip install -r requirements.txt

REM 启动Streamlit应用
streamlit run app.py

REM 如果应用意外关闭
echo.
echo 应用已关闭。按任意键退出...
pause > nul 