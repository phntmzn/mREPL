import numpy as np
from midiutil import MIDIFile
from mingus.core import notes as mingus_notes

def create_midi(tracks=1, tempo=120):
    midi = MIDIFile(tracks)
    midi.addTempo(0, 0, tempo)
    return midi

def add_note(midi, pitch, time, duration=1, volume=100, track=0, channel=0):
    midi.addNote(track, channel, pitch, time, duration, volume)

def add_chord(midi, pitches, time, duration=1, volume=80, track=0, channel=0):
    for p in pitches:
        add_note(midi, p, time, duration, volume, track, channel)

def add_arpeggio(midi, pitches, time, step=0.5, duration=0.5, volume=90, track=0, channel=0):
    for i, p in enumerate(pitches):
        add_note(midi, p, time + i * step, duration, volume, track, channel)

def add_measure(midi, chords, bar_number, duration=1, volume=80, track=0, channel=0):
    """Add one or more chords to a bar based on meter settings."""
    beats_per_bar = meter["numerator"]
    start_time = bar_start(bar_number)

    if isinstance(chords[0], list):  # multiple chords (one per beat)
        for i, chord in enumerate(chords):
            for note in chord:
                midi.addNote(track, channel, note, start_time + i, duration, volume)
    else:  # single chord
        for note in chords:
            midi.addNote(track, channel, note, start_time, duration, volume)


def fill_bar(midi, pitches, bar_number, volume=100, track=0, channel=0):
    """Evenly distributes notes across a measure based on meter."""
    beats_per_bar = meter["numerator"]
    start_time = bar_start(bar_number)
    step = beats_per_bar / len(pitches)

    for i, note in enumerate(pitches):
        time = start_time + i * step
        midi.addNote(track, channel, note, time, step, volume)

def print_bar_summary(bar_number, notes):
    note_names = pretty_notes(notes)
    print(f"📏 Bar {bar_number}: {' '.join(note_names)}")








# Global meter (default 4/4)
meter = {"numerator": 4, "denominator": 4}

def set_meter(numerator, denominator):
    meter["numerator"] = numerator
    meter["denominator"] = denominator
    print(f"🎵 Meter set to {numerator}/{denominator}")

def bar_start(bar_number):
    """Get the starting beat time of a given measure/bar number."""
    return (bar_number - 1) * meter["numerator"]


def write_midi(midi, filename):
    with open(filename, "wb") as f:
        midi.writeFile(f)
        print(f"✅ MIDI written to {filename}")

def note_name_with_octave(n):
    name = mingus_notes.int_to_note(n % 12)
    octave = n // 12
    return f"{name}{octave}"

def pretty_notes(notes_list):
    return [note_name_with_octave(n) for n in notes_list]



def run_repl():
    print("🎶 MIDI + NumPy + Mingus REPL (type 'exit' to quit)")
    local_scope = {
        "np": np,
        "MIDIFile": MIDIFile,
        "create_midi": create_midi,
        "add_note": add_note,
        "add_chord": add_chord,
        "add_arpeggio": add_arpeggio,
        "write_midi": write_midi,
        "int_to_note": mingus_notes.int_to_note,
        "note_to_int": mingus_notes.note_to_int,
        "note_name_with_octave": note_name_with_octave,
        "pretty_notes": pretty_notes,
        "set_meter": set_meter,
        "bar_start": bar_start,
        "meter": meter,
        "add_measure": add_measure,
        "fill_bar": fill_bar,
        "print_bar_summary": print_bar_summary,
    }

    while True:
        try:
            code = input(">>> ")
            if code.lower() in ("exit", "quit"):
                print("👋 Bye!")
                break

            try:
                result = eval(code, globals(), local_scope)
                if result is not None:
                    print(result)
            except SyntaxError:
                exec(code, globals(), local_scope)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run_repl()
