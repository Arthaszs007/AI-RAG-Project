# md5
MD5_PATH = "./back/data/md5.text"

# chroma
COLLECTION_NAME = "rag"
PERSIST_DIRECTORY = "./back/data/chroma_db"
SIMILAR_SEARCH_KWG = 2

# spliter
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
SEPARATOR = ["\n\n", "\n", ",", ".", "?", "|", "!", " ", ". ", ""]
MAX_CHAT_CHAR_NUM = 1000


# model
CHAT_MODEL_NAME = "qwen3-max"
EMBEDDING_MODEL_NAME = "text-embedding-v4"


# docs data
FILES_HEADER = ["id", "name", "size", "update", "status"]
