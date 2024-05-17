from ascii import ascii_art
from pydub import AudioSegment
from pydub.playback import play

# ---------------- Constants and Variables ---------------------
DOT_DURATION = 200  # milliseconds
DASH_DURATION = DOT_DURATION * 3
FREQUENCY = 950  # Hertz
LETTER_BREAK_DURATION = DOT_DURATION * 3  # longer break between letters
WORD_BREAK_DURATION = DOT_DURATION * 7  # longer break between words
SILENCE = 0

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '\\': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
}


# ---------------- Text Functionality ---------------------
def text_to_code():
    morse_code = []
    text_convert = text.upper()
    for letter in text_convert:
        if letter in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[letter])
        else:
            morse_code.append(' ')
    return ' '.join(morse_code)


# ---------------- Sound Functionality ----------------------
def play_sound(sound_file, duration):
    sound = AudioSegment.from_wav(sound_file)
    sound = sound[:duration]  # Truncate to get duration
    play(sound)


def silent():
    silence = AudioSegment.silent(duration=1000)
    play(silence)


def play_morse(morse_code):
    for char in morse_code:
        if char == '.':
            play_sound('beep.wav', DOT_DURATION)
        elif char == '-':
            play_sound('beep.wav', DASH_DURATION)
        elif char == ' ':
            silent()


# ---------------- Morse to Text and Sound ----------------------
print(ascii_art)
text = input('Type the text you want to convert.\n')
morse_code = text_to_code()
print(morse_code)
play_morse(morse_code)
