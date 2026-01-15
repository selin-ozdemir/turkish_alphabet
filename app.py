import streamlit as st

# FORCE LIGHT THEME - THIS FIXES THE BLACK BACKGROUND!
st.markdown("""
    <style>
    /* Override Streamlit's theme completely */
    .stApp {
        background-color: #f8fafc !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #f8fafc !important;
    }
    [data-testid="stHeader"] {
        background-color: #ffffff !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="Turkish Alphabet Pronunciation Guide",
    page_icon="🇹🇷",
    layout="wide"
)

# Rest of your styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #e11d48 !important;
        color: white !important;
        font-size: 20px;
        font-weight: bold;
        border-radius: 8px;
        padding: 15px;
        border: none;
        width: 100%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #be123c !important;
        transform: scale(1.05);
    }
    .word-card {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 8px;
        border: 2px solid #e5e7eb;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    .word-card h3 {
        color: #e11d48 !important;
        margin-top: 0;
        font-size: 20px;
    }
    .word-card p {
        color: #374151 !important;
        margin: 5px 0;
    }
    .tips-box {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 8px;
        border: 2px solid #fbbf24;
        margin-top: 20px;
    }
    .tips-box h3 {
        color: #1f2937 !important;
        margin-top: 0;
    }
    .tips-box ul {
        color: #374151 !important;
    }
    .tips-box li {
        color: #374151 !important;
    }
    .selected-letter {
        background-color: #ffffff !important;
        padding: 25px;
        border-radius: 8px;
        border: 2px solid #e11d48;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .selected-letter h2 {
        color: #e11d48 !important;
        font-size: 48px;
        margin: 0;
    }
    .selected-letter p {
        color: #374151 !important;
        font-size: 18px;
        margin: 10px 0;
    }
    .selected-letter strong {
        color: #1f2937 !important;
    }
    .selected-letter .sound {
        color: #e11d48 !important;
        font-weight: bold;
        font-size: 22px;
    }
    /* Force all text to be dark */
    h1, h2, h3, h4, h5, h6 {
        color: #1f2937 !important;
    }
    p, span, div, label {
        color: #374151 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'selected_letter' not in st.session_state:
    st.session_state.selected_letter = None

# Turkish alphabet data
alphabet = [
    {'letter': 'A', 'sound': 'ah', 'example': 'father', 'turkish': 'anne', 'meaning': 'mother'},
    {'letter': 'B', 'sound': 'b', 'example': 'bed', 'turkish': 'baba', 'meaning': 'father'},
    {'letter': 'C', 'sound': 'j', 'example': 'jam', 'turkish': 'cam', 'meaning': 'glass'},
    {'letter': 'Ç', 'sound': 'ch', 'example': 'chair', 'turkish': 'çay', 'meaning': 'tea'},
    {'letter': 'D', 'sound': 'd', 'example': 'dog', 'turkish': 'dört', 'meaning': 'four'},
    {'letter': 'E', 'sound': 'eh', 'example': 'bed', 'turkish': 'el', 'meaning': 'hand'},
    {'letter': 'F', 'sound': 'f', 'example': 'fish', 'turkish': 'fırtına', 'meaning': 'storm'},
    {'letter': 'G', 'sound': 'g', 'example': 'go', 'turkish': 'gül', 'meaning': 'rose'},
    {'letter': 'Ğ', 'sound': 'silent/lengthens', 'example': 'lengthens vowel', 'turkish': 'dağ', 'meaning': 'mountain'},
    {'letter': 'H', 'sound': 'h', 'example': 'house', 'turkish': 'hasta', 'meaning': 'sick'},
    {'letter': 'I', 'sound': 'uh', 'example': 'cousin (unstressed)', 'turkish': 'ışık', 'meaning': 'light'},
    {'letter': 'İ', 'sound': 'ee', 'example': 'see', 'turkish': 'iyi', 'meaning': 'good'},
    {'letter': 'J', 'sound': 'zh', 'example': 'treasure', 'turkish': 'jilet', 'meaning': 'razor'},
    {'letter': 'K', 'sound': 'k', 'example': 'kite', 'turkish': 'kedi', 'meaning': 'cat'},
    {'letter': 'L', 'sound': 'l', 'example': 'love', 'turkish': 'limon', 'meaning': 'lemon'},
    {'letter': 'M', 'sound': 'm', 'example': 'mother', 'turkish': 'mavi', 'meaning': 'blue'},
    {'letter': 'N', 'sound': 'n', 'example': 'nice', 'turkish': 'nine', 'meaning': 'grandmother'},
    {'letter': 'O', 'sound': 'oh', 'example': 'phone', 'turkish': 'okul', 'meaning': 'school'},
    {'letter': 'Ö', 'sound': 'uh', 'example': 'bird (British)', 'turkish': 'öğle', 'meaning': 'noon'},
    {'letter': 'P', 'sound': 'p', 'example': 'park', 'turkish': 'para', 'meaning': 'money'},
    {'letter': 'R', 'sound': 'r', 'example': 'rolled r', 'turkish': 'renk', 'meaning': 'color'},
    {'letter': 'S', 'sound': 's', 'example': 'sun', 'turkish': 'su', 'meaning': 'water'},
    {'letter': 'Ş', 'sound': 'sh', 'example': 'ship', 'turkish': 'şeker', 'meaning': 'sugar'},
    {'letter': 'T', 'sound': 't', 'example': 'top', 'turkish': 'tuz', 'meaning': 'salt'},
    {'letter': 'U', 'sound': 'oo', 'example': 'moon', 'turkish': 'uçak', 'meaning': 'airplane'},
    {'letter': 'Ü', 'sound': 'ew', 'example': 'few', 'turkish': 'üzüm', 'meaning': 'grape'},
    {'letter': 'V', 'sound': 'v', 'example': 'van', 'turkish': 'vazo', 'meaning': 'vase'},
    {'letter': 'Y', 'sound': 'y', 'example': 'yes', 'turkish': 'yol', 'meaning': 'road'},
    {'letter': 'Z', 'sound': 'z', 'example': 'zoo', 'turkish': 'zaman', 'meaning': 'time'}
]

common_words = [
    {'word': 'Merhaba', 'pronunciation': 'mehr-hah-bah', 'meaning': 'Hello'},
    {'word': 'Teşekkür ederim', 'pronunciation': 'teh-shehk-kur eh-deh-reem', 'meaning': 'Thank you'},
    {'word': 'Günaydın', 'pronunciation': 'gew-nay-duhn', 'meaning': 'Good morning'},
    {'word': 'İyi akşamlar', 'pronunciation': 'ee-yee ahk-shahm-lahr', 'meaning': 'Good evening'},
    {'word': 'Nasılsınız', 'pronunciation': 'nah-suhl-suh-nuhz', 'meaning': 'How are you?'},
    {'word': 'Lütfen', 'pronunciation': 'lewt-fehn', 'meaning': 'Please'},
    {'word': 'Evet', 'pronunciation': 'eh-veht', 'meaning': 'Yes'},
    {'word': 'Hayır', 'pronunciation': 'hah-yuhr', 'meaning': 'No'}
]

def translate_text(text):
    """Convert Turkish text to approximate English pronunciation"""
    if not text:
        return ""
    
    rules = {
        'c': 'j', 'ç': 'ch', 'ğ': '', 'ı': 'uh', 'i': 'ee', 'İ': 'ee',
        'j': 'zh', 'ö': 'uh', 'ş': 'sh', 'ü': 'ew', 'u': 'oo',
        'C': 'J', 'Ç': 'Ch', 'Ğ': '', 'I': 'Uh', 'Ö': 'Uh',
        'Ş': 'Sh', 'Ü': 'Ew', 'U': 'Oo'
    }
    
    result = ''
    for char in text:
        result += rules.get(char, char)
    return result

# Title
st.title("🇹🇷 Turkish Alphabet Pronunciation Guide")
st.markdown("**Learn to read Turkish using English sounds**")
st.markdown("---")

# The Alphabet Section
st.header("📖 The Alphabet")
st.write("Click on any letter to see its pronunciation:")

# Create columns for the alphabet grid
cols_per_row = 7
for i in range(0, len(alphabet), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, col in enumerate(cols):
        if i + j < len(alphabet):
            letter_data = alphabet[i + j]
            with col:
                if st.button(letter_data['letter'], key=f"btn_{i+j}", use_container_width=True):
                    st.session_state.selected_letter = letter_data

# Display selected letter information
if st.session_state.selected_letter is not None:
    letter = st.session_state.selected_letter
    st.markdown(f"""
    <div class='selected-letter'>
        <h2>🔊 {letter['letter']}</h2>
        <p><strong>Sound:</strong> <span class='sound'>{letter['sound']}</span></p>
        <p><strong>Like in English:</strong> <em>{letter['example']}</em></p>
        <p><strong>Example word:</strong> <strong>{letter['turkish']}</strong> ({letter['meaning']})</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Common Turkish Words Section
st.header("💬 Common Turkish Words")

col1, col2 = st.columns(2)
for idx, item in enumerate(common_words):
    target_col = col1 if idx % 2 == 0 else col2
    with target_col:
        st.markdown(f"""
        <div class='word-card'>
            <h3>{item['word']}</h3>
            <p><em>{item['pronunciation']}</em></p>
            <p>"{item['meaning']}"</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Practice Reading Section
st.header("✨ Practice Reading")
st.write("Type any Turkish word and see how to pronounce it!")

practice_text = st.text_input("", placeholder="Try: Istanbul, Ankara, Türkiye...", key="practice")

if practice_text:
    pronunciation = translate_text(practice_text)
    st.markdown(f"""
    <div class='word-card'>
        <p><strong>Turkish:</strong> {practice_text}</p>
        <p><strong>Approximate pronunciation:</strong> <span class='sound'>{pronunciation}</span></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Tips Section
st.markdown("""
<div class='tips-box'>
    <h3>💡 Key Tips:</h3>
    <ul>
        <li>Turkish is phonetic - each letter always makes the same sound</li>
        <li><strong>C</strong> sounds like J in "jam", not K</li>
        <li><strong>Ç</strong> sounds like CH in "chair"</li>
        <li><strong>Ş</strong> sounds like SH in "ship"</li>
        <li><strong>Ğ</strong> (soft g) is silent and lengthens the previous vowel</li>
        <li><strong>I</strong> (undotted) sounds like "uh", <strong>İ</strong> (dotted) sounds like "ee"</li>
    </ul>
</div>
""", unsafe_allow_html=True)
