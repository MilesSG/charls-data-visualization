import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from pyecharts.charts import Bar, Pie, Line, Radar, Funnel
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts
from styles import STYLES
import json
import os
import uuid

# 确保data目录存在
DATA_DIR = "data"
SURVEY_FILE = os.path.join(DATA_DIR, "survey_data.json")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 如果JSON文件不存在，创建一个空的JSON文件
if not os.path.exists(SURVEY_FILE):
    with open(SURVEY_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=4)

def load_survey_data():
    try:
        if not os.path.exists(SURVEY_FILE):
            return []
        with open(SURVEY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception as e:
        st.error(f"加载数据时出错: {str(e)}")
        return []

def save_survey_data(data):
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(SURVEY_FILE), exist_ok=True)
        
        # 确保数据是列表类型
        if not isinstance(data, list):
            raise ValueError("数据必须是列表类型")
        
        # 写入文件前先读取现有数据进行比较
        current_data = load_survey_data()
        if current_data != data:  # 只有当数据真的改变时才写入
            with open(SURVEY_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            st.write("数据已更新到文件")
            return True
        else:
            st.write("数据未发生变化，无需保存")
            return False
    except Exception as e:
        st.error(f"保存数据时出错: {str(e)}")
        return False

def add_survey(survey_data):
    data = load_survey_data()
    survey_data['id'] = str(uuid.uuid4())
    survey_data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.append(survey_data)
    save_survey_data(data)

def update_survey(survey_id, updated_data):
    data = load_survey_data()
    for i, item in enumerate(data):
        if item['id'] == survey_id:
            # 保留原有的ID和创建时间
            updated_data['id'] = item['id']
            updated_data['created_at'] = item['created_at']
            # 添加更新时间
            updated_data['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 更新数据
            data[i] = updated_data
            break
    save_survey_data(data)

def delete_survey(survey_id):
    data = load_survey_data()
    data = [item for item in data if item['id'] != survey_id]
    save_survey_data(data)

# 设置页面配置
st.set_page_config(
    page_title="CHARLS数据可视化大屏",
    page_icon="📊",
    layout="wide",
)

# 添加样式
st.markdown(STYLES, unsafe_allow_html=True)

# 显示主要内容
st.title("🏥 中国健康与养老追踪调查(CHARLS)数据可视化")

# 创建一个按钮来显示/隐藏管理系统
if 'show_management' not in st.session_state:
    st.session_state.show_management = False

# 在右上角添加管理系统按钮
with st.container():
    st.markdown(
        '<div style="position: relative; height: 0;">',
        unsafe_allow_html=True
    )
    if st.button("📋 问卷管理系统", key="manage_button", help="点击管理问卷数据", type="primary"):
        st.session_state.show_management = not st.session_state.show_management
    st.markdown('</div>', unsafe_allow_html=True)

# 如果按钮被点击，显示管理系统
if st.session_state.show_management:
    with st.container():
        st.markdown('<div class="management-system">', unsafe_allow_html=True)
        
        # 如果正在编辑问卷，显示编辑表单
        if st.session_state.get('show_edit_form', False):
            with st.form("edit_form"):
                st.subheader("编辑问卷")
                survey = st.session_state['editing_survey']
                
                col1, col2 = st.columns(2)
                with col1:
                    age = st.number_input("年龄", min_value=1, max_value=120, value=int(survey['age']))
                with col2:
                    gender = st.selectbox("性别", ["男", "女"], index=0 if survey['gender']=="男" else 1)
                
                health_status = st.selectbox(
                    "健康状况自评",
                    ["很好", "好", "一般", "差", "很差"],
                    index=["很好", "好", "一般", "差", "很差"].index(survey['health_status'])
                )
                has_chronic_disease = st.checkbox("是否有慢性病", value=survey['has_chronic_disease'])
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.form_submit_button("保存修改", type="primary", use_container_width=True):
                        updated_data = {
                            "age": int(age),
                            "gender": gender,
                            "health_status": health_status,
                            "has_chronic_disease": has_chronic_disease,
                            "id": survey['id'],
                            "created_at": survey['created_at']
                        }
                        update_survey(survey['id'], updated_data)
                        st.session_state.pop('editing_survey', None)
                        st.session_state.pop('show_edit_form', None)
                        st.success("✅ 修改成功！")
                        st.rerun()
                with col2:
                    if st.form_submit_button("取消编辑", type="secondary", use_container_width=True):
                        st.session_state.pop('editing_survey', None)
                        st.session_state.pop('show_edit_form', None)
                        st.rerun()
            
            # 添加一个分隔线
            st.markdown("---")
        
        # 创建标签页
        tab1, tab2 = st.tabs(["📋 问卷列表", "+ 添加新问卷"])
        
        # 问卷列表标签页
        with tab1:
            survey_data = load_survey_data()
            if survey_data:
                # 分页设置
                ITEMS_PER_PAGE = 5  # 每页显示5个卡片（一行）
                
                if 'current_page' not in st.session_state:
                    st.session_state.current_page = 0
                
                total_pages = len(survey_data) // ITEMS_PER_PAGE + (1 if len(survey_data) % ITEMS_PER_PAGE > 0 else 0)
                start_idx = st.session_state.current_page * ITEMS_PER_PAGE
                end_idx = min(start_idx + ITEMS_PER_PAGE, len(survey_data))
                
                # 创建一行5列的布局
                cols = st.columns(5)
                
                # 填充这一行的卡片
                for col_idx, item_idx in enumerate(range(start_idx, end_idx)):
                    with cols[col_idx]:
                        item = survey_data[item_idx]
                        # 创建一个简单的卡片布局
                        st.markdown(f"""
                            <div style='padding: 15px; background: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 15px;'>
                                <div style='font-size: 24px; font-weight: bold; color: #0066cc; text-align: center; margin-bottom: 10px;'>
                                    {item['age']} 岁
                                </div>
                                <div style='margin: 5px 0; padding: 8px; background: #f8f9fa; border-radius: 5px;'>
                                    <span style='color: #666;'>性别：</span>{item['gender']}
                                </div>
                                <div style='margin: 5px 0; padding: 8px; background: #f8f9fa; border-radius: 5px;'>
                                    <span style='color: #666;'>慢性病：</span>{'是' if item['has_chronic_disease'] else '否'}
                                </div>
                                <div style='margin: 5px 0; padding: 8px; background: #f8f9fa; border-radius: 5px;'>
                                    <span style='color: #666;'>健康状况：</span>{item['health_status']}
                                </div>
                                <div style='font-size: 10px; color: #999; text-align: right; margin-top: 5px;'>
                                    创建于: {item['created_at']}
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # 按钮组
                        btn_cols = st.columns(2)
                        with btn_cols[0]:
                            if st.button("✏️ 编辑", key=f"edit_{item['id']}_{item_idx}", use_container_width=True):
                                st.session_state['editing_survey'] = item
                                st.session_state['show_edit_form'] = True
                                st.rerun()
                        with btn_cols[1]:
                            if st.button("🗑️ 删除", key=f"delete_{item['id']}_{item_idx}", use_container_width=True):
                                delete_survey(item['id'])
                                st.rerun()
                
                # 填充空白列以保持布局一致
                for col_idx in range(end_idx - start_idx, 5):
                    with cols[col_idx]:
                        st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
                
                # 分页控制
                if total_pages > 1:
                    st.markdown("<br>", unsafe_allow_html=True)  # 添加一些间距
                    cols = st.columns([2, 1, 2, 1, 2])
                    with cols[1]:
                        if st.button("上一页", disabled=st.session_state.current_page == 0, use_container_width=True):
                            st.session_state.current_page -= 1
                            st.rerun()
                    with cols[2]:
                        st.markdown(f"""
                            <div style='text-align: center; padding: 8px; background: #f8f9fa; border-radius: 4px;'>
                                第 {st.session_state.current_page + 1} / {total_pages} 页
                            </div>
                        """, unsafe_allow_html=True)
                    with cols[3]:
                        if st.button("下一页", disabled=st.session_state.current_page == total_pages - 1, use_container_width=True):
                            st.session_state.current_page += 1
                            st.rerun()
            else:
                st.info("📭 暂无问卷数据")
        
        # 添加新问卷标签页
        with tab2:
            with st.form("add_survey_form"):
                st.subheader("添加新问卷")
                
                col1, col2 = st.columns(2)
                with col1:
                    age = st.number_input("年龄", min_value=1, max_value=120, value=45)
                with col2:
                    gender = st.selectbox("性别", ["男", "女"])
                
                health_status = st.selectbox(
                    "健康状况自评",
                    ["很好", "好", "一般", "差", "很差"]
                )
                has_chronic_disease = st.checkbox("是否有慢性病")
                
                if st.form_submit_button("提交", type="primary"):
                    new_survey = {
                        "age": int(age),
                        "gender": gender,
                        "health_status": health_status,
                        "has_chronic_disease": has_chronic_disease,
                        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    add_survey(new_survey)
                    st.success("✅ 添加成功！")
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

try:
    # 第一行：关键指标展示
    st.markdown("### 📊 关键指标概览")
    
    # 创建指标容器
    st.markdown('''
    <div class="metrics-container">
        <div class="metrics-grid">
            <div class="metric-item">
                <div class="metric-label">基线调查样本量</div>
                <div class="metric-value">17,708</div>
                <div class="metric-delta positive">覆盖28个省份</div>
            </div>
            <div class="metric-item">
                <div class="metric-label">受访者平均年龄</div>
                <div class="metric-value">60.2岁</div>
                <div class="metric-delta">45岁以上人群</div>
            </div>
            <div class="metric-item">
                <div class="metric-label">慢性病患病率</div>
                <div class="metric-value">75.3%</div>
                <div class="metric-delta negative">需要关注</div>
            </div>
            <div class="metric-item">
                <div class="metric-label">医保覆盖率</div>
                <div class="metric-value">95.7%</div>
                <div class="metric-delta positive">全民覆盖</div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # 第二行：四列布局
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('''
        <div class="metrics-container">
            <div class="visualization-title">样本数量与跟踪率变化趋势</div>
            <div class="sample-stats">
                <div class="stat-row">
                    <div class="year-label">2020年样本量</div>
                    <div class="sample-number">14960</div>
                    <div class="trend-indicator trend-down">↓ 2.4%</div>
                </div>
                <div class="stat-row">
                    <div class="year-label">2018年样本量</div>
                    <div class="sample-number">15331</div>
                    <div class="trend-indicator trend-down">↓ 3.6%</div>
                </div>
                <div class="stat-row">
                    <div class="year-label">2015年样本量</div>
                    <div class="sample-number">15900</div>
                    <div class="trend-indicator trend-down">↓ 5.4%</div>
                </div>
                <div class="stat-row">
                    <div class="year-label">2013年样本量</div>
                    <div class="sample-number">16810</div>
                    <div class="trend-indicator trend-down">↓ 5.1%</div>
                </div>
                <div class="stat-row">
                    <div class="year-label">2011年基线样本量</div>
                    <div class="sample-number">17708</div>
                    <div class="trend-indicator trend-up">基线年份</div>
                </div>
                <div class="tracking-rate">
                    <div class="stat-row">
                        <div class="year-label">当前跟踪率</div>
                        <div class="tracking-number">84.5%</div>
                    </div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
        st.markdown('<div class="visualization-title">各年龄段健康状况分析</div>', unsafe_allow_html=True)
        # 健康状况雷达图
        radar = Radar()
        radar.add_schema(
            schema=[
                opts.RadarIndicatorItem(name="自评健康良好率", max_=100),
                opts.RadarIndicatorItem(name="慢性病患病率", max_=100),
                opts.RadarIndicatorItem(name="抑郁症状检出率", max_=100),
                opts.RadarIndicatorItem(name="日常活动受限率", max_=100),
                opts.RadarIndicatorItem(name="认知功能正常率", max_=100)
            ]
        )
        radar.add("45-54岁", [[78.5, 65.2, 25.4, 15.3, 92.1]])
        radar.add("55-64岁", [[65.3, 72.8, 32.6, 25.7, 85.4]])
        radar.add("65-74岁", [[52.1, 81.5, 38.9, 35.8, 75.2]])
        radar.add("75岁以上", [[38.6, 88.7, 45.2, 52.3, 62.8]])
        st_pyecharts(radar, height="400px")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
        st.markdown('<div class="visualization-title">教育水平分布</div>', unsafe_allow_html=True)
        # 教育水平分布饼图
        edu_pie = Pie()
        edu_data = [
            ("文盲", 27.3),
            ("小学", 38.4),
            ("初中", 21.6),
            ("高中/中专", 9.8),
            ("大专及以上", 2.9)
        ]
        edu_pie.add(
            series_name="教育水平",
            data_pair=edu_data,
            radius=["35%", "70%"]
        )
        edu_pie.set_colors(["#0066cc", "#30b0c7", "#5ac8c8", "#7bd2be", "#98ddb6"])
        st_pyecharts(edu_pie, height="400px")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
        st.markdown('<div class="visualization-title">家庭年收入分布</div>', unsafe_allow_html=True)
        # 收入水平分布饼图
        income_pie = Pie()
        income_data = [
            ("低收入(≤1万)", 18.5),
            ("中低收入(1-3万)", 35.2),
            ("中等收入(3-5万)", 24.8),
            ("中高收入(5-10万)", 15.6),
            ("高收入(>10万)", 5.9)
        ]
        income_pie.add(
            series_name="年收入水平",
            data_pair=income_data,
            radius=["35%", "70%"]
        )
        income_pie.set_colors(["#0066cc", "#1a8cff", "#30b0c7", "#5ac8c8", "#7bd2be"])
        st_pyecharts(income_pie, height="400px")
        st.markdown('</div>', unsafe_allow_html=True)

    # 第三行：四列布局
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
        st.markdown('<div class="visualization-title">医疗保险覆盖情况</div>', unsafe_allow_html=True)
        # 医疗保险分布饼图
        pie = Pie()
        insurance_data = [
            ("城镇职工医保", 32.5),
            ("城乡居民医保", 41.8),
            ("新农合", 18.4),
            ("商业医疗保险", 3.8),
            ("公费医疗", 2.2),
            ("大病保险", 0.9),
            ("其他补充医疗保险", 0.4)
        ]
        pie.add(
            series_name="医疗保险覆盖率",
            data_pair=insurance_data,
            radius=["35%", "70%"]
        )
        pie.set_colors(["#0066cc", "#1a8cff", "#30b0c7", "#45b4c7", "#5ac8c8", "#6fccc8", "#85d0c8"])
        st_pyecharts(pie, height="400px")
        st.markdown('</div>', unsafe_allow_html=True)

    with col6:
        st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
        st.markdown('<div class="visualization-title">主要慢性病患病率趋势</div>', unsafe_allow_html=True)
        # 慢性病趋势折线图
        line2 = Line()
        years = ["2011", "2013", "2015", "2018", "2020"]
        diseases = {
            "高血压": [38.5, 39.2, 41.3, 43.2, 44.8],
            "糖尿病": [15.2, 16.1, 17.3, 18.5, 19.4],
            "心脏病": [22.3, 23.8, 24.2, 25.8, 26.9],
            "关节炎": [31.4, 32.8, 33.2, 34.7, 35.1],
            "慢性肺病": [12.2, 12.6, 13.1, 13.4, 13.9],
            "消化系统疾病": [20.5, 21.8, 22.1, 22.6, 23.2],
            "恶性肿瘤": [2.8, 3.1, 3.4, 3.6, 3.9]
        }
        line2.add_xaxis(years)
        colors = ["#0066cc", "#1a8cff", "#30b0c7", "#45b4c7", "#5ac8c8", "#6fccc8", "#85d0c8"]
        for i, (disease, data) in enumerate(diseases.items()):
            line2.add_yaxis(
                disease,
                data,
                is_smooth=True,
                symbol="circle",
                symbol_size=1,
                linestyle_opts=opts.LineStyleOpts(width=2, opacity=0.8),
                label_opts=opts.LabelOpts(is_show=False),
                itemstyle_opts=opts.ItemStyleOpts(color=colors[i])
            )
        st_pyecharts(line2, height="400px")
        st.markdown('</div>', unsafe_allow_html=True)

    with col7:
        st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
        st.markdown('<div class="visualization-title">城乡健康差异对比</div>', unsafe_allow_html=True)
        # 城乡对比柱状图
        bar = Bar()
        categories = ["自评健康良好率", "慢性病患病率", "医保覆盖率", "就医可及性", "养老保险覆盖率"]
        urban_data = [68.5, 72.3, 97.5, 92.8, 89.6]
        rural_data = [58.2, 78.4, 93.8, 75.2, 82.3]
        bar.add_xaxis(categories)
        bar.add_yaxis("城市", urban_data, itemstyle_opts=opts.ItemStyleOpts(color="#0066cc"))
        bar.add_yaxis("农村", rural_data, itemstyle_opts=opts.ItemStyleOpts(color="#30b0c7"))
        st_pyecharts(bar, height="400px")
        st.markdown('</div>', unsafe_allow_html=True)

    with col8:
        st.markdown('<div class="metrics-container">', unsafe_allow_html=True)
        st.markdown('<div class="visualization-title">养老方式分析</div>', unsafe_allow_html=True)
        # 养老方式漏斗图
        funnel = Funnel()
        funnel_data = [
            ("与子女同住", 41.3),
            ("独立居住", 37.8),
            ("社区养老", 12.5),
            ("机构养老", 5.2),
            ("其他方式", 3.2)
        ]
        funnel.add(
            series_name="养老方式",
            data_pair=funnel_data,
            label_opts=opts.LabelOpts(position="inside", formatter="{b}: {c}%")
        )
        funnel.set_colors(["#0066cc", "#1a8cff", "#30b0c7", "#45b4c7", "#5ac8c8"])
        st_pyecharts(funnel, height="400px")
        st.markdown('</div>', unsafe_allow_html=True)

    # 添加数据来源说明
    st.markdown("""
    <div style='text-align: center; color: #333333; padding: 20px;'>
    数据来源：中国健康与养老追踪调查(CHARLS)2011-2020年调查数据
    </div>
    """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"发生错误: {str(e)}")
