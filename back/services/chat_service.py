import json
import os
from datetime import datetime

# ── 配置 ──────────────────────────────────────────────────────────────────────
DATA_DIR = "./data"  # 用户会话 JSON 存放根目录


# ══════════════════════════════════════════════════════════════════════════════
# 内部工具
# ══════════════════════════════════════════════════════════════════════════════


def _user_path(user_id: str) -> str:
    """返回该用户 JSON 文件的完整路径"""
    return os.path.join(DATA_DIR, str(user_id), "session.json")


def _ensure_dir(user_id: str) -> None:
    """确保用户目录存在"""
    user_dir = os.path.join(DATA_DIR, str(user_id))
    os.makedirs(user_dir, exist_ok=True)


def generate_timestamp() -> str:
    """生成当前时间戳，格式：YYYY-MM-DD HH:MM:SS"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ══════════════════════════════════════════════════════════════════════════════
# 函数 1 · 添加聊天消息
# ══════════════════════════════════════════════════════════════════════════════


def add_message(user_id: str, role: str, content: str) -> dict:
    """
    向指定用户的会话文件追加一条消息。
    - 用户目录/文件不存在时自动创建。
    - 用户目录/文件已存在时直接追加。

    Args:
        user_id : 用户唯一标识（作为子目录名）
        role    : 消息角色，如 "user" / "assistant" / "system"
        content : 消息正文

    Returns:
        本次写入的消息字典
    """
    path = _user_path(user_id)
    _ensure_dir(user_id)

    # 读取已有数据，文件不存在则初始化空列表
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                messages: list = json.load(f)
            except json.JSONDecodeError:
                messages = []
    else:
        messages = []

    # 构建新消息
    new_message = {
        "role": role,
        "time": generate_timestamp(),
        "content": content,
    }

    messages.append(new_message)

    # 回写
    with open(path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

    return new_message


# ══════════════════════════════════════════════════════════════════════════════
# 函数 2 · 读取聊天记录
# ══════════════════════════════════════════════════════════════════════════════


def read_messages(user_id: str) -> list[dict]:
    """
    读取指定用户的全部聊天记录。

    Args:
        user_id : 用户唯一标识

    Returns:
        消息列表，每项包含 role / time / content；
        文件不存在时返回空列表。

    Example:
        [
          {"role": "user",      "time": "2026-05-16 10:00:00", "content": "你好"},
          {"role": "assistant", "time": "2026-05-16 10:00:01", "content": "你好！有什么可以帮你？"},
        ]
    """
    path = _user_path(user_id)

    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        try:
            messages: list = json.load(f)
        except json.JSONDecodeError:
            return []

    # 只返回三个标准字段，过滤掉可能存在的多余字段
    return [
        {
            "role": msg.get("role", ""),
            "time": msg.get("time", ""),
            "content": msg.get("content", ""),
        }
        for msg in messages
    ]


# ══════════════════════════════════════════════════════════════════════════════
# 函数 3 · 清除聊天记录
# ══════════════════════════════════════════════════════════════════════════════


def clear_messages(user_id: str) -> bool:
    """
    清除指定用户的全部聊天记录（将 JSON 内容重置为空列表）。
    不删除文件本身，保留目录结构。

    Args:
        user_id : 用户唯一标识

    Returns:
        True  → 清除成功
        False → 用户文件不存在，无需操作
    """
    path = _user_path(user_id)

    if not os.path.exists(path):
        return False

    with open(path, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)

    return True
