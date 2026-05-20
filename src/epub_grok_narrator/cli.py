"""Command Line Interface for epub-grok-narrator."""

import click
from pathlib import Path
# from .parser import EPUBParser
# from .chunker import TextChunker
# from .tts import TTSGenerator
# from .exporter import AudioExporter


@click.group()
@click.version_option()
def cli():
    """epub-grok-narrator: Turn EPUBs into Grok Voice-ready audio narrations."""
    pass


@cli.command()
@click.argument("epub_file", type=click.Path(exists=True, dir_okay=False))
@click.option("--output", "-o", default="./output", help="Output directory for audio and manifest.")
@click.option("--voice", default="en", help="TTS language/voice code (e.g. en, en-us).")
@click.option("--speed", default=1.0, type=float, help="Speaking speed (gTTS slow mode if <1).")
@click.option("--max-chunk", default=4500, type=int, help="Max characters per TTS chunk.")
@click.option("--dry-run", is_flag=True, help="Inspect chapters without generating audio.")
def convert(epub_file: str, output: str, voice: str, speed: float, max_chunk: int, dry_run: bool):
    """Convert EPUB to audio narration chapters + manifest."""
    click.echo(f"Processing: {epub_file}")
    click.echo(f"Output dir: {output}")
    click.echo(f"Voice: {voice}, Speed: {speed}")

    if dry_run:
        click.echo("[DRY RUN] Would parse chapters and show structure.")
        # TODO: Implement dry run with parser
        return

    # Placeholder for full pipeline
    click.echo("\n[INFO] Full pipeline implementation in progress.")
    click.echo("Core modules (parser, chunker, tts, exporter) are ready for integration.")
    click.echo("Run with --dry-run or check the source for skeletons.")

    # Example future flow:
    # parser = EPUBParser(epub_file)
    # chapters = parser.extract_chapters()
    # chunker = TextChunker(max_chars=max_chunk)
    # tts = TTSGenerator(lang=voice, slow=(speed < 1))
    # exporter = AudioExporter(output)
    # ... process each chapter, generate chunks, save, build manifest


@cli.command()
@click.argument("epub_file", type=click.Path(exists=True))
def inspect(epub_file: str):
    """Inspect EPUB structure and chapters without audio generation."""
    click.echo(f"Inspecting: {epub_file}")
    click.echo("[TODO] Full inspection using EPUBParser coming soon.")


if __name__ == "__main__":
    cli()
