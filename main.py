import streamlit as st


st.set_page_config(page_title="Clicker", page_icon="🖱️", layout="centered")



if "counter" not in st.session_state:
    st.session_state.counter = 0
    
if "reset_confirm" not in st.session_state:
    st.session_state.reset_confirm = False

if "keypad_input" not in st.session_state:
    st.session_state.keypad_input = 0  # Initialize as an integer
    
def hacks():
    st.session_state.counter += 9999
    
def dev_hacks():
    st.session_state.counter = 15778800000
def reset():
    st.session_state.counter = 0
    st.session_state.reset_confirm = False
    
def reset_no():
    st.session_state.reset_confirm = False
    
def plus1():
    st.session_state.counter += 1
    
st.title(f"{st.session_state.counter}")

st.button("                              +1                              ", on_click=plus1)
    
if st.button("Reset"):
    st.session_state.reset_confirm = True

if st.session_state.reset_confirm:
    st.write("Are you sure?")
    st.button("Yes", on_click=reset)
    st.button("No", on_click=reset_no)


st.subheader("Achievements:")


# Achievement levels
achievements = [50, 100, 300, 350, 400, 450, 500, 1000, 10000, 15778800000]

# Create containers for each achievement and the special message at 10,000
achievement_containers = [st.empty() for _ in achievements]
special_10000_container = st.empty()  # Container for the special 10,000 message

# Variable for tracking "keepGoing" status at 10,000
keepGoing = None

# Display achievements and handle the final achievement logic
for i, achievement in enumerate(achievements):
    # Display achievement if reached
    if st.session_state.counter >= achievement:
        # Only display achievements that are not the final one
        if achievement < 15778800000:
            achievement_containers[i].write(f"Achievement Made: {achievement}")

            # Special message and options at 10,000 clicks
            if achievement == 10000:
                with special_10000_container:
                    keepGoing = st.selectbox("GEEZ YOU'VE BEEN GOING FOREVER! WILL YOU EVER STOP?", ["Choose an option", "Yes", "NO!"])

        # Handle the final achievement
        elif achievement == 15778800000:
            # Clear all previous achievements including the special 10,000 message
            for container in achievement_containers[:-1]:  # All but the last achievement container
                container.empty()
            special_10000_container.empty()  # Clear the special 10,000 message

            # Show final achievement options
            st.write("If you are seeing this you shouldn't be, but if you are for some reason, you get access to hacks.")
            st.button("Hacks", on_click=lambda: hacks())
            st.write("If you click this button you will add 9,999 to the counter.")

            # Nested option if they choose "Yes" for "keepGoing"
            if keepGoing == "Yes":
                when = st.selectbox("WHEN?", ["Choose an option", "30+ Min", "2 hours", "1 week", "3 months", "4 years", "10 decades", "1 century"])
                if when == "10 decades" or when == "1 century":
                    st.write("We are gonna be here a while then. Approximately 15,778,800,000 clicks. Did you also realize that 10 decades and 1 century are the same thing?")
