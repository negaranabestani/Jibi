import streamlit as st
import requests
import pandas as pd

FASTAPI_BASE_URL = "http://localhost:8000/jibi"

def get_categories(x_token):
    url = f"{FASTAPI_BASE_URL}/category/"
    headers = {"x-token": x_token}
    response = requests.get(url, headers=headers)
    return response.json()

def add_category(category, x_token):
    url = f"{FASTAPI_BASE_URL}/category/"
    headers = {"x-token": x_token, "Content-Type": "application/json"}
    response = requests.post(url, json=category, headers=headers)
    return response.json(), response.status_code

def edit_category(category, x_token):
    url = f"{FASTAPI_BASE_URL}/category/"
    headers = {"x-token": x_token, "Content-Type": "application/json"}
    response = requests.put(url, json=category, headers=headers)
    return response.json(), response.status_code

def delete_category(category_id, x_token):
    url = f"{FASTAPI_BASE_URL}/category/{category_id}"
    headers = {"x-token": x_token}
    response = requests.delete(url, headers=headers, params={'id': category_id})
    return response.json(), response.status_code

def main():
    st.title("Category Management")
    x_token = st.session_state.user_token  # Assuming you have stored the token in session_state

    if not x_token:
        st.warning("Please sign in first.")
        return

    selected_action = st.selectbox("Select Action", ["View Categories", "Add Category", "Edit Category", "Delete Category"])

    if selected_action == "View Categories":
        st.header("Categories")
        categories = get_categories(x_token)
        print(categories)
        if len(categories):
            st.table(pd.DataFrame(categories).set_index('id')[['title', 'color', 'icon']])
        else:
            st.warning("No categories found.")


# color: str
#     icon: str
#     title: str
#     user_id: str
#     id: int

# if len(records):
#             st.table(pd.DataFrame(records).set_index('id')[['title', 'category', 'amount', 'date']])
#         else:
#             st.warning("No records found.")

    elif selected_action == "Add Category":
        st.header("Add Category")
        #olor = st.text_input("Color")
        title = st.text_input("Title")
        icon = st.text_input("Icon")
        color = st.color_picker("Color", value='#FB0202')

        if st.button("Add Category"):
            new_category = {
                "category": {
                    "color": color,
                    "icon": icon,
                    "title": title,
                    "id": 0
                },
                "requestID": "NULL"
            }

            response, status_code = add_category(new_category, x_token)
            if status_code == 200:
                st.success(f"Category added successfully!")
            else:
                st.warning(response.get('message', ' '))
            

    elif selected_action == "Edit Category":
        st.header("Edit Category")
        category_id = st.number_input("Category ID to Edit", min_value=1, step=1)
        title = st.text_input("Title")
        icon = st.text_input("Icon")
        color = st.color_picker("Color", value='#FB0202')

        if st.button("Edit Category"):
            edited_category = {
                "category": {
                    "color": color,
                    "icon": icon,
                    "title": title,
                    "id": category_id
                },
                "requestID": "NULL"
            }

            response, status_code = edit_category(edited_category, x_token)
            if status_code == 200:
                st.success(f"Record edited successfully!")
            else:
                st.warning(response.get('message', ' '))

    elif selected_action == "Delete Category":
        st.header("Delete Category")
        category_id = st.number_input("Category ID to Delete", min_value=1, step=1)

        if st.button("Delete Category"):
            response, status_code = delete_category(category_id, x_token)
            if status_code == 200:
                st.success(f"Record deleted successfully!")
            else:
                st.warning(response.get('message', ' '))

main()
