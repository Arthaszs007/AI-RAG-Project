from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder


def get_prompt():
    prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """你是一个专业的AI知识库助手。

                    请严格根据提供的参考资料回答问题。

                    参考资料:{context}

                    规则：
                    1. 优先使用参考资料中的内容回答
                    2. 如果参考资料中没有明确答案，请直接回答：
                    “资料中没有相关信息”
                    3. 不要使用你自己的知识进行补充或猜测
                    4. 回答保持专业、清晰、简洁
                    5. 优先总结重点，不要大段重复原文
                    6. 使用中文回答
                    
                    """,
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
        ]
    )

    return prompt_template
