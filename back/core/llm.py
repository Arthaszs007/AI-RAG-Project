from back.core.chroma import VectorBase
from back.core.prompt import get_prompt
from langchain_community.chat_models import ChatTongyi
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
import back.config
from langchain_core.documents import Document


class LLM:
    def __init__(self):
        self.vector_service = VectorBase()
        self.prompt_template = get_prompt()
        self.chat_model = ChatTongyi(model=back.config.CHAT_MODEL_NAME)
        self.chain = self._build_chain()

    def _build_chain(self):
        retriever = self.vector_service.get_retriever()

        def format_doc(docs: list[Document]):
            if not docs:
                return "没有找到相关参考资料"

            return "\n\n".join([f"""
            参考资料 {i+1}:
            来源: {doc.metadata.get("source", "unknown")}

            内容:
            {doc.page_content}
        """ for i, doc in enumerate(docs)])

        chain = (
            {
                "context": RunnableLambda(lambda x: x["input"])
                | retriever
                | format_doc,
                "input": RunnableLambda(lambda x: x["input"]),
                "chat_history": RunnableLambda(lambda x: x["chat_history"]),
            }
            | self.prompt_template
            | self.chat_model
            | StrOutputParser()
        )

        return chain
