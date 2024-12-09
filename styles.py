STYLES = """
    <style>
    /* 基础样式 */
    .main {
        position: relative;
        overflow: hidden;
    }
    
    .stApp {
        position: relative;
        min-height: 100vh;
        overflow: hidden;
    }

    /* 内容样式 */
    .block-container {
        padding: 2rem 1rem !important;
        max-width: 95% !important;
        position: relative;
        z-index: 1;
        background: transparent !important;
    }

    /* 大屏样式 */
    .metrics-container {
        background: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
        margin-bottom: 30px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        position: relative;
        z-index: 1;
    }
    
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 25px;
        padding: 10px;
    }
    
    .metric-item {
        background: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
        text-align: center;
        transition: all 0.3s ease;
        animation: glow 3s ease-in-out infinite;
        position: relative;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        z-index: 1;
    }
    
    @keyframes glow {
        0% {
            box-shadow: 0 4px 24px rgba(0, 102, 204, 0.1);
        }
        50% {
            box-shadow: 0 4px 24px rgba(0, 102, 204, 0.2);
        }
        100% {
            box-shadow: 0 4px 24px rgba(0, 102, 204, 0.1);
        }
    }
    
    .metric-item:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 36px rgba(0, 102, 204, 0.25);
    }
    
    .metric-label {
        color: #86868b;
        font-size: 15px;
        font-weight: 500;
        margin-bottom: 10px;
    }
    
    .metric-value {
        color: #1d1d1f;
        font-size: 32px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    
    .metric-delta {
        font-size: 13px;
        padding: 4px 12px;
        border-radius: 20px;
        display: inline-block;
        font-weight: 500;
    }
    
    .metric-delta.positive {
        background-color: #e8fff3;
        color: #1d883a;
    }
    
    .metric-delta.negative {
        background-color: #fff1f0;
        color: #d70015;
    }
    
    .visualization-title {
        color: #1d1d1f;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 20px;
        padding-left: 15px;
        border-left: 4px solid #0066cc;
    }
    
    h1 {
        color: #1d1d1f;
        text-align: center;
        padding: 25px;
        font-size: 38px !important;
        font-weight: 600;
        margin-bottom: 35px;
        position: relative;
        z-index: 1;
    }
    
    h3 {
        color: #1d1d1f;
        padding: 15px;
        font-size: 24px !important;
        font-weight: 600;
        margin: 20px 0;
        border-left: 4px solid #0066cc;
    }
    
    .stMetric {
        display: none;
    }

    /* 确保所有Streamlit元素在动态背景之上 */
    .stMarkdown, .stButton, .stText, .stHeader, .element-container {
        position: relative;
        z-index: 1;
    }

    /* 问卷管理系统样式 */
    .management-system {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    .survey-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #eee;
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }

    .survey-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    .info-item {
        background: #f8f9fa;
        padding: 8px;
        margin: 8px 0;
        border-radius: 6px;
    }

    .info-label {
        color: #666;
        font-size: 13px;
        margin-bottom: 4px;
    }

    .info-value {
        color: #333;
        font-weight: 500;
    }

    .button-container {
        display: flex;
        gap: 10px;
        margin-top: 15px;
    }

    .stButton button {
        width: 100%;
    }

    /* 标签页样式 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 45px;
        border-radius: 8px;
        padding: 0 20px;
        font-weight: 500;
    }

    .stTabs [aria-selected="true"] {
        background-color: #0066cc !important;
        color: white !important;
    }

    /* 样本统计相关样式 */
    .sample-stats {
        background: white;
        border-radius: 10px;
        padding: 20px;
    }
    .stat-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px;
        margin: 5px 0;
        background: #f8f9fa;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stat-row:hover {
        background: #f0f2f5;
    }
    .year-label {
        color: #666;
        font-size: 14px;
        font-weight: 500;
        flex: 1;
    }
    .sample-number {
        color: #0066cc;
        font-size: 20px;
        font-weight: 600;
        margin: 0 20px;
    }
    .trend-indicator {
        font-size: 12px;
        padding: 4px 12px;
        border-radius: 12px;
        min-width: 80px;
        text-align: center;
    }
    .trend-down {
        background-color: #fff1f0;
        color: #d70015;
    }
    .trend-up {
        background-color: #e8fff3;
        color: #1d883a;
    }
    .tracking-rate {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid #eee;
    }
    .tracking-number {
        color: #30b0c7;
        font-size: 20px;
        font-weight: 600;
    }
    </style>
""" 