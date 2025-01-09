# audio_expo
Audio manipulations w. Python.

E.g. get parts of audio file(MP3, AAC, WAV etc.), 
and extract raw samples - then get/calculate vital data from samples, 
like MAX/MIN-values and average level('energy').
Possibly scan lengthy audiofiles for 'active' parts and retrieve these passages.

Requirements:
- PyDub module
- 'libffi' installed (on Ubuntu/Linux), w. MP3/FLAC/AAC codecs
