# ══════════════════════════════════════════════════════════════════════════════
# 工具函数
# ══════════════════════════════════════════════════════════════════════════════
import uuid
from datetime import datetime


def generate_uuid() -> str:
    """生成一个不含连字符的大写 UUID（8位短码）"""
    return str(uuid.uuid4()).replace("-", "")[:8].upper()


def generate_timestamp() -> str:
    """生成当前时间戳字符串，格式：YYYY-MM-DD HH:MM:SS"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
