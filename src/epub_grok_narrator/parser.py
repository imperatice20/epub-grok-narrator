"""EPUB Parser module for extracting chapters and content."""

from ebooklib import epub
import re
from bs4 import BeautifulSoup
from typing import List, Dict, Any


class EPUBParser:
    """Parse EPUB files and extract structured content for narration."""

    def __init__(self, epub_path: str):
        self.epub_path = epub_path
        self.book = None
        self.chapters = []

    def load(self):
        """Load the EPUB book."""
        self.book = epub.read_epub(self.epub_path)
        return self.book

    def extract_metadata(self) -> Dict[str, Any]:
        """Extract book metadata."""
        if not self.book:
            self.load()
        metadata = {
            "title": self.book.get_metadata("DC", "title"),
            "author": self.book.get_metadata("DC", "creator"),
            "language": self.book.get_metadata("DC", "language"),
            "identifier": self.book.get_metadata("DC", "identifier"),
        }
        return metadata

    def extract_chapters(self) -> List[Dict[str, Any]]:
        """Extract chapters with title and cleaned text content."""
        if not self.book:
            self.load()

        chapters = []
        for item in self.book.get_items():
            if item.get_type() == epub.ITEM_DOCUMENT:
                # Get chapter title from spine or filename
                soup = BeautifulSoup(item.get_content(), "html.parser")
                
                # Try to find chapter title
                title = None
                h1 = soup.find("h1")
                if h1:
                    title = h1.get_text(strip=True)
                elif soup.find("title"):
                    title = soup.find("title").get_text(strip=True)
                else:
                    title = item.get_name().replace(".xhtml", "").replace("_", " ").title()

                # Extract and clean text
                text = self._clean_text(soup.get_text())

                if text.strip():  # Only include if there's content
                    chapters.append({
                        "id": item.get_id(),
                        "title": title,
                        "content": text,
                        "file_name": item.get_name(),
                    })

        self.chapters = chapters
        return chapters

    def _clean_text(self, text: str) -> str:
        """Clean extracted text for better TTS narration."""
        # Remove excessive whitespace
        text = re.sub(r"\s+", " ", text)
        # Remove common EPUB artifacts or navigation text if needed
        text = re.sub(r"(?i)(table of contents|copyright|all rights reserved)", "", text)
        text = text.strip()
        return text

    def get_chapter_count(self) -> int:
        return len(self.chapters)
