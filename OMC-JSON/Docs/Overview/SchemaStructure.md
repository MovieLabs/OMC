# Schema Structure

Ontology for Media Creation (OMC) provides a conceptual and technical model for the production process, and is described [here](https://mc.movielabs.com/docs/ontology/). This model is implemented using RDF schema (OMC-RDF), which provides a useful degree of formality, especially for relationships and complex classes. JSON, of course, can also be used for data modelling, but it has different mechanics, properties and types, and no inherent representation for classes or relationships.  This is a change request.

The OMC-JSON schema retains the vocabulary, concepts, and top-level structures of the OMC-RDF, although some changes are necessary to support expressing the details of the concepts in JSON. In particular, the OMC-JSON schema provides mechanisms for encoding relationships (in the RDF sense) and uses a compositional model rather than classes and inheritance.



<figure><img src="../Diagrams/Narrative-1.svg" alt=""><figcaption><p>This is an image</p></figcaption></figure>

## Key Concepts

There are three pervasive concepts in the OMC-JSON schema:

* Entities
* Identifiers
* Relationships

## Entities

An entity represents one of the core concepts in OMC, things like Character, Asset and Participant. RDF is a class-based system, so in OMC-RDF these are represented as classes and sub-classes. JSON does not use a class-based model or the idea of class inheritance, in OMC-JSON we use a compositional model. The schema is comprised of individual sub-schemas which are then composed to describe the core concepts of OMC and broadly align with the RDF classes.

> **Entity**: A top level concept in the ontology that includes a set of properties with associated values and its relationships to other entities.
>
> **Property**: A `<key> <value>` pair where the value can be a reference to another entity, a complex type (object or array of objects), or a primitive value (string, number, Boolean or null).

## Identifiers

Identifiers are used liberally in the ontology, so it is important to develop a good understanding of the concept. Each entity is required to be uniquely identified within a declared scope, and entities are related to one another using their identifier.

It is worth noting that entities can have multiple identifiers, common when the same thing exists in multiple systems. For example, the same Person may exist in an HR system, payroll system, security system, and production system. Each system likely has its own identifier, and by retaining all the identifiers for each system, there is an understanding they all refer to the same 'thing', in this case the same person.

An identifier consists of a value and scope; the value should be unique within a given scope. OMC is designed as an interchange standard, allowing data about things to be exchanged and synchronized across different systems. This is why knowing the scope is essential - the universe within which the identifier is valid and unique. For example, "42" is a perfectly good identifier, but without knowing the scope, there is no way of knowing what it represents, as many systems likely use “42” as an identifier. See [OMC Part 9: Utilities](https://mc.movielabs.com/docs/ontology/utilities/introduction/) for further details, including some meanings of "42".

The `identifier` property, is required on all entities. It is an array, and `identifierScope` and `identiferValue` are required.

OMC-JSON

```json
{
  "identifier": [
    {
      "identifierScope": "labkoat",
      "identifierValue": "ptc/3AE1ybCWJXJFxKhWhF0qd"
    }
  ]
}
```

URLs can be used as identifiers but can be fragile in complex production systems: things can move or exist in more than one location. A `file:` URL can be used as an identifier, but this can make workflows fragile, since even a shared filesystem can be mounted at different mount points on different systems.

The 2030 vision proposes the use of a resolution mechanism for identifiers. A resolver can be used for retrieving files and/or additional data. When an identifier is resolved with a resolver, the response is one or more URLs that can then be used to retrieve information.

For more information on resolvers, see here: [Through the Looking Glass](https://movielabs.com/through-the-looking-glass/)

## Relationships

An ontology creates a graph of related entities. How things are related is as important as the things themselves. The relationships in OMC are created by referencing another entity using its identifier. The name of the relationship (in graphs called an edge) can carry semantic meaning, describing the nature of the relationship.

In OMC-JSON, there are two common situations where you may wish to express the relationship between two entities by referencing the other.

* When another entity is an intrinsic property, then the property value can contain just reference (it's identifier) to the entity. Alternatively OMC-JSON also allows for the entity to be dereferenced, meaning its properties and values may be embedded inline. This second method allows a single JSON object to contain the data for multiple related entities, avoiding the recipient having to retrieve or reconstruct this themselves.
* Relationships to entities that are not intrinsic properties are contained in a Context. Most entities have Context as one of its intrinsic properties.

For a more detailed explanation read the section on [Relationships & Context](../Tech-Notes/RelationshipContext.md)

When an intrinsic property is another entity, the property name is often the entity type it references, but not always. However, intrinsic properties always use pascal case (first letter capitalized).

The example below shows a Narrative Location. It has the intrinsic properties `Location` and `Context`. The value is an identifier for the Location and Context respectively. To examine the specific properties of these entities they need to be resolved; this is typically a separate operation by the consuming party, [see below](SchemaStructure.md#de-referencing-identifiers).

OMC-JSON

```json
    {
      "entityType": "NarrativeLocation",
      "identifier": [
        {
          "identifierScope": "labkoat",
          "identifierValue": "loc/50DwTikSnhJViFrABXvGF"
        }
      ],
      "name": "Beach",
      "description": "Sandy beach leading into jungle on coastline",
      "Location": {
        "identifier": [
          {
            "identifierScope": "labkoat",
            "identifierValue": "loc/hfl4390vjhqwp0suf32f"
          }
        ]
      },
      "Context": [
        {
          "identifier": [
            {
              "identifierScope": "labkoat",
              "identifierValue": "cxt/6mZcMvDTYRQnfwQOH2GcA"
            }
          ]
        }
      ]
    }
```

## Grouping

Some entities, such as Asset and Participant, allow grouping. In OMC-JSON they are represented as a top-down hierarchy, with one entity nested inside another. In OMC-RDF an entity is a `memberOf` its parent entity (the group). In OMC-JSON intrinsic relationship names are inferred, the consuming application is free to recreate the graph in both directions if it so desires.

OMC-JSON

```json
{
    "entityType": "Asset",
    "identifier": [{
        "identifierValue": "1234",
        "identifierScope": "Movielabs"
    }],
    "Asset": [
    {
      "identifier": [
        {
          "identifierScope": "Movielabs",
          "identifierValue": "1-ABCD"
        }
      ]
    },
    {
      "identifier": [
        {
          "identifierScope": "movielabs",
          "identifierValue": "2-ABCD"
        }
      ]
    }
  ]
}
```

## De-Referencing Identifiers

In addition to providing a reference, OMC allows flexibility to de-reference any or all identifiers for the properties of an entity. When referencing another entity by including only an identifier, it is up to the consuming party to request the details of that entity. The producers of any payload can decide what to include, allowing payloads to be tailored to specific use cases.

The choice between using an identifier or a de-referenced entity will vary across applications and workflows based on factors such as latency, data availability, identifier resolution, caching behavior in applications, etc. It is always possible to send de-referenced data for any entity to any depth, but caution should be exercised regarding the size of the payload, especially since it is graph-based.

The example below shows a Narrative Location, where the Location itself is referenced only by its identifier. A client receiving this payload would then need to request the full set of attributes using the Location’s identifier if needed.

OMC-JSON - Location as a reference only

```json
{
  "entityType": "NarrativeLocation",
  "identifier": [
    {
      "identifierScope": "labkoat",
      "identifierValue": "loc/50DwTikSnhJViFrABXvGF"
    }
  ],
  "name": "Beach",
  "description": "Sandy beach leading into jungle on coastline",
  "Location": {
    "identifier": [
      {
        "identifierScope": "labkoat",
        "identifierValue": "loc/hfl4390vjhqwp0suf32f"
      }
    ]
  }
}
```

The next example shows a full Location entity de-referenced and included directly in the payload.

OMC-JSON - Location de-referenced inside the payload

```json
    {
      "entityType": "NarrativeLocation",
      "identifier": [
        {
          "identifierScope": "labkoat",
          "identifierValue": "loc/50DwTikSnhJViFrABXvGF"
        }
      ],
      "Location": {
          "entityType": "Location",
          "identifier": [
            {
            "identifierScope": "labkoat",
            "identifierValue": "loc/hfl4390vjhqwp0suf32f"
            }
          ],
          "name": "Sherlock Holmes' residence",
          "address": {
              "street": "221b Baker St.",
              "region": "London",
              "postalCode": "NW1 6XE",
              "country": "uk"
          }
      },
      "description": "Sherlock Holmes' residence"
    }
```

When only a reference is included the consuming party may need to make a follow up request for additional information. This can present some potential issues: a decoupled system may not know which application prepared the payload and the consumer will need to know API endpoints, have credentials, etc., to acquire additional missing data. Sometimes, all that a particular application wants is an identifier so it can anchor the portions of the graph it cares about in a broader structure, in which case the identifier doesn't need to be de-referenced.

## Sub-Classing

JSON does not support the concept of classes, and by extension, sub-classing, something the OMC-RDF model uses extensively. To represent sub-classes OMC-JSON uses a `...Type` property on some entities, allowing the sub-class to be expressed. This helps manage the scale of the schema, by not requiring every sub-class to be expressed as its own entity and sub-schema.

For example, in OMC-RDF a parent class of NarrativeObject has various sub-classes: NarrativeProp, NarrativeSetDressing, NarrativeGreenery, etc. In OMC-JSON, the top-level class is the entity type (NarrativeObject) and a property `narrativeType` indicates the sub-class or type.

```json
    {
        "NarrativeObject": {
            "entityType": "NarrativeObject",
            "narrativeType": "narrativeProp"
        }
    }
```

The `types` are typically expressed as an enumerated set of values, there is often a value that represents the top-level class in case one of the sub-classes is not applicable.

> `...Type` is not generally a required value, but it is considered best practice to always include it.
>
> Sometimes a `...Type` property exists even when there are no sub-classes, this is there for possible later extensions, and it is still considered best practice to include it, even though it is duplicative information.

We use a similar mechanism for `functionalType` and `structuralType` for entities like Assets that have structural and functional characteristics.

## Reification

Reification is a technique to encode a relationship between entities in such a way that it is it's own entity. This allows properties to placed onto the relationship itself and allows these relationships to be reused multiple times. This technique is employed in several places throughout OMC, a Depiction and Participant are examples. We also utilize the same concept for Contexts, where multiple relationships may be bundled together.

For more details and examples see the sections on [Relationships & Context](../Tech-Notes/RelationshipContext.md) and [Depictions & Portrayals](../Tech-Notes/DepictionPortrayal.md).

## Standard Entity Properties

Almost all entities utilize a `baseEntity` sub-schema. This provides a core set of properties that are included on all entities. Technically a union is created between the `baseEntity` sub-schema and the sub-schema specific to a given entity, for those more familiar with class inheritance it is functional equivalent to the entity inheriting the `baseEntity` class.

A similar pattern is used for the version property, where version properties specific to an entity type are composed with the `baseVersion` schema.

**`schemaVersion` (required)** Declares the version of the OMC-JSON schema that was used to encode the instance. This allows parsers to understand the structure and nature of the properties in the entity.

**`identifier` (required)** The identifier, or identifiers uniquely identify this entity within the described scope. An entity can have multiple identifiers. For example a Creative Work may have an identifier with the production company's ID, the studio's ID, an IMDb ID, or an EIDR ID.

**`entityType` (required)** A required property that enumerates the type of the entity, it is always a `const` matching the name of the entity.

A consumer of OMC-JSON can use this to determine how to parse it correctly.

**`name (best practice)`** A human readable name for the entity.

This is primarily intended for things like UI's or someone who is examining a payload.

It should not be considered canonical. For entities that actually have 'names' as properties, like a Person or Character there will be a property where the canonical value should be included (even if they are the same).

**`description (best practice)`** A human readable (preferably short) description of the entity.

As with name, this is primarily for human consumption and should not be used for encoding structured information.

Other properties are detailed in [baseEntity](../Schema/core/baseEntity/) schema definition.

See [Schema-Practices](SchemaPractices.md) for more information.
