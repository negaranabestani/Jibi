import streamlit as st
import requests
import json
import pandas as pd

FASTAPI_BASE_URL = "http://localhost:8000/jibi"

def get_records(x_token):
    url = f"{FASTAPI_BASE_URL}/record/"
    headers = {"x-token": x_token}
    response = requests.get(url, headers=headers)
    return response.json()

def add_record(record, x_token):
    url = f"{FASTAPI_BASE_URL}/record/"
    headers = {"x-token": x_token, "Content-Type": "application/json"}
    print(headers)
    print(record)
    response = requests.post(url, json=record, headers=headers)
    print(response)
    return response.json(), response.status_code

def edit_record(record, x_token):
    url = f"{FASTAPI_BASE_URL}/record/"
    headers = {"x-token": x_token, "Content-Type": "application/json"}
    response = requests.put(url, json=record, headers=headers)
    return response.json(), response.status_code

def delete_record(record_id, x_token):
    url = f"{FASTAPI_BASE_URL}/record/{record_id}"
    headers = {"x-token": x_token}
    response = requests.delete(url, headers=headers, params={"record_id": record_id})
    return response.json(), response.status_code

def main():
    st.title("Record Management")
    print('***********************************')
    x_token = st.session_state.user_token  # Assuming you have stored the token in session_state
    print(x_token)
    print('********************************')

    if not x_token:
        st.warning("Please sign in first.")
        return

    selected_action = st.selectbox("Select Action", ["View Records", "Add Record", "Edit Record", "Delete Record"])

    if selected_action == "View Records":
        st.header("Records")
        records = get_records(x_token).get('record', {})
        if len(records):
            st.table(pd.DataFrame(records).set_index('id')[['title', 'category', 'amount', 'date', 'type']])
        else:
            st.warning("No records found.")

    elif selected_action == "Add Record":
        st.header("Add Record")
        title = st.text_input("Title")
        amount = st.number_input("Amount", min_value=0.0)
        category = st.number_input("Category ID", min_value=1, step=1)
        record_type = st.selectbox("Type", ["Income", "Expense"])

        if st.button("Add Record"):
            new_record = {
                "record": {
                    "amount": amount,
                    "category": category,
                    "title": title,
                    "type": record_type
                },
                "record_id": 1,
                "requestID": "NULL"
            }

            response, status_code = add_record(new_record, x_token)
            if status_code == 200:
                st.success(f"Record added successfully!")
            else:
                st.warning(response.get('message', ' '))

    elif selected_action == "Edit Record":
        st.header("Edit Record")
        record_id = st.number_input("Record ID to Edit", min_value=1, step=1)
        title = st.text_input("Title")
        amount = st.number_input("Amount", min_value=0.0)
        category = st.number_input("Category", min_value=1, step=1)
        record_type = st.selectbox("Type", ["Income", "Expense"])

        if st.button("Edit Record"):
            edited_record = {
                "record": {
                    "amount": amount,
                    "category": category,
                    "title": title,
                    "type": record_type
                },
                "record_id": record_id,
                "requestID": "NULL"
            }

            response, status_code = edit_record(edited_record, x_token)
            print(response)
            if status_code == 200:
                st.success(f"Record edited successfully!")
            else:
                st.warning(response.get('message', ' '))
    elif selected_action == "Delete Record":
        st.header("Delete Record")
        record_id = st.number_input("Record ID to Delete", min_value=1, step=1)

        if st.button("Delete Record"):
            response, status_code = delete_record(record_id, x_token)
            print(response)
            if status_code == 200:
                st.success(f"Record deleted successfully!")
            else:
                st.warning(response.get('message', ' '))

main()
