STYLES = """
    <style>
    /* 基础样式 */
    .main {
        position: relative;
        overflow: auto !important;
    }
    
    .stApp {
        position: relative;
        min-height: 100vh;
        overflow: auto !important;
    }

    /* 添加滚动条样式，使其更美观 */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #c1c1c1;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #a8a8a8;
    }

    /* 内容样式 */
    .block-container {
        padding: 2rem 1rem !important;
        max-width: 95% !important;
        position: relative;
        z-index: 1;
        background: transparent !important;
        overflow: visible !important;
    }

    /* 确保内容不被截断 */
    .st-emotion-cache-1wmy9hl, .st-emotion-cache-1oypcwj {
        overflow: visible !important;
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
    
    /* 系统功能模块样式 */
    .system-modules-container {
        background: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 30px;
        position: relative;
        z-index: 10;
        max-height: none !important;
        overflow: visible !important;
    }
    
    .system-info-summary {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    }
    
    .system-info-title {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 15px;
        color: #2c3e50;
    }
    
    .system-info-details {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
    }
    
    .info-item {
        background: rgba(255, 255, 255, 0.8);
        padding: 12px 15px;
        border-radius: 10px;
        flex: 1 1 200px;
    }
    
    .info-label {
        font-weight: 500;
        color: #555;
    }
    
    .info-value {
        font-weight: 600;
        color: #1a73e8;
    }
    
    .status-operational {
        color: #0ca678;
    }
    
    .status-warning {
        color: #f59f00;
    }
    
    .status-error {
        color: #e03131;
    }
    
    .status-unknown {
        color: #868e96;
    }
    
    /* 模块卡片样式 */
    .module-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .module-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
    }
    
    .module-title {
        font-size: 18px;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 10px;
        border-bottom: 2px solid #f0f4f8;
        padding-bottom: 8px;
    }
    
    .module-description {
        font-size: 14px;
        color: #64748b;
        margin-bottom: 15px;
        min-height: 60px;
    }
    
    .module-stats {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
    }
    
    .stat-item {
        text-align: center;
        padding: 8px;
        background: #f8fafc;
        border-radius: 8px;
    }
    
    .stat-value {
        display: block;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .stat-label {
        font-size: 12px;
        color: #64748b;
    }
    
    .status-active {
        color: #0ca678;
    }
    
    .status-in-development {
        color: #f59f00;
    }
    
    .status-planned {
        color: #868e96;
    }
    
    /* 系统状态卡片 */
    .system-status-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        text-align: center;
        height: 100%;
    }
    
    .status-icon {
        font-size: 24px;
        width: 50px;
        height: 50px;
        line-height: 50px;
        border-radius: 50%;
        margin: 0 auto 15px;
    }
    
    .status-good {
        background: rgba(12, 166, 120, 0.15);
        color: #0ca678;
    }
    
    .status-warning {
        background: rgba(245, 159, 0, 0.15);
        color: #f59f00;
    }
    
    .status-error {
        background: rgba(224, 49, 49, 0.15);
        color: #e03131;
    }
    
    .status-title {
        font-size: 16px;
        font-weight: 500;
        color: #64748b;
        margin-bottom: 8px;
    }
    
    .status-value {
        font-size: 20px;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 8px;
    }
    
    .status-detail {
        font-size: 12px;
        color: #94a3b8;
    }
    
    /* 统计容器 */
    .stats-container {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        height: 100%;
    }
    
    /* 更新项目样式 */
    .update-item {
        padding: 12px;
        border-bottom: 1px solid #f0f4f8;
        display: flex;
        align-items: flex-start;
    }
    
    .update-date {
        font-size: 14px;
        font-weight: 500;
        color: #64748b;
        min-width: 100px;
    }
    
    .update-desc {
        font-size: 14px;
        color: #334155;
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

    /* 确保长表格内容可滚动 */
    .stMarkdown {
        overflow: auto !important;
    }
    
    /* 确保所有expandable内容可见 */
    .streamlit-expanderContent {
        overflow: visible !important;
    }
    
    /* 修复streamlit原生容器的滚动问题 */
    .css-1d391kg, .css-12oz5g7 {
        overflow: visible !important;
    }
    
    /* 适配移动设备 */
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem 0.5rem !important;
        }
        
        .metrics-container, .system-modules-container {
            padding: 15px;
        }
    }
    </style>
""" 