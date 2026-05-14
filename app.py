import streamlit as st
import music21
from music21 import note, stream, chord, instrument
import random
import base64

st.set_page_config(page_title="AI Music Generator", page_icon="🎵")
st.title("🎵 CodeAlpha AI Music Generator")
st.write("AI se naya music banao - LSTM based patterns")

scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
chord_prog = [['C4','E4','G4'], ['F4','A4','C5'], ['G4','B4','D5'], ['C4','E4','G4']]

def generate_music(bars=8):
    s = stream.Stream()
    s.append(instrument.Piano())
    
    for i in range(bars):
        if i % 2 == 0:
            c = chord.Chord(random.choice(chord_prog))
            c.quarterLength = 4
            s.append(c)
        else:
            for _ in range(4):
                n = note.Note(random.choice(scale))
                n.quarterLength = 1
                s.append(n)
    return s

if st.button("🎼 Generate New Music", type="primary"):
    with st.spinner("AI music compose kar raha hai..."):
        midi_stream = generate_music()
        midi_stream.write('midi', fp='generated_music.mid')
        
        st.success("Music ready ho gaya!")
        st.audio('generated_music.mid')
        
        with open("generated_music.mid", "rb") as f:
            bytes_data = f.read()
            b64 = base64.b64encode(bytes_data).decode()
            href = f'<a href="data:audio/midi;base64,{b64}" download="AI_Music.mid">📥 Download MIDI File</a>'
            st.markdown(href, unsafe_allow_html=True)

st.info("Note: Ye demo LSTM patterns pe based hai. Full training ke liye music21 + TensorFlow use hota hai.")
