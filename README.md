# Read Me

## OMC-JSON
The OMC-JSON folder contains all materials related to the OMC-JSON schema

**OMC-JSON-v2.6.schema.json**:The OMC schema itself

**/Docs**: Supplementary documentation including schema documentation and tech notes giving guidance on how to use the OMC and OMC-JSON schema.

The documentation is split into two sections, a set of documents that outline the basic structure and practices we used to guide the schema development, and a set of tech notes focussed on specific concepts and how to use them.

Overview
1. [Introduction](OMC-JSON/Docs/Overview/Introduction.md) 
2. [Schema Structure](OMC-JSON/Docs/Overview/SchemaStructure.md)
3. [Schema Practices](OMC-JSON/Docs/Overview/SchemaPractices.md)
4. [Schema Versioning](OMC-JSON/Docs/Overview/SchemaVersioning.md)

Tech Notes
1. [Narrative & Production](OMC-JSON/Docs/Tech-Notes/NarrativeProduction.md)
2. [Functional & Structural](OMC-JSON/Docs/Tech-Notes/FunctionalStructural.md)
3. [Assets](OMC-JSON/Docs/Tech-Notes/Assets.md)
4. [Relationships](OMC-JSON/Docs/Tech-Notes/RelationshipContext.md)
5. [Depictions & Portrayals](OMC-JSON/Docs/Tech-Notes/DepictionPortrayal.md)
6. [Versions](OMC-JSON/Docs/Tech-Notes/Version.md)
7. [Relationship Appendix](OMC-JSON/Docs/Tech-Notes/RelationshipAppendix.md)

Schema Documentation
1. [Introduction](OMC-JSON/Docs/Schema/Introduction.md)
2. [root](OMC-JSON/Docs/Schema/core/root.md)

**/Examples**: A set of example OMC-JSON files, these will validate against the schema and demonstrate the structure and concepts.

## OMC-RDF
The RDF in this repo is currently v2.0. The schema is divided into three files:

- cw.ttl is the basic Creative Work. The namespace is [https://mc.movielabs.com/cw](https://mc.movielabs.com/rdf/cw_v1.2.ttl) and it uses cw: as its prefix. A Creative Work is a uniquely identified production.  (See [Part 6: Creative Works](https://mc.movielabs.com/docs/ontology/creative-works/introduction))

  - cw:CreativeWork is the base class for Creative Work, and is declared to be equivalent to the (empty)  omc:CreativeWork using ‘owl:equivalentClass omc:CreativeWork’
  - cw: has structures for episodic content and edits based on the model used by [EIDR](https://www.eidr.org/technology/).
  - cw.ttl includes omc.ttl

- omc.ttl is the Ontology for Media Creation and covers the production process for Creative Works. The     namespace is [https://mc.movielabs.com/omc](https://mc.movielabs.com/rdf/omc_v1.2.ttl) and it uses omc: as its prefix.

- omd.ttl is the Ontology for Media Distribution, covering distribution channels, consumption metrics, and some kinds of marketing information such as awards, reviews, and ratings. The namespace is [https://mc.movielabs.com/omd](https://mc.movielabs.com/rdf/omd_v1.2.ttl) and it uses omd: as its prefix. It includes CW (and hence OMC).

  OMD is a *connected ontology* as defined in [*Part 1: Overview*](https://mc.movielabs.com/docs/ontology/overview/introduction).

  ***NOTE***: *OMD is in pre-release, and subject to change.*

These three files are used to generate two sets of self-contained HTML documentation pages, one for OMC (including CW) and one for OMD (including OMC and CW). The HTML documentation shows many of the object properties of a class in a diagram; however, not all relationships are shown that way, so it is important to look at the References section on each page as well.

The generated documentation is included in this repo as two zip files, one for OMC and one for OMD. Browsable versions are available online for [OMC](https://movielabs.com/prodtech/omc/v2.0/omcDoc/) and [OMD](https://movielabs.com/prodtech/omc/v2.0/omdDoc/)

### Structure

The OMC-RDF folder contains all materials related to the OMC RDF schema

**tentativePropertiedAdded.txt**: Properties in the omcT: namespace

**releaseNotes.txt**: release notes for the 2.0 and 2.5 releases.

**[Functional And Structural Classes in RDF](./OMC-RDF/RDFFunctionalStructural.md)**

**[Points and Matrices in RDF](./OMC-RDF/RDFPointMatrix.md)**

**[Known Bugs and Issues](OMC-RDF/KnownBugsIssues.md)**

**/OntologyMediaCreation-OMC**: The OMC ontology, containing the current schema, with previous revisions in **OntologyMediaCreation-OMC/previous**

**/OntologyMediaDistribution-OMD**: The OMD ontology, containing the current schema, with previous revisions in **OntologyMediaDistribution-OMD/previous**

**/CreativeWorks-CW**: The CW ontology, containing the current schema, with previous revisions in **CreativeWorks-CW/previous**

### Notes

- Most distribution-oriented concepts have been moved from cw: into omd: (e.g. different release titles and consumption metrics) but there are still a few left (e.g. cw:Genre and cw:Franchise.)

- The names of relationships (the predicates in the RDF triples) are taken from [Part 7: Relationships](https://mc.movielabs.com/docs/ontology/relationships/introduction) for most object properties. Some relationship names are in the omcT: namespace and are subject to change. If they do change, the omcT:  name will be retained for backwards compatibility.
- The datatype properties that are present are based on the names of attributes in the larger documentation set.
- Not all property names (relationships, in the parlance of the overview documents) have a skos:prefLabel declared; this will be fixed in future releases.

## **FAQs**

**What's happening with the original 2018 Creative Works Ontology?**

The Creative Works Ontology was the result of a working group focused on distribution and analytics. Much of the thinking about the basic Creative Work has been retained in the new model. OMC builds off of the revised Creative Work on the production side, and OMD moves the distribution and analytics model into a connected ontology, rather than being completely standalone. Information captured during production is often lost and has to be re-created, the connected ontologies make it easier to carry it forward to distribution. We encourage you to migrate from the original 2018 CW to the new ontologies, but the original 2018 CW is still available for reference.

When we refer to a Creative Work in OMC, it refers to the Creative Work as defined in [*Part 6: Creative Works*](https://mc.movielabs.com/docs/ontology/creative-works/introduction). Formal documentation for OMD will be published as an Annex to Part 6: Creative Works.

**Why are some things classes rather than more traditional relationships?**

For example, the ontology defines a class called 'Anything with a Name' and makes various other classes subclasses of it. In a pure RDF world, this could just as well be managed with a relationship or reified relationship. However, the model described by the ontology has to implementable using other common technologies, such as JSON, where subclassing and composition are more natural. For that reason, we use relationships for things that are conceptually connections between different things, and a small number of sub-classable things for information that is more closely related to the object itself (such as a name or an identifier).

**Why are there more data properties in the JSON than in the TTL, and in OMD than OMC?**

One of the main goals of the working groups that produced the ontology was to understand and model a framework for creative works and their production and distribution. To that end, we spent more time on the concepts themselves and their relationships to each other. The data properties of top-level concepts are generally things that are so essential to the definition or so prevalent in similar systems that they are relatively non-contentious. We will continue to add the data properties used by real-world applications (both RDF and JSON) as they are developed. OMD is based on the 2018 Creative Works Ontology, which has been around for a while now, and there is a body of implementation practice from which to draw

## License

All files in this repository are Copyright 2021-2023 Motion Picture Laboratories, Inc. and made available under the Apache 2.0 license provided in the [LICENSE](./LICENSE.txt) file.
