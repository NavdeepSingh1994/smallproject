import streamlit as st
import xml.etree.ElementTree as ET
import streamlit.components.v1 as components
import pandas as pd
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="📦 DAM Viewer", page_icon="🗂")
st.title("Digital Asset Management – XML Viewer mit kleinem Onlineshop (WIP) - Bewerbungsgespräch IT-Projektmanager 10.06.2025")

# Aktuelle Uhrzeit
st.markdown("## 🕒 Aktuelle Uhrzeit")

clock_html = '''
<div id="clock" style="font-size:24px;font-weight:bold;margin-bottom:30px;color:#00c4ff"></div>
<script>
function updateClock() {
    const now = new Date();
    const timeStr = now.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    document.getElementById('clock').innerText = timeStr;
}
setInterval(updateClock, 1000);
updateClock();
</script>
'''
components.html(clock_html)

st.markdown("""
Diese Demo zeigt, wie XML-Daten aus einem Digital Asset Management (DAM) System verarbeitet und dargestellt werden können. Drei Modi:
1. **Nur XML-Datei hochladen** (z. B. einfache Asset-Daten)
2. **XML mit Stylesheet** (z. B. XSL für Vorschau oder erweiterte Struktur)
3. **KI-gestützte Suche in der XML** (GPT-gestützt, semantisch)
""")

# === Upload der einfachen XML ===
st.header("1️⃣ DAM XML ohne Stylesheet")
dam_plain = st.file_uploader("📂 XML-Datei hochladen", type="xml", key="plain")

if dam_plain:
    try:
        tree = ET.parse(dam_plain)
        root = tree.getroot()
        st.success("✅ XML geladen")

        assets_data = []

        for asset in root.findall("asset"):
            name = asset.find("name").text if asset.find("name") is not None else "(kein Name)"
            path = asset.find("path").text if asset.find("path") is not None else "(kein Pfad)"
            desc = asset.find("description").text if asset.find("description") is not None else ""
            category = asset.find("category").text if asset.find("category") is not None else "Sonstige"

            assets_data.append({"Name": name, "Pfad": path, "Beschreibung": desc, "Kategorie": category})

        df = pd.DataFrame(assets_data)

        selected_category = st.selectbox("🔍 Nach Kategorie filtern:", options=["Alle"] + sorted(df["Kategorie"].unique().tolist()))

        if selected_category != "Alle":
            df = df[df["Kategorie"] == selected_category]

        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Exportiere Tabelle als CSV", csv, "assets_export.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Fehler beim Parsen der XML: {e}")

# === Upload der XML mit Stylesheet ===
st.header("2️⃣ DAM XML mit Stylesheet")
dam_styles = st.file_uploader("📂 XML-Datei mit Stylesheet hochladen", type="xml", key="styled")

if dam_styles:
    try:
        tree = ET.parse(dam_styles)
        root = tree.getroot()
        st.success("✅ XML geladen")

        st.subheader("🌐 Web-Vorschau (HTML/JS)")

        for asset in root.findall("asset"):
            name = asset.find("name").text if asset.find("name") is not None else "(kein Name)"
            img = asset.find("url").text if asset.find("url") is not None else ""
            link = asset.find("link").text if asset.find("link") is not None else "https://navdeepsingh.dev/dam-showcase"
            cta = asset.find("cta").text if asset.find("cta") is not None else "Zum Shop"

            html = f'''
                <div style="background-color:#1e1e1e;padding:25px;border-radius:10px;border:1px solid #444;color:#f0f0f0;margin-bottom:30px;max-width:600px">
                    <h2 style="color:#00c4ff;margin-bottom:15px">{name}</h2>
                    {'<img src="' + img + '" alt="" style="width:100%;max-width:100%;border-radius:8px;margin-bottom:20px" />' if img else ''}
                    <div style="text-align:right">
                        <a href="{link}" target="_blank" style="display:inline-block;background:#00c4ff;padding:12px 24px;color:#000;border-radius:6px;text-decoration:none;font-weight:bold;font-size:16px;">{cta} 🚀</a>
                    </div>
                </div>
            '''
            components.html(html, height=430)

    except Exception as e:
        st.error(f"❌ Fehler beim Parsen oder Anzeigen: {e}")

# === KI-gestützte Suche ===
st.header("3️⃣ KI-Suche in XML")
st.markdown("Nutze GPT, um intelligente Fragen zu deinen Assets zu stellen (z. B. \"vegane Labels\", \"Produktbilder mit Creatin\" usw.)")

option = st.radio("📥 Eingabemethode wählen:", ["Textfeld", "Datei-Upload"])

xml_ki_input = ""
if option == "Textfeld":
    xml_ki_input = st.text_area("📄 XML-Inhalt einfügen", height=300)
elif option == "Datei-Upload":
    uploaded = st.file_uploader("📂 XML-Datei hochladen", type="xml", key="ai")
    if uploaded:
        xml_ki_input = uploaded.read().decode("utf-8")

query = st.text_input("💬 Deine Frage an das System:")

if st.button("🔎 Mit GPT suchen") and xml_ki_input and query:
    with st.spinner("Frage wird an GPT übergeben..."):
        try:
            system_prompt = """Du bist ein DAM-Assistent. Du bekommst eine XML-Liste mit Assets und eine Frage. Gib dem Nutzer eine relevante Liste mit Name, Beschreibung und Pfad der passenden Assets zurück. Gib nur Assets aus, die wirklich zur Frage passen."""

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Hier ist die XML:\n{xml_ki_input}\n\nFrage: {query}"}
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.3
            )

            answer = response["choices"][0]["message"]["content"]
            st.markdown("### 🧠 GPT-Antwort:")
            st.info(answer)

        except Exception as e:
            st.error(f"Fehler bei der GPT-Abfrage: {e}")
st.markdown("---")
st.markdown("🔗 [Zur interaktiven Bewerbungsdemo mit JavaScript & Fragen](http://localhost:8501/streamlit_main)")

st.markdown(
    "<small style='color:gray'>Hinweis: Diese Verlinkung demonstriert Webtechnologie-Kenntnisse mit Streamlit, HTML, CSS & JS.</small>",
    unsafe_allow_html=True
)