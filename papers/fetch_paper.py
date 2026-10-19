#!/usr/bin/env python3
"""Download the cited arXiv paper for local reading; keep its PDF out of Git."""

import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
from urllib.request import Request, urlopen


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    directory = Path(__file__).resolve().parent
    metadata = json.loads((directory / "source.json").read_text())
    target = directory / metadata["local_filename"]
    expected = metadata["pdf_sha256"]

    if target.exists():
        if sha256(target) != expected:
            raise ValueError(
                f"An existing file at {target} has a different checksum. "
                "Move it aside before downloading; it has not been changed."
            )
        print(f"Verified existing paper: {target}")
        return

    request = Request(
        metadata["pdf_url"],
        headers={"User-Agent": "BowlingActionPaperReference/1.0"},
    )
    temporary = None
    try:
        with urlopen(request, timeout=30) as response:
            with tempfile.NamedTemporaryFile(
                dir=directory, prefix=".paper-", suffix=".download", delete=False
            ) as output:
                temporary = Path(output.name)
                for chunk in iter(lambda: response.read(1024 * 1024), b""):
                    output.write(chunk)
        if sha256(temporary) != expected:
            raise ValueError("Downloaded PDF checksum differs from the verified source.")
        # Link atomically without overwriting a file created by another process.
        os.link(temporary, target)
        print(f"Downloaded and verified: {target}")
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Paper download failed: {error}", file=sys.stderr)
        sys.exit(1)
