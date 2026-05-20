"""Audio Exporter: Saves chapter audios and generates manifest.json for compatibility."""

import json
import os
from typing import List, Dict, Any
from tqdm import tqdm


class AudioExporter:
    """Export generated audio chunks/chapters and create playback manifest."""

    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def save_chapter_audio(self, chapter_title: str, audio_chunks: List[str], chapter_index: int) -> Dict[str, Any]:
        """Save audio for a chapter (list of chunk paths or single). Returns chapter info."""
        chapter_dir = os.path.join(self.output_dir, f"chapter_{chapter_index:03d}")
        os.makedirs(chapter_dir, exist_ok=True)

        saved_files = []
        for i, chunk_path in enumerate(audio_chunks):
            if os.path.exists(chunk_path):
                dest = os.path.join(chapter_dir, f"chunk_{i:03d}.mp3")
                # In real impl, move or copy; here assume already generated to temp
                # For simplicity in skeleton, we note the path
                saved_files.append(dest)

        chapter_info = {
            "index": chapter_index,
            "title": chapter_title,
            "audio_dir": chapter_dir,
            "num_chunks": len(saved_files),
            "files": saved_files,  # In full impl: actual relative paths
        }
        return chapter_info

    def generate_manifest(self, book_metadata: Dict, chapters_info: List[Dict], total_duration: float = 0.0) -> str:
        """Generate manifest.json with all info for voice players / Grok integration."""
        manifest = {
            "book": book_metadata,
            "total_chapters": len(chapters_info),
            "estimated_duration_seconds": total_duration,
            "chapters": chapters_info,
            "format_version": "1.0",
            "compatible_with": ["grok-voice", "standard-players", "custom-apps"],
            "instructions": "Use chapter audio files with the manifest for structured narration playback."
        }

        manifest_path = os.path.join(self.output_dir, "manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        return manifest_path

    def create_simple_playlist(self, chapters_info: List[Dict]) -> str:
        """Create a simple M3U playlist for easy playback."""
        playlist_path = os.path.join(self.output_dir, "playlist.m3u")
        with open(playlist_path, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for ch in chapters_info:
                f.write(f"#EXTINF:-1,{ch.get('title', 'Chapter')}\n")
                # Note: In full version, point to actual audio files
                f.write(f"{ch.get('audio_dir', '')}\n")
        return playlist_path
