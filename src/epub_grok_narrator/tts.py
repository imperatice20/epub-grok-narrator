"""TTS Generator module - extensible for multiple backends including future Grok Voice."""

from gtts import gTTS
from typing import Optional
import os


class TTSGenerator:
    """Wrapper for Text-to-Speech engines."""

    def __init__(self, engine: str = "gtts", lang: str = "en", slow: bool = False):
        self.engine = engine.lower()
        self.lang = lang
        self.slow = slow
        # TODO: Add support for other engines

    def generate_audio(self, text: str, output_path: str) -> str:
        """Generate audio file from text. Returns path to saved file."""
        if self.engine == "gtts":
            return self._generate_gtts(text, output_path)
        else:
            raise NotImplementedError(f"TTS engine '{self.engine}' not yet implemented. Use 'gtts' or extend the class.")

    def _generate_gtts(self, text: str, output_path: str) -> str:
        """Generate using Google TTS."""
        if not text.strip():
            return ""
        tts = gTTS(text=text, lang=self.lang, slow=self.slow)
        tts.save(output_path)
        return output_path

    # Placeholder for future engines
    # def _generate_openai(self, text, output_path): ...
    # def _generate_elevenlabs(self, text, output_path): ...
    # def _generate_grok_voice(self, text, output_path): ...  # When xAI provides API

    def get_supported_engines(self) -> list:
        return ["gtts"]  # Extend as implemented
