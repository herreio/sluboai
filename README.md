# Clients for OAI-PMH repositories of SLUB Dresden

## Installation

```sh
# ... via SSH:
pip install -e git+ssh://git@github.com/herreio/sluboai.git#egg=sluboai
# ... or via HTTPS:
pip install -e git+https://github.com/herreio/sluboai.git#egg=sluboai
```

## Repositories

- [Qucosa](https://slub.qucosa.de/) (`sluboai.qucosa`)
- [Digital Collections](https://digital.slub-dresden.de/) (`sluboai.digital`)

## Dependencies

- [Sickle](https://sickle.readthedocs.io/)

## Usage

```py
# import package
import sluboai
# request record from Digital Collections
digital_rec = sluboai.digital.record("oai:de:slub-dresden:db:id-1738286142")
# request record from Qucosa
qucosa_rec = sluboai.qucosa.record("oai:qucosa:de:qucosa:72737")
```

Return type of `sluboai.base.Client.record` is [`sickle.models.Record`](https://sickle.readthedocs.io/en/latest/api.html#record-object).

```py
import json
print(json.dumps(digital_rec.metadata, ensure_ascii=False, indent=2))
```

```json
{
  "identifier": [
    "oai:de:slub-dresden:db:id-1738286142",
    "http://digital.slub-dresden.de/id1738286142",
    "urn:nbn:de:bsz:14-db-id17382861428"
  ],
  "title": [
    "Dante Alighieri's Göttliche Komödie in Zeichnungen"
  ],
  "creator": [
    "Witte, Karl; Emler, Bonaventura; Hanfstaengl, Hanns; Dante, Alighieri"
  ],
  "date": [
    "[circa 1861]"
  ],
  "coverage": [
    "Dresden"
  ],
  "format": [
    "application/mets+xml"
  ],
  "type": [
    "Text"
  ]
}
```

```py
print(json.dumps(qucosa_rec.metadata, ensure_ascii=False, indent=2))
```

```json
{
  "title": [
    "Der Computer als Denkzeug für hermeneutische Arbeit"
  ],
  "identifier": [
    "urn:nbn:de:bsz:14-qucosa2-727377",
    "https://slub.qucosa.de/id/qucosa%3A72737",
    "https://slub.qucosa.de/api/qucosa%3A72737/attachment/ATT-0/"
  ],
  "language": [
    "ger"
  ],
  "relation": [
    "10.25366/2020.87",
    "urn:nbn:de:bsz:14-qucosa2-727358",
    "qucosa:72735"
  ],
  "description": [
    "Computer science and the humanities seem to belong to two opposite sides within the spectrum of scientific methods and research. In the domain of digital humanities, however, formalization and hermeneutic interpretation have to be integrated. As will be argued in this article, this integration provides a fundamentally new challenge to both disciplines. \nIn particular, researchers from the humanities want to be sure that using the tools provided by computer science (big data, machine learning, etc.) do not change insights in any non-expected way. However, even if this could be partially secured, it cannot be achieved in general for most of the research practices. As will be demonstrated in the context of digital editions in musicology, it is impossible to design technology in a neutral or context-free manner. Due to the interests of different actors and institutions, numerous design conflicts arise where the implementation of requirements violates other, equally valid demands. To balance these conflicting requirements invariably brings  some bias to the overall design. Thus, it is important to develop a strategy for identifying potential influences as well as the impact of design decisions throughout the whole process of developing tools and infrastructures.\nThe paper presents an approach for hypotheses driven design of digital tools and infrastructures from a computer science point of view, placing great emphasis on supporting mutual understanding and ensuring a transparent design process."
  ],
  "subject": [
    "Digitale Musikwissenschaft, computer science, digital humanities",
    "info:eu-repo/classification/ddc/780",
    "ddc:780"
  ],
  "creator": [
    "Keil, Reinhard"
  ],
  "contributor": [
    "Musikwissenschaftliches Seminar der Universität Paderborn und der Hochschule für Musik Detmold"
  ],
  "date": [
    "2020-11-09"
  ],
  "rights": [
    "info:eu-repo/semantics/openAccess"
  ],
  "type": [
    "doc-type:conferenceObject",
    "info:eu-repo/semantics/conferenceObject",
    "doc-type:Text"
  ]
}
```
