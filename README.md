# Usage
Command line for now:

```
python client.py
```

# Dependencies
- [pytube](https://github.com/pytube/pytube/)
- [pydub](https://github.com/jiaaro/pydub)
    - ffmpeg
- [eyed3](https://eyed3.readthedocs.io/en/latest/installation.html)

# Notes
### Windows 10
- Issue with `ffmpeg` when running `pydub` solved with [GitHub Issue #604](https://github.com/jiaaro/pydub/issues/604)
- Issue with `pydub` calling `subprocess.py` fixed on line 274
from 
```python
res = Popen(command, stdin=stdin_parameter, stdout=PIPE, stderr=PIPE)

```
to
```python
res = Popen(command, stdin=stdin_parameter, stdout=PIPE, stderr=PIPE, shell=True)

```
Should probably do check for OS but I can't be bothered lmao
