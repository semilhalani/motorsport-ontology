# Motorsport Ontology & Semantic Web Querying

A semantic web project building an OWL ontology for the motorsport domain, populating it from DBpedia and querying it with SPARQL.

## Summary

This project defines an OWL ontology for the motorsport domain in Protégé 5.5.0, with classes such as Category, Events, Genre, Industry, Occupation and Service. `basic.py` runs a SPARQL CONSTRUCT query against the public DBpedia endpoint through SPARQLWrapper and merges the results with the ontology in an rdflib graph, saved as `car_basic.owl`. `query_basic.py` then queries that graph with SPARQL SELECT in Python.

**Honest framing:** the query scripts build on lab-provided starter/template code for connecting to and querying SPARQL endpoints. The original contribution is the motorsport ontology design itself (`car.owl` / `car_basic.owl`), plus the specific queries built on top of the template to explore it.

## Tech stack

- Python
- `rdflib` / `SPARQLWrapper` for RDF handling and SPARQL queries
- OWL (Web Ontology Language) for ontology definition
- Protégé for ontology design and editing
- DBpedia as the public linked-data SPARQL endpoint

## What's in this repo

| File | Description |
|---|---|
| `car.owl` / `car_basic.owl` | The motorsport ontology definitions |
| `basic.py` | Runs a SPARQL CONSTRUCT against DBpedia and merges the results with `car.owl` into `car_basic.owl` |
| `bonus.py` | An attempted second source (LinkedMDB). That endpoint has been offline for years, so the query is switched off and the script only prints a note |
| `query_basic.py` | Loads `car_basic.owl` into an RDFlib graph and runs a SPARQL SELECT that pulls distinct genre and service pairs for `Motorsport` individuals, grouped by genre, printing the results as a formatted table |
| `car.properties` / `car_basic.properties` | Protégé-generated config. No credentials, just blank templates |

## How to explore

```bash
git clone https://github.com/semilhalani/motorsport-ontology.git
cd motorsport-ontology
pip install -r requirements.txt
python basic.py
```

To view or edit the ontology itself, open the `.owl` files in [Protégé](https://protege.stanford.edu/).

## Key technical decisions

The ontology is structured as 10 classes: `Category`, `Events`, `Genre`, `Industry`, `KnownFor`, `Occupation`, `Purpose`, `Service`, `Union`, and the top-level `Motorsport`. All 9 are subclasses of `Motorsport`. There are 9 object properties (`isGenreOf`, `hasUnion`, `isServiceOf`, and others) linking these classes, and 5 data properties (`first`, `name`, `region`, `olympic`, `firstlabel`) capturing literal attributes.

Object properties were individually characterized rather than left as generic links. For example, `isGenreOf` was asserted as asymmetric, since a Motorsport instance can be a genre of something but not the reverse. It was also set as the inverse of `hasGenre`, so the reasoner could infer the reverse relationship automatically instead of it being asserted twice.
