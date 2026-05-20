"""
Page manage and main entrance
"""

import streamlit as st

# 可选：页面配置（建议加）
st.set_page_config(page_title="My App", layout="wide")

# ===== Sidebar 公告 =====
with st.sidebar:
    st.title("📢 个人RAG作品展示")

    st.markdown("""
    ### 
    - 当前版本：v0.1.0
    - 功能：支持提问 + 知识库文档管理
    - 作者：Arthas Liu
    - 作技术栈：streamlit + python + langchain
    - embedding/ai model：同义/tongyi
                
    ---

    ⚠️ 功能介绍：
                
    - 支持上传md5,txt,pdf,csv文件到知识库。
                
    - 提问会从知识库中进行匹配回答，非知识库中会告知无相关信息。
                
    - 保留了最近的上下文chat history拼到chain中,优化prompt
                
    - 仅供展示RAG项目的核心功能
    """)

pg = st.navigation(
    [
        st.Page("front/views/chat.py", title="chat", icon="💬"),
        st.Page("front/views/lib.py", title="lib", icon="📚"),
    ]
)

pg.run()
