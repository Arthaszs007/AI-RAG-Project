import streamlit as st
import pandas as pd
from front.config import FILES_HEADER
from back.services.files_service import read_csv, delete_by_id, write_csv
from back.services.upload_service import upload_file

# data area
files_info = read_csv()
df = pd.DataFrame(files_info, columns=FILES_HEADER)

files_table = f"data_table_version_{len(df)}"
files_uploader = f"data_uploader_version_{len(df)}"

if "embedding" not in st.session_state:
    st.session_state["embedding"] = False

if "run_embedding" not in st.session_state:
    st.session_state["run_embedding"] = False

# components area
col1, col2 = st.columns([8, 1])
col1.write(f"files amount: {len(df)}")

delete_btn = col2.button("delete", type="primary")


event = st.dataframe(
    df, key=files_table, on_select="rerun", selection_mode=["multi-row"], height=600
)

uploader = st.file_uploader(
    "upload", label_visibility="hidden", accept_multiple_files=True, key=files_uploader
)

submit_btn = st.button("Submit", type="primary")


@st.dialog("Processing")
def embedding_modal():

    st.write("⏳ Embedding in progress... 向量化入库中,请耐心等待3~10分钟...")
    with st.spinner("Please wait..."):
        pass


# logic area
if delete_btn:
    rows = event.selection.get("rows", [])

    if not rows:
        st.toast("Select rows to remove", icon="⚠️")
        st.stop()

    valid_rows = [r for r in rows if r < len(df)]

    if valid_rows:
        ids = df.iloc[valid_rows]["id"].tolist()
        for id_ in ids:
            delete_by_id(id_)

    st.rerun()


if submit_btn:

    if not uploader:
        st.toast("No files upload", icon="⚠️")
        st.stop()

    # 打开弹窗状态
    st.session_state["embedding"] = True
    st.session_state["run_embedding"] = True

if st.session_state["embedding"]:
    embedding_modal()

    # 执行你的 embedding
    for file in uploader:
        write_csv(name=file.name, size=file.size)

    upload_file(uploader)

    st.session_state["embedding"] = False
    st.session_state["run_embedding"] = False
    st.rerun()
