# 📚 RAG 知识库问答系统

一个基于 RAG（Retrieval-Augmented Generation，检索增强生成）的个人知识库问答系统，使用 Streamlit 构建，实现文档上传、向量检索和智能问答。

---

## 🚀 项目功能

- 📄 支持上传文档（txt / pdf / csv / md）
- 🔍 自动文本解析与切片（chunking）
- 🧠 基于向量的语义检索（RAG）
- 💬 Chat 对话式问答系统
- 🗂️ 文件管理（上传 / 删除 / 查看）
- 💾 文件元数据持久化存储
- ⚡ Streamlit 可视化交互界面

---

## 🏗️ 项目结构

front/
 ├── views/
 │    ├── chat.py        # 聊天问答页面
 │    └── lib.py         # 文件管理页面
 │
back/
 ├── services/
 │    ├── upload_service.py   # 文档解析 + 切片 + embedding
 │    ├── files_service.py    # 文件管理逻辑
 │    └── ...
 │
data/
 └── files.csv              # 文件记录存储

streamlit_app.py           # 项目入口

---

## ⚙️ 技术栈

- Python 3.10+
- Streamlit
- Pandas / NumPy
- PyPDF
- 向量数据库（Chroma / 内存向量）
- 大模型 API（DashScope / OpenAI 兼容）
- Text Splitter 文本切分

---

## 📦 安装依赖

pip install -r requirements.txt

---

## ▶️ 启动项目

streamlit run streamlit_app.py

---

## 📥 环境变量配置

在项目根目录创建 .env 文件：

DASHSCOPE_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key

---

## 📊 工作流程

用户上传文档
↓
文本解析
↓
切分 chunk
↓
生成 embedding
↓
存入向量数据库
↓
用户提问
↓
语义检索相关内容
↓
大模型生成回答

---

## 🧠 RAG 原理

User Question
↓
Vector Search（向量检索）
↓
Relevant Context（相关文本）
↓
Prompt 构建
↓
LLM 生成回答

---

## 📌 注意事项

本项目用于学习和 Demo 展示
部分部署平台（如 Hugging Face Spaces）对文件上传机制有限制
生产环境建议使用外部存储（S3 / Supabase / 向量数据库服务）

---

## 🚀 后续优化方向

- 多用户支持
- 聊天记录持久化
- 流式输出（Streaming）
- 云端向量数据库
- 登录鉴权系统
- Docker 部署支持

---

## 👨‍💻 作者

Arthas L

RAG 学习与实践项目

---

## 📜 License

MIT License
 
