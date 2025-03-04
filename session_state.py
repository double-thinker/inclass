import streamlit as st

st.title("Counter App")

# Initialize session state for counter if it doesn't exist
if "count" not in st.session_state:
    st.session_state.count = 0


# Create a row of buttons
col1, col2 = st.columns(2)

# Increment button
if col1.button("Increment"):
    st.session_state.count += 1
    # This will trigger a rerun with the new count value

# Reset button
if col2.button("Reset"):
    st.session_state.count = 0
    # This will trigger a rerun with the count reset


# Display the current count
st.header(f"Count: {st.session_state.count}")

# Conditional message
if st.session_state.count > 10:
    st.success("You've reached more than 10!")
