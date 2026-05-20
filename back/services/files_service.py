import pandas as pd
import os
from back.utils.helper import generate_timestamp, generate_uuid
from back.config import FILES_HEADER

# ── 配置 ──────────────────────────────────────────────────────────────────────
CSV_DIR = "./data"  # CSV 存放目录，可按需修改
CSV_NAME = "fake_files_date.csv"
CSV_PATH = os.path.join(CSV_DIR, CSV_NAME)
HEADERS = FILES_HEADER


# ══════════════════════════════════════════════════════════════════════════════
# 函数 1 · 读取 CSV，返回 DataFrame（供 Streamlit st.dataframe 使用）
# ══════════════════════════════════════════════════════════════════════════════


def read_csv(path: str = CSV_PATH) -> pd.DataFrame:
    """
    读取指定路径的 CSV 文件，返回 DataFrame。
    若文件不存在则返回空 DataFrame（含标准表头）。

    Args:
        path: CSV 文件路径，默认使用模块级 CSV_PATH

    Returns:
        pd.DataFrame，可直接传给 st.dataframe()
    """
    if not os.path.exists(path):
        return pd.DataFrame(columns=HEADERS)

    df = pd.read_csv(path, dtype=str)

    # 补齐缺失列，保证结构一致
    for col in HEADERS:
        if col not in df.columns:
            df[col] = ""

    return df[HEADERS]


# ══════════════════════════════════════════════════════════════════════════════
# 函数 2 · 写入 / 追加一条记录到 001.csv
# ══════════════════════════════════════════════════════════════════════════════


def write_csv(
    name: str, size: str, status: str = "active", path: str = CSV_PATH
) -> dict:
    """
    检查 001.csv 是否存在：
      - 不存在 → 创建文件并写入表头，再写入新行
      - 存在   → 直接追加新行

    Args:
        name:   文件名（或任意名称字段）
        size:   文件大小（字符串，如 "1.2 MB"）
        status: 状态，默认 "active"
        path:   CSV 路径，默认使用模块级 CSV_PATH

    Returns:
        新写入行的字典
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    new_row = {
        "id": generate_uuid(),
        "name": name,
        "size": size,
        "update": generate_timestamp(),
        "status": status,
    }

    file_exists = os.path.exists(path)

    if file_exists:
        # 追加模式：不写表头
        pd.DataFrame([new_row]).to_csv(path, mode="a", header=False, index=False)
    else:
        # 创建模式：写表头 + 数据
        pd.DataFrame([new_row], columns=HEADERS).to_csv(
            path, mode="w", header=True, index=False
        )

    return new_row


# ══════════════════════════════════════════════════════════════════════════════
# 函数 3 · 根据 id 删除指定行
# ══════════════════════════════════════════════════════════════════════════════


def delete_by_id(file_id: str, path: str = CSV_PATH) -> bool:
    """
    根据 id 删除 CSV 中对应的行，并将结果回写文件。

    Args:
        file_id: 要删除的行 id
        path:   CSV 路径，默认使用模块级 CSV_PATH

    Returns:
        True  → 找到并删除成功
        False → 文件不存在或未找到对应 id
    """
    if not os.path.exists(path):
        return False

    df = pd.read_csv(path, dtype=str)

    mask = df["id"] == str(file_id)
    if not mask.any():
        return False

    df = df[~mask].reset_index(drop=True)
    df.to_csv(path, index=False)
    return True
