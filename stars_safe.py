
import streamlit as st
import datetime
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Star's Safe", layout="wide")

# --- STYLE ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Orbitron:wght@700&display=swap');

    body, .main {
        background-color: #121212;
        color: #DDD;
        font-family: 'Montserrat', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        color: #A4DFFF;
        font-weight: 700;
        letter-spacing: 1.5px;
    }
    button {
        background-color: #A4DFFF !important;
        color: #121212 !important;
        border-radius: 5px !important;
        font-weight: 700 !important;
        border: none !important;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    button:hover {
        background-color: #6EB8FF !important;
    }
    input, textarea {
        background-color: #222 !important;
        color: #DDD !important;
        border: 2px solid #A4DFFF !important;
        border-radius: 6px !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: 500;
    }
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(135deg, #0D0D0D 0%, #1A1A1A 100%);
        border-right: 2px solid #A4DFFF;
    }
    /* Sharp shapes */
    .sharp-shape {
        position: fixed;
        width: 100px;
        height: 100px;
        background: #6EB8FF;
        clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
        opacity: 0.15;
        z-index: 0;
        animation: pulse 3s ease-in-out infinite;
    }
    .sharp-top-left {
        top: 0;
        left: 0;
    }
    .sharp-bottom-right {
        bottom: 0;
        right: 0;
    }
    @keyframes pulse {
        0% {opacity: 0.15;}
        50% {opacity: 0.3;}
        100% {opacity: 0.15;}
    }
    .quote {
        font-style: italic;
        margin: 1em 0;
        color: #6EB8FF;
        font-size: 1.2em;
        border-left: 4px solid #A4DFFF;
        padding-left: 10px;
    }
    .img-gallery img {
        border-radius: 10px;
        border: 2px solid #A4DFFF;
        margin: 10px;
        max-width: 200px;
        transition: transform 0.3s ease;
        cursor: pointer;
    }
    .img-gallery img:hover {
        transform: scale(1.1);
        border-color: #6EB8FF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="sharp-shape sharp-top-left"></div>', unsafe_allow_html=True)
st.markdown('<div class="sharp-shape sharp-bottom-right"></div>', unsafe_allow_html=True)

# --- SESSION STATE SETUP ---
if "todos" not in st.session_state:
    st.session_state.todos = []
if "rituals_done" not in st.session_state:
    st.session_state.rituals_done = {}

# --- FUNCTIONS ---
def add_item(list_name, item):
    if item and item.strip():
        st.session_state[list_name].append(item.strip())
        st.success(f"Added to {list_name}!")

# --- RITUALS ---
rituals = {
    "Love": [
        "Light a soft pink or red candle.",
        "Say: “I open my heart to love and positive energy.”",
        "Visualize the love you want as bright light surrounding you.",
        "Write down one thing you love about yourself every day.",
        "Listen to a song that makes you feel loved and powerful."
    ],
    "Fame": [
        "Light a white or gold candle.",
        "Say: “I attract success and shine bright on every stage.”",
        "Visualize yourself shining under bright lights.",
        "Write down one goal you want to achieve today.",
        "Play a song that makes you feel unstoppable."
    ],
    "Confidence": [
        "Stand in front of a mirror and say: “I am powerful and worthy.”",
        "Take three deep breaths and hold your head high.",
        "Write down three things you are proud of.",
        "Wear your favorite outfit that makes you feel fierce.",
        "Listen to a song that pumps you up."
    ],
}

# --- MAIN APP UI ---
st.title("Star's Safe ✨ Your Rockstar HQ & Rituals")

st.header("Daily To-Do List")
new_todo = st.text_input("Add a task to your list")
if st.button("Add Task"):
    if new_todo.strip():
        st.session_state.todos.append(new_todo.strip())
        st.success("Task added!")
if st.session_state.todos:
    for i, task in enumerate(st.session_state.todos):
        st.write(f"- {task}")

st.header("Rituals & Manifestations")
for ritual_name, steps in rituals.items():
    with st.expander(f"{ritual_name} Ritual"):
        done_key = f"ritual_{ritual_name.lower()}_done"
        done = st.checkbox("Mark as done today", key=done_key)
        for step in steps:
            st.write(f"• {step}")

st.header("Inspirational Quotes")
quotes = [
    "“Don’t wait for opportunity. Create it.” – Alejandra Villarreal",
    "“The stage is where I feel alive.” – Alejandra Villarreal",
    "“Music is the weapon.” – Fela Kuti",
    "“Rock ‘n’ roll is about freedom.” – Joan Jett",
    "“You were born to shine.” – Unknown",
    "“Turn your wounds into wisdom.” – Oprah Winfrey",
    "“Without music, life would be a mistake.” – Friedrich Nietzsche",
    "“Let the music heal your soul.” – Unknown"
]
st.info(random.choice(quotes))

st.header("Songwriting Ideas")
ideas = [
    "Write about a moment when the world feels heavy but you refuse to break.",
    "Describe the feeling of riding your motorcycle at night, wind in your hair.",
    "A song about transformation — from doubt to power.",
    "Paint a picture of a secret place where only music speaks.",
    "Channel Alejandra’s fierce confidence — write a 'battle anthem.'",
    "Write about chasing dreams when everyone doubts you.",
    "Describe a night out with your band, wild and free.",
    "Write lyrics inspired by the stars and the moonlight.",
]
st.write(random.choice(ideas))
