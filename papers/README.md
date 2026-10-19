# Research paper

**Deep Learning Based Illegal Bowling Action Detection**  
Debopom Sutradhar, Niful Islam, Sudipto Mondal, Tasmima Hossain Jamim,
Jubaer Muhammad Shufol, and Swakkhar Shatabda.  
arXiv:2610.07223, version 1, submitted October 5, 2026.

- [Abstract and version history](https://arxiv.org/abs/2610.07223)
- [Version 1 HTML](https://arxiv.org/html/2610.07223v1)
- [Version 1 PDF](https://arxiv.org/pdf/2610.07223v1)
- [DOI](https://doi.org/10.48550/arXiv.2610.07223)
- [BibTeX citation](paper.bib)
- [Source metadata and PDF checksum](source.json)

## Download a local copy

Run from the repository root with Python 3:

```bash
python3 papers/fetch_paper.py
```

The command downloads the original PDF from arXiv into
`papers/2610.07223v1.pdf` and verifies its SHA-256 checksum. The file is
50,181,621 bytes (about 47.9 MiB). An existing verified copy is reused.
No third-party Python packages are needed.

## Paper license

The paper is posted under the **arXiv.org perpetual, non-exclusive license**.
The repository's MIT license applies to its released software and does not
automatically relicense the separately published paper. arXiv describes its
default license as granting limited distribution rights to arXiv and limiting
reuse by others. No separate permission to republish the complete paper was
identified as of October 19, 2026.

This directory therefore tracks the paper's citation, official source URLs,
metadata, and download command. The downloaded PDF is ignored by Git. A future
PDF addition should include permission from the rights holder or an applicable
redistribution license.

Source: [arXiv license information](https://info.arxiv.org/help/license/index.html).

## Code version reviewed alongside the paper

The source repository cited by the paper is
[Debopom/Illegal-Bowling-Action-Detection](https://github.com/Debopom/Illegal-Bowling-Action-Detection).
The code snapshot reviewed with this reference was commit
`943ec5180370bcf2e7b04fbda710994b0db08667`.

Adding this paper reference does not supply the trained `model.pt` file
referenced by `classifier.ipynb`. That file is absent from this snapshot.
