
import streamlit as st

st.set_page_config(
    page_title="My Study Planner",
    page_icon="📚"
)

st.title("📚 My Study Planner")
st.write("Plan your studies and homework!")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.header("Add a Study Task")

subject = st.selectbox(
    "Choose a subject",
    ["Mathematics", "Science", "English",
     "Social Science", "Hindi", "Computer"]
)

task = st.text_input("Enter your study task")

time = st.selectbox(
    "Study time",
    ["4:00 PM", "5:00 PM", "6:00 PM",
     "7:00 PM", "8:00 PM"]
)

hours = st.slider("Study hours", 1, 3, 1)

if st.button("Add Task"):
    if task.strip():
        st.session_state.tasks.append({
            "Subject": subject,
            "Task": task,
            "Time": time,
            "Hours": hours
        })
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")

st.header("🗓️ My Timetable")

total_hours = sum(
    item["Hours"] for item in st.session_state.tasks
)

st.metric("Total Study Hours", total_hours)

for item in st.session_state.tasks:
    st.subheader(item["Subject"])
    st.write("Task:", item["Task"])
    st.write("Time:", item["Time"])
    st.write("Duration:", item["Hours"], "hour(s)")
    st.divider()
