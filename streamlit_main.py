import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CELUM Bewerbung – Gesprächsfragen", layout="centered")

st.title("Nachbereitungsfragen Bewerbungsgespräch 17.06.25")

# Textbasierte Darstellung mit Expander
with st.expander("1. Ab wann könnten Sie bei CELUM starten?"):
    st.markdown("""
    Ich kann offiziell ab dem **01.09.2025** starten, wenn ich bis Ende Juni kündige.
    Falls das keine Option ist, kann ich mit meinem Chapter Lead und Functional Lead nochmal 
    eine Anfrage haben, ob ich die Firma mit Ende Juli verlassen kann, das lässt sich vereinbaren.  
    Mein Chapter Lead ist informiert und unterstützt meinen Wechsel.  
    Mein Functional Lead bindet mich aktuell noch für:
    - Erstellung von Confluence-Dokumentationen  
    - Knowledge Transfers  
    - Abend-Deployments  
    """)

with st.expander("2. Letzter Einsatz"):
    st.markdown(""" 
    Ich habe **2015 während der Flüchtlingskrise** im Bundesheer mitgeholfen und möchte dem Staat etwas zurückgeben.  
    Der **letzte Einsatz** ist vom **20.–31. Oktober 2025** – danach habe ich alle Pflichttage abgeleistet.
    """)

with st.expander("3. Gehaltsvorstellungen"):
    st.markdown("""
    Wie mit **Moritz** besprochen, liegt meine Gehaltsvorstellung bei **75.000 EUR brutto Jahresgehalt**.
    """)

# Eingebettetes JavaScript als Zusatz
st.subheader("🧠 Interaktive JavaScript-Demo")
components.html("""
    <div style='padding:10px;font-family:sans-serif;border:1px solid #ccc;border-radius:5px;max-width:600px'>
        <h4 style='color:#3366cc;'>Live JavaScript: Frageauswahl</h4>
        <p>Wähle eine Frage:</p>
        <select onchange="document.getElementById('antwort').innerText = this.value">
            <option value=''>-- Bitte wählen --</option>
            <option value='Ich kann ab 01.09.2025 starten, ggf. auch ab August.'>Startdatum</option>
            <option value='Letzter Milizeinsatz 20.–31.10.2025, danach vollständig verfügbar.'>Miliz</option>
            <option value='Gehaltswunsch: 75.000 EUR brutto, mit Moritz besprochen.'>Gehaltswunsch</option>
        </select>
        <p id='antwort' style='margin-top:1em;color:darkgreen;font-weight:bold;'></p>
    </div>
    """, height=250)
