<h1>Morse Code Converter</h1>
<p>This project is a Morse Code Converter that translates text to Morse code and plays the Morse code using sound. It's built using Python and the <code>pydub</code> library for handling audio playback.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#how-it-works">How it Works</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
</ul>

<h2 id="features">Features</h2>
<ul>
    <li>Converts plain text to Morse code.</li>
    <li>Plays Morse code as audio beeps.</li>
    <li>Supports configurable durations for dots, dashes, and spaces.</li>
</ul>

<h2 id="installation">Installation</h2>
<h3>Prerequisites</h3>
<ul>
    <li>Python 3.x</li>
    <li><code>pydub</code> library</li>
    <li><code>ffmpeg</code> or <code>libav</code> installed and available in the system path.</li>
</ul>

<h3>Steps</h3>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/morse-code-converter.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd morse-code-converter</code></pre>
    </li>
    <li>Set up a virtual environment (optional but recommended):
        <pre><code>
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        </code></pre>
    </li>
    <li>Install the required packages:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h3>FFmpeg Installation</h3>
<p>On macOS:</p>
<pre><code>brew install ffmpeg</code></pre>

<p>On Windows:</p>
<p>Download the FFmpeg executable from <a href="https://ffmpeg.org/download.html">FFmpeg</a> and add it to your PATH.</p>

<p>On Linux:</p>
<pre><code>sudo apt-get install ffmpeg</code></pre>

<h2 id="usage">Usage</h2>
<ol>
    <li>Create a text file with the message you want to convert to Morse code.</li>
    <li>Run the script:
        <pre><code>python main.py</code></pre>
    </li>
    <li>Enter the text to be converted when prompted, or modify the script to read from a file.</li>
</ol>

<h3>Example</h3>
<pre><code>
text = "HELLO WORLD"
morse_code = text_to_morse(text)
print(morse_code)
play_morse(morse_code)
</code></pre>

<h2 id="how-it-works">How it Works</h2>
<ol>
    <li>The <code>text_to_morse</code> function converts plain text to Morse code using a predefined dictionary.</li>
    <li>The <code>play_morse</code> function iterates over the Morse code string and plays the corresponding sound for dots and dashes using the <code>pydub</code> library.</li>
    <li>Timing between characters and words is managed using silent audio segments.</li>
</ol>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! Please follow these steps to contribute:</p>
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch:
        <pre><code>git checkout -b feature/your-feature-name</code></pre>
    </li>
    <li>Commit your changes:
        <pre><code>git commit -m 'Add some feature'</code></pre>
    </li>
    <li>Push to the branch:
        <pre><code>git push origin feature/your-feature-name</code></pre>
    </li>
    <li>Open a pull request.</li>
</ol>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2 id="acknowledgements">Acknowledgements</h2>
<ul>
    <li><a href="https://github.com/jiaaro/pydub">pydub</a> - A simple and easy high-level interface for manipulating audio with Python.</li>
    <li><a href="https://ffmpeg.org/">FFmpeg</a> - A complete, cross-platform solution to record, convert and stream audio and video.</li>
</ul>
