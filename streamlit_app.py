
import streamlit as st
import time
import base64

st.set_page_config(page_title="Stretch & Pray", page_icon="🙏")

st.title("🙏 Stretch & Pray")
st.write("Bewegung und Gebet in Einklang bringen – eine kleine 5-Minuten-Routine.")

# --- Hilfsfunktion für Sounds ---
def play_sound(file_path: str, placeholder: st.delta_generator.DeltaGenerator):
    time.sleep(1)
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    unique_id = str(time.time()).replace(".", "")  # jede Wiedergabe mit neuer ID
    md = f"""
    <audio id="audio-{unique_id}" autoplay>
      <source src="data:audio/wav;base64,{b64}" type="audio/wav">
    </audio>
    """
    placeholder.markdown(md, unsafe_allow_html=True)

routine = [
    {
        "exercise": "🧘‍♀️ Child's Pose",
        "duration": 30,
        "prayer": "Ich lasse mich nieder und spüre Ruhe. In Gottes Gegenwart erkenne ich, was still und beständig ist."
    },
    {
        "exercise": "🐱🐮 Cat-Cow",
        "duration": 30,
        "prayer": "Ich bewege meinen Körper bewusst. Jesu Gegenwart lehrt mich, im Wechsel von Spannung und Entspannung zu leben."
    },
    {
        "exercise": "🐍 Cobra",
        "duration": 30,
        "prayer": "Ich richte mich auf, fühle Kraft und Wachheit. Der Heilige Geist ist ein stiller Begleiter, der mein inneres Gleichgewicht wahrt."
    },
    {
        "exercise": "🌏 World's Greatest Stretch (links)",
        "duration": 30,
        "prayer": "Ich strecke mich nach links und öffne mich. Gottes Weite zeigt mir, dass ich mehr tragen und halten kann, als ich dachte."
    },
    {
        "exercise": "🌏 World's Greatest Stretch (rechts)",
        "duration": 30,
        "prayer": "Ich strecke mich nach rechts. Jesu Gegenwart erinnert mich daran, offen und aufmerksam zu bleiben."
    },
    {
        "exercise": "🥞 Pancake Stretch",
        "duration": 30,
        "prayer": "Ich beuge mich tief, erde mich, weite mich zugleich. Der Heilige Geist gibt mir Stille, in der ich nachdenken kann."
    },
    {
        "exercise": "🏋️‍♂️ Deep Squat Hold",
        "duration": 30,
        "prayer": "Ich halte die Position, spüre Standfestigkeit. Gottes Gegenwart gibt mir Kraft, in mir selbst zu ruhen."
    },
    {
        "exercise": "🤲 Shoulder Stretch (links)",
        "duration": 30,
        "prayer": "Die linke Schulter öffnet sich. Jesu Licht erinnert mich daran, Lasten bewusst zu tragen."
    },
    {
        "exercise": "🤲 Shoulder Stretch (rechts)",
        "duration": 30,
        "prayer": "Die rechte Schulter dehnt sich. Der Heilige Geist gibt Klarheit und Stärke für das, was ich tun muss."
    },
    {
        "exercise": "💪 Triceps Stretch (links)",
        "duration": 30,
        "prayer": "Ich spüre Kraft im linken Arm. Gottes Weisheit leitet mein Tun, während ich die Verantwortung selbst trage."
    },
    {
        "exercise": "💪 Triceps Stretch (rechts)",
        "duration": 30,
        "prayer": "Der rechte Arm öffnet sich. Jesu Gegenwart erinnert mich an achtsames Handeln im Alltag."
    },
    {
        "exercise": "👣 Toe Reaches",
        "duration": 30,
        "prayer": "Ich strecke mich nach unten und finde Erdung. Der Heilige Geist lässt mich die Verbindung zu allem Leben spüren."
    },
    {
        "exercise": "🙏 Abschluss – Hände zum Gebet",
        "duration": 15,
        "prayer": "Ich verweile in Stille. Gottes Weisheit, Jesu Gegenwart und des Heiligen Geistes Licht begleiten meine Schritte."
    }
]


# --- States ---
if "started" not in st.session_state:
    st.session_state.started = False
if "step" not in st.session_state:
    st.session_state.step = 0

# --- Platzhalter ---
exercise_placeholder = st.empty()
progress_placeholder = st.empty()
sound_placeholder = st.empty()

# --- Startbutton ---
if st.button("▶️ Starte die Routine") and not st.session_state.started:
    st.session_state.started = True
    st.session_state.step = 0

# --- Ablauf ---
if st.session_state.started:
    current = routine[st.session_state.step]

    with exercise_placeholder.container():
        st.subheader(f"Übung {st.session_state.step+1} von {len(routine)}")
        st.markdown(f"### ✨ {current['exercise']}")
        st.write(current["prayer"])

    progress_bar = progress_placeholder.progress(0)

    # Start-Sound
    #play_sound("sounds/start.wav", sound_placeholder)

    if st.session_state.step == 0:
        play_sound("prayers/childs_pose.wav", sound_placeholder)
    elif st.session_state.step == 1:
        play_sound("prayers/catcow.wav", sound_placeholder)
    elif st.session_state.step == 2:
        play_sound("prayers/cobra.wav", sound_placeholder)
    elif st.session_state.step == 3:
        play_sound("prayers/worldsstretchleft.wav", sound_placeholder)
    elif st.session_state.step == 4:
        play_sound("prayers/worldsstretchright.wav", sound_placeholder)
    elif st.session_state.step == 5:
        play_sound("prayers/pancake.wav", sound_placeholder)
    elif st.session_state.step == 6:
        play_sound("prayers/deepsquat.wav", sound_placeholder)
    elif st.session_state.step == 7:
        play_sound("prayers/shoulderleft.wav", sound_placeholder)
    elif st.session_state.step == 8:
        play_sound("prayers/shoulderright.wav", sound_placeholder)
    elif st.session_state.step == 9:
        play_sound("prayers/tricepsleft.wav", sound_placeholder)
    elif st.session_state.step == 10:
        play_sound("prayers/tricepsright.wav", sound_placeholder)
    elif st.session_state.step == 11:
        play_sound("prayers/toe.wav", sound_placeholder)
    elif st.session_state.step == 12:
        play_sound("prayers/abschluss.wav", sound_placeholder)

    # Fortschritt & Tick-Sounds
    for sec in range(current["duration"]):
        time.sleep(1)
        progress_bar.progress((sec+1)/current["duration"])

    # Ende der Übung
    exercise_placeholder.success("✅ Übung beendet!")
    time.sleep(1)

    # Nächste Übung oder Ende
    if st.session_state.step < len(routine)-1:
        st.session_state.step += 1
        st.rerun()
    else:
        st.balloons()
        st.success("🎉 Routine abgeschlossen!")
        st.session_state.started = False
