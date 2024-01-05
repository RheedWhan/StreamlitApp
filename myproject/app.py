import streamlit as st

def main():
    st.title("Google Form Creator")

    # Get user input
    user_name = st.text_input("Enter your name:")
    user_email = st.text_input("Enter your email:")

    # Display the entered information
    st.write("Entered Information:")
    st.write(f"Name: {user_name}")
    st.write(f"Email: {user_email}")

    # You can add more input fields as needed

    # You can use the entered information to populate a Google Form or perform other actions
    # Here, we're just displaying a message
    st.success("Thank you for providing your information!")

if __name__ == "__main__":
    main()
