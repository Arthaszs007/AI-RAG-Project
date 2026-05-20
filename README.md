# 📚 RAG 知识库问答系统

一个基于 RAG（Retrieval-Augmented Generation，检索增强生成）的个人知识库问答系统，使用 Streamlit 构建，实现文档上传、向量检索和智能问答。
只做了RAG核心功能，数据暂时存储于本地

---

## 🚀 项目功能

- 📄 支持上传文档（txt / pdf / csv / md）
- 🔍 自动文本解析与切片（chunking）
- 🧠 基于向量的语义检索（RAG）
- 💬 Chat 流式对话问答系统
- 🗂️ 文件管理（上传 / 删除 / 查看）
- 💾 文件元数据持久化存储
- ⚡ Streamlit 可视化交互界面

---

## ⚙️ 技术栈

- Python 3.10+
- Streamlit
- 向量数据库（Chroma）
- 大模型 API（llm），基于自定义 Chain 结构将 Chat History、用户问题与向量检索结果进行动态拼接，并进行 Prompt 优化设计，以提升 RAG 上下文利用率与回答准确性
- Text Splitter 文本切分

---

## 📦 安装依赖

pip install -r requirements.txt

---

## ▶️ 启动项目

streamlit run app.py

---

## 📥 环境变量配置

在项目根目录创建 .env 文件：

DASHSCOPE_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key

note：目前仅支持tongyi的key
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

---


## 👨‍💻 作者

Arthas L

---

 
