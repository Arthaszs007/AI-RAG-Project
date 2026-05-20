import streamlit as st
from back.services.chat_service import read_messages, add_message
from back.core.llm import LLM
from langchain_core.messages import HumanMessage, AIMessage

# init
DEFAULT_USER_ID = "100011"

if "history" not in st.session_state:
    st.session_state["history"] = []

MAX_HISTORY = 20  # 10轮对话（Human+AI）

user_id = st.session_state.get("user_id", DEFAULT_USER_ID)
messages = read_messages(user_id)

llm = LLM()

# component area


# 渲染历史消息
for msg in messages:
    with st.chat_message(msg["role"]):
        st.caption(msg["time"])
        st.write(msg["content"])

prompt = st.chat_input("Say something")

# logic area
if prompt:
    # 用户消息
    with st.chat_message("user"):
        st.caption(add_message(user_id, "user", prompt)["time"])
        st.write(prompt)

    # 当前 prompt 还没加入，history 此时全是"之前的对话"，正好作为上下文传入
    history_for_chain = st.session_state["history"][-MAX_HISTORY:]
    # 👉 加入 memory
    st.session_state["history"].append(HumanMessage(content=prompt))

    # ✔ 新增：限制 history 长度（
    st.session_state["history"] = st.session_state["history"][-MAX_HISTORY:]

    # AI消息
    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        full_response = ""

        # 流式输出
        for chunk in llm.chain.stream(
            {"input": prompt, "chat_history": history_for_chain}
        ):

            full_response += chunk

            message_placeholder.markdown(full_response)

    # 保存最终结果
    add_message(user_id, "assistant", full_response)

    # 👉 加入 memory
    st.session_state["history"].append(AIMessage(content=full_response))

    # ✔ 新增：限制 history 长度（关键修改点）
    st.session_state["history"] = st.session_state["history"][-MAX_HISTORY:]
