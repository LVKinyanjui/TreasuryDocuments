import os
import pandas as pd
import streamlit as st
from supabase import create_client, Client

st.title("Treasury Documents")

@st.cache_resource
def init() -> Client:
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    return create_client(url, key)

supabase = init()

@st.cache_data
def query_all() -> dict:
    return dict(supabase.table("t-publications").select("*").execute())

response = query_all()
data = pd.DataFrame(response["data"])

data.sort_values(by="title", inplace=True)
data.drop(columns="id", inplace=True)

data
