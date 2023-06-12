# Remove Background
### Streamlit app that uses rembg to remove the background from a picture.
<hr>

***NOTE: Images provided are generated by Stable Diffusion***
<br>
Image generation metadata has been preserved to mark the files.
<br>
Files are CC0 and published for research and testing purposes.

<hr>

Open a command prompt and `cd` to a new directory of your choosing:

(optional; recommended) Create a virtual environment with:
```
python -m venv "venv"
venv\Scripts\activate
```

To install do:
```
git clone https://github.com/vluz/RemoveBackground.git
cd RemoveBackground
pip install -r requirements.txt
```

On first run it may download several models.
<br>
The GUI may be blank or unresponsive for the duration of the setup.
<br>
It will take quite some time, both on reqs above and on first run.
<br>
Please allow it time to finish.
<br>
All runs after the first are then faster to load.

To run do:<br>
`streamlit run delbg.py`

Gui will open on your default browser

<hr>

TODO: add other methods, display all outputs and let user choose the best

NOTE: Not tested, do not use in production

