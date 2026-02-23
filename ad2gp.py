import argparse
from pathlib import Path

from mido import MidiFile, MidiTrack

from guitar_pro_map import mapping


def convert(midi: MidiFile) -> MidiFile:
    track = midi.tracks[0]  # We assume that we have one and only midi track

    for msg in track:
        if hasattr(msg, 'note'):
            msg.note = mapping[msg.note]

    return midi


def open_file(path: str) -> MidiFile:
    return MidiFile(path, clip=True)


def main():
    parser = argparse.ArgumentParser(description="Convert .midi from addictive drums 2 layout to Guitar Pro 7 layout. "
                                                 "Midi file should contain only one midi track!")
    parser.add_argument('file', help='Path to .midi file')

    args = parser.parse_args()
    midi_file = open_file(args.file)
    midi_file = convert(midi_file)

    input_path = Path(args.file)
    output_path = input_path.with_name(f"{input_path.stem}_converted.midi")
    midi_file.save(output_path.as_posix())


if __name__ == '__main__':
    main()
