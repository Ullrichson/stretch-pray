
import streamlit as st
import time
import base64

st.set_page_config(page_title="Stretch & Pray", page_icon="🙏")

st.title("🙏 Stretch & Pray")
st.write("Bewegung und Gebet in Einklang bringen – eine kleine 5-Minuten-Routine.")

# --- Hilfsfunktion für Sounds ---
def play_sound(file_path: str, placeholder: st.delta_generator.DeltaGenerator):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    unique_id = str(time.time()).replace(".", "")  # jede Wiedergabe mit neuer ID
    md = f"""
    <audio id="audio-{unique_id}" autoplay>
      <source src="data:audio/wav;base64,{b64}" type="audio/mp3">
    </audio>
    """
    placeholder.markdown(md, unsafe_allow_html=True)

# --- Routine ---
routine = [
    {
        "exercise": "Nacken- und Schulterdehnung (rechts)",
        "duration": 10,
        "prayer": "Herr, ich lege dir die Lasten meines Tages hin. Schenke mir Ruhe, schenke mir Frieden."
    },
    {
        "exercise": "Nacken- und Schulterdehnung (links)",
        "duration": 10,
        "prayer": "Jesus, öffne mein Herz für deine Liebe. Wie ich Raum im Körper spüre, so schaffe Raum in mir für dich."
    },
    {
        "exercise": "Seitliche Dehnung",
        "duration": 10,
        "prayer": "Heiliger Geist, breite dich aus in mir. Fülle mich mit deiner Stärke, mit deiner Leichtigkeit."
    },
    {
        "exercise": "Vorbeuge",
        "duration": 10,
        "prayer": "Herr, ich beuge mich vor dir. Richte du mich auf. In deiner Nähe finde ich Halt."
    },
    {
        "exercise": "Abschluss – Hände zum Gebet",
        "duration": 10,
        "prayer": "Danke, Vater im Himmel, für diesen Moment der Ruhe. Segne meinen Körper, meine Gedanken, meinen Geist. Amen."
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
    play_sound("sounds/start.wav", sound_placeholder)

    # Fortschritt & Tick-Sounds
    for sec in range(current["duration"]):
        time.sleep(1)
        progress_bar.progress((sec+1)/current["duration"])

        if sec == current["duration"] - 2:  # 2 Sekunden vor Ende
            play_sound("sounds/tick.wav", sound_placeholder)

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
