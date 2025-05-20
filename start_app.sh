#!/bin/bash

echo "正在启动CHARLS数据可视化系统..."
echo "请稍候，系统正在加载中..."

# 尝试激活虚拟环境（如果存在）
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# 安装必要的依赖
pip install -r requirements.txt

# 启动Streamlit应用
streamlit run app.py

# 如果应用意外关闭
echo ""
echo "应用已关闭。按任意键退出..."
read -n 1 