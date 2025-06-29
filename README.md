Here is the updated `README.md` with `>>>` prompts added to all REPL example lines:

```markdown
# 🎶 MIDI REPL with NumPy, Mingus, and MIDIUtil

This project provides an interactive **REPL (Read-Eval-Print Loop)** for generating and manipulating MIDI files using Python. It leverages:

- `numpy` for numerical operations
- `mingus` for music theory functions (e.g. note ↔ int)
- `midiutil` for writing standard MIDI files

---

## 📦 Requirements

Install the required packages:

```bash
pip install numpy midiutil mingus
```

---

## 🚀 Running the REPL

Start the interactive MIDI REPL:

```bash
python cl.py
```

You’ll see:

```
🎶 MIDI + NumPy + Mingus REPL (type 'exit' to quit)
>>>
```

---

## 🛠️ Available Functions

### 🎼 Create a MIDI File

```python
>>> midi = create_midi(tracks=1, tempo=120)
```

---

### 🎵 Add Notes, Chords, Arpeggios

```python
>>> add_note(midi, 60, time=0)  # C4
>>> add_chord(midi, [60, 64, 67], time=1)
>>> add_arpeggio(midi, [60, 64, 67], time=2)
```

---

### 🪗 Work with Measures and Bars

```python
>>> set_meter(3, 4)  # Set time signature to 3/4
>>> add_measure(midi, [[60, 64, 67], [62, 65, 69], [64, 67, 71]], bar_number=1)
>>> fill_bar(midi, [60, 62, 64, 65], bar_number=2)
>>> print_bar_summary(2, [60, 62, 64, 65])
```

---

### 💾 Save to File

```python
>>> write_midi(midi, "output.mid")
```

---

## 🧠 Helper Tools

```python
>>> int_to_note(60)
'C'

>>> note_to_int('D#')
3

>>> note_name_with_octave(61)
'C#5'

>>> pretty_notes([60, 62, 64])
['C5', 'D5', 'E5']
```

---

## 🏁 Exiting the REPL

To exit:

```text
>>> exit
```

or

```text
>>> quit
```

---

## 📁 Example REPL Session

```python
>>> midi = create_midi()
>>> add_chord(midi, [60, 64, 67], 0)
>>> fill_bar(midi, [60, 62, 64, 65], 2)
>>> write_midi(midi, "example.mid")
```

---

## 📄 License

MIT License
```

Let me know if you want to include this as a string inside the script for dynamic help inside the REPL.
