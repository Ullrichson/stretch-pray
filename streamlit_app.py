import streamlit as st
import time

st.set_page_config(page_title="Stretch & Pray", page_icon="🙏")

st.title("🙏 Stretch & Pray")
st.write("Bewegung und Gebet in Einklang bringen – eine kleine 5-Minuten-Routine.")

# Beispielroutine
routine = [
    {
        "exercise": "Nacken- und Schulterdehnung (rechts)",
        "duration": 30,
        "prayer": "Herr, ich lege dir die Lasten meines Tages hin. Schenke mir Ruhe, schenke mir Frieden."
    },
    {
        "exercise": "Nacken- und Schulterdehnung (links)",
        "duration": 30,
        "prayer": "Jesus, öffne mein Herz für deine Liebe. Wie ich Raum im Körper spüre, so schaffe Raum in mir für dich."
    },
    {
        "exercise": "Seitliche Dehnung",
        "duration": 30,
        "prayer": "Heiliger Geist, breite dich aus in mir. Fülle mich mit deiner Stärke, mit deiner Leichtigkeit."
    },
    {
        "exercise": "Vorbeuge",
        "duration": 30,
        "prayer": "Herr, ich beuge mich vor dir. Richte du mich auf. In deiner Nähe finde ich Halt."
    },
    {
        "exercise": "Abschluss – Hände zum Gebet",
        "duration": 30,
        "prayer": "Danke, Vater im Himmel, für diesen Moment der Ruhe. Segne meinen Körper, meine Gedanken, meinen Geist. Amen."
    }
]

# State speichern
if "step" not in st.session_state:
    st.session_state.step = 0

current = routine[st.session_state.step]

st.subheader(f"Übung {st.session_state.step+1} von {len(routine)}")
st.markdown(f"### ✨ {current['exercise']}")
st.write(current["prayer"])
st.progress(0)

# Timer-Button
if st.button("▶️ Starte diese Übung"):
    progress_bar = st.progress(0)
    for sec in range(current["duration"]):
        time.sleep(1)
        progress_bar.progress((sec+1)/current["duration"])
    st.success("✅ Übung beendet!")

    if st.session_state.step < len(routine)-1:
        st.session_state.step += 1
        st.experimental_rerun()
    else:
        st.balloons()
        st.success("🎉 Routine abgeschlossen!")
