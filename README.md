# epub-grok-narrator

A powerful tool to convert EPUB eBooks into high-quality audio narrations optimized for **Grok Voice** and other AI voice systems.

Transform your digital library into immersive audiobooks with intelligent chapter detection, natural text chunking, and professional TTS generation.

## Features

- **EPUB Parsing**: Robust extraction of chapters, titles, authors, and structured content using `ebooklib`.
- **Smart Text Processing**: Cleans HTML, normalizes text, splits into narration-friendly chunks (sentences/paragraphs) to avoid TTS limits and ensure natural pacing.
- **Multiple TTS Backends**: 
  - Default: Google TTS (gTTS) for quick demos.
  - Extensible: Easy integration with OpenAI TTS, ElevenLabs, Azure Cognitive Services, or local models (Coqui, Piper, etc.).
  - Future: Direct Grok Voice / xAI TTS integration when available.
- **Chapterized Output**: Generates individual chapter audio files + a `manifest.json` with metadata, timestamps, and playback info for easy import into players or Grok-compatible apps.
- **Audiobook Assembly** (optional): Concatenate chapters into a single MP3/M4B with chapter markers (requires ffmpeg).
- **CLI & Library**: Usable as command-line tool or importable Python module.
- **Progress & Resumability**: Track processing with tqdm; resume interrupted conversions.
- **Customization**: Voice selection, speed, pitch, language, chunk size, and more.
- **Metadata Preservation**: Embeds or exports book metadata for rich voice experiences.

## Why for Grok Voice?

Grok Voice excels with well-structured, naturally paced text and high-quality audio segments. This tool prepares EPUB content specifically for optimal voice synthesis:
- Proper sentence segmentation for prosody.
- Chapter-aware chunking.
- Cleaned, readable text free of EPUB artifacts.
- Structured output (JSON manifest + audio) ready for voice apps, agents, or custom Grok workflows.

## Installation

### Prerequisites
- Python 3.10+
- ffmpeg (optional, for full audiobook concatenation)

```bash
pip install -r requirements.txt
```

For ffmpeg on Ubuntu/Debian:
```bash
sudo apt-get install ffmpeg
```

## Quick Start

```bash
# Basic usage: Convert an EPUB to audio chapters
python -m epub_grok_narrator.cli convert mybook.epub --output ./audiobook_output

# With specific voice and speed
python -m epub_grok_narrator.cli convert mybook.epub --voice en --speed 1.1 --output ./my_narration

# List available chapters without generating audio
python -m epub_grok_narrator.cli inspect mybook.epub
```

## Project Structure

```
epub-grok-narrator/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── epub_grok_narrator/
│       ├── __init__.py
│       ├── parser.py          # EPUB parsing and chapter extraction
│       ├── chunker.py         # Intelligent text chunking for TTS
│       ├── tts.py             # TTS engine wrappers (gTTS, extensible)
│       ├── exporter.py        # Audio export, manifest generation
│       ├── cli.py             # Command-line interface
├── examples/
├── tests/
└── pyproject.toml (future packaging)
```

## Current Status

**v0.1.0 - Initial Setup**

The repository is initialized with project structure and plans. Core implementation is in progress. Check back soon for working code or contribute!

## Roadmap

- [x] Initial repo setup with detailed README
- [ ] Core EPUB parser with chapter detection
- [ ] Text cleaning and chunker optimized for natural TTS
- [ ] gTTS backend integration
- [ ] JSON manifest + per-chapter audio exporter
- [ ] Full CLI with argparse/click and rich progress
- [ ] Additional TTS providers (OpenAI TTS, ElevenLabs)
- [ ] Optional full audiobook assembly (single file + chapters)
- [ ] Support for images/covers in output if relevant
- [ ] Gradio or simple web demo
- [ ] Direct integration hooks for Grok / xAI voice
- [ ] Docker container
- [ ] Comprehensive tests and documentation

## Usage Examples (Planned)

After implementation:

```python
 from epub_grok_narrator import Narrator

 narrator = Narrator(epub_path="book.epub")
 narrator.process(output_dir="./output", tts_engine="gtts", voice="en", speed=1.0)
```

## Contributing

We welcome contributions to make this the best EPUB-to-voice tool for Grok users and beyond!

- Improve parsing for complex EPUBs
- Add new TTS backends
- Optimize chunking algorithms for more natural narration
- Add support for SSML, pauses, emphasis
- Build UI components

Fork, branch, and open a PR.

## License

MIT

## Acknowledgments

Inspired by the desire to make every EPUB come alive with Grok's voice.

---

**Let's build the ultimate audiobook creator for the AI era!**