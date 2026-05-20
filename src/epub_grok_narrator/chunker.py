"""Text chunking module optimized for TTS narration."""

from typing import List
import re


class TextChunker:
    """Split text into chunks suitable for TTS engines (respecting char limits and natural breaks)."""

    def __init__(self, max_chars: int = 4500, min_chars: int = 200):
        self.max_chars = max_chars  # Safe limit for most TTS (gTTS ~5000, others vary)
        self.min_chars = min_chars

    def chunk_text(self, text: str) -> List[str]:
        """Split text into chunks preferring sentence/paragraph boundaries."""
        if not text or len(text) <= self.max_chars:
            return [text] if text.strip() else []

        chunks = []
        # Split into paragraphs first
        paragraphs = re.split(r"\n{2,}", text)

        current_chunk = ""

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            if len(current_chunk) + len(para) + 1 <= self.max_chars:
                current_chunk += (" " if current_chunk else "") + para
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                # If paragraph itself is too long, split by sentences
                if len(para) > self.max_chars:
                    chunks.extend(self._split_by_sentences(para))
                else:
                    current_chunk = para
                    continue
                current_chunk = ""

        if current_chunk:
            chunks.append(current_chunk)

        # Further split any oversized chunks
        final_chunks = []
        for chunk in chunks:
            if len(chunk) > self.max_chars:
                final_chunks.extend(self._split_by_sentences(chunk))
            else:
                final_chunks.append(chunk)

        return [c.strip() for c in final_chunks if c.strip()]

    def _split_by_sentences(self, text: str) -> List[str]:
        """Split text by sentence boundaries."""
        # Simple sentence splitter (can be improved with NLTK/spacy)
        sentences = re.split(r"(?<=[.!?])\s+", text)
        chunks = []
        current = ""

        for sent in sentences:
            sent = sent.strip()
            if not sent:
                continue
            if len(current) + len(sent) + 1 <= self.max_chars:
                current += (" " if current else "") + sent
            else:
                if current:
                    chunks.append(current)
                current = sent
        if current:
            chunks.append(current)

        return chunks
