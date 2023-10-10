# Schema Structure
Ontology for Media Creation (OMC) provides a conceptual and technical model for the production process, and is described [here](https://mc.movielabs.com/docs/ontology/). This model is implemented using RDF schema (OMC-RDF), which provides a useful degree of formality, especially for relationships and complex classes. JSON, of course, can also be used for data modelling, but it has different mechanics for classes, properties, and types, and less emphasis on relationships than RDF.

The OMC-JSON schema retains the vocabulary, concepts, and top-level structures of the OMC-RDF, although some changes are necessary to support expressing the details of the concepts in JSON. In particular, the OMC-JSON schema provides mechanisms for encoding relationships (in the RDF sense) and a compositional model rather than classes and inheritance.

## Key Concepts
There are three pervasive concepts in the OMC-JSON schema:

- Entities
- Identifiers
- Relationships

## Entities
An entity represents one of the core concepts in OMC, things like Character, Asset and Participant. RDF is a class-based system, so in OMC-RDF these are represented as classes and sub-classes. JSON does not use a class-based model or the idea of class inheritance. Therefore, in OMC-JSON we use a compositional model. The schema is comprised of individual sub-schemas (each entity has a sub-schema) which can then be composed to describe the core concepts of OMC and broadly align with the RDF classes.
> **Entity**: A top level concept in the ontology that includes a set of properties with associated values and its relationships to other entities.
> 
> **Property**: A `<key> <value>` pair where the value can be a reference to another entity, a complex type (object or array of objects), or a primitive value (string, number, Boolean or null).
> 
## Identifiers
Identifiers are used liberally in the ontology, so it is important to develop a good understanding of the concept. Each entity is required to be uniquely identified within a declared scope, and entities are related to one another using their identifier.

It is worth noting that entities can have multiple identifiers, common when same thing exists in multiple systems. For example, the same Person may exist in an HR system, payroll system, security system, and production system. Each system likely has its own identifier, and by retaining all the identifiers for each system, there is an understanding they all refer to the same 'thing', for example a person.

An identifier consists of a value and scope; the value should be unique within a given scope. OMC is designed as an interchange standard, allowing data about things to be exchanged and synchronized across different systems. This is why knowing the scope is essential - the universe within which the identifier is valid and unique. For example, "42" is a perfectly good identifier, but without knowing the scope, there is no way of knowing what it represents, as many systems likely use “42” as an identifier. See [OMC Part 9: Utilities](https://mc.movielabs.com/docs/ontology/utilities/introduction/) for further details, including some meanings of "42".

The `identifier` property, is required on all entities. It is an array, and `identifierScope` and `identiferValue` are required.

OMC-JSON
```
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

- When another entity is an intrinsic property of an entity, then the property value will either be a reference to the entity or some, or all, of the properties of entity itself.
- Relationships to entities that are not intrinsic properties are expressed in a Context property.

For a more detailed explanation read the section on [Relationships & Context](../Tech-Notes/RelationshipContext.md)

When an intrinsic property is another entity, the name of the property is often that entity type. The property name uses pascal case (first letter capitalized).

The example below shows a Narrative Location. It has the intrinsic properties `Location` and `Context` which carry the identifier for a Location and a Context. To examine the properties of these entities they need to be resolved; this may be done in a separate operation by the consuming party or by de-referencing in-line [see below](#de-referencing-identifiers).

OMC-JSON
```JSON
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
Some entities, such as Asset and Participant, allow grouping. In OMC-JSON they are represented as a top-down hierarchy, with one entity nested inside another. In OMC-RDF an entity is a `memberOf` its parent entity (the group). In OMC-JSON the relationship name is inferred, and the consuming application is free to recreate the graph in both directions if it so desires.

OMC-JSON
```JSON
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
As well as being able to just provide a reference, OMC allows flexibility to de-reference any or none of the identifiers for properties of an entity. When referencing another entity by only including an identifier, it is left to the consuming party to make a request for the details of that entity. The producers of any payload can decide what they want to include, allowing payloads to be tailored to specific use cases.

Which method is used (identifier vs de-referenced entity) will differ across applications and workflows based on things like latency, availability of data or identifier resolution, caching behavior in applications, etc. It is always possible to send de-referenced data for any entity to any depth, but caution should be exercised when considering the size of the payload, especially given that it is graph-based.

The example below shows a Narrative Location, where the Location itself is only referenced by its identifier. A client receiving this payload could then make a request using the Location's identifier to retrieve the full set of attributes if it needs them.

OMC-JSON - Location as a reference only
```JSON
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
```JSON
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

When only a reference is included the consuming party may need to make a follow up request for additional information. This can present some potential issues: a decoupled system may not know which application prepared the payload and the consumer will need to know API endpoints, have required credentials, etc., to acquire additional data. Sometimes, all that a particular application wants is an identifier so it can anchor the portions of the graph it cares about in a broader structure, in which case the identifier doesn't need to be de-referenced.

## Sub-Classing
JSON does not support the concept of classes, and by extension, sub-classing, something the OMC-RDF model uses extensively. Therefore OMC-JSON uses a `type` property on some entities that allow the sub-class to be expressed. This helps manage the scale of the schema, by not requiring every sub-class to be expressed as its own entity.

For example, in OMC-RDF a parent class of NarrativeObject has various sub-classes: NarrativeProp, NarrativeSetDressing, NarrativeGreenery, etc. In OMC-JSON, the top-level class is the entity type (NarrativeObject) and a property `narrativeType` indicates the sub-class or type.

```JSON
    {
        "NarrativeObject": {
            "entityType": "NarrativeObject",
            "narrativeType": "prop"
        }
    }
```

We use a similar mechanism for Asset `functionalType` and `structuralType` for entities that have structural and functional characteristics.

## Reification
Reification is technique which we use to bundle up relationships between two entities into an entity itself. This allows us to pass around and reuse those relationships multiple times. This technique is used in several places throughout OMC, but most notably in entities like Depiction and we use partial Reification in Contexts which are used bundle up relationships into useful groupings.

For more details and examples see the sections on [Relationships & Context](../Tech-Notes/RelationshipContext.md) and [Depictions & Portrayals](../Tech-Notes/DepictionPortrayal.md)

## Standard Entity Properties
There are some properties that are used consistently throughout the schema:

**schemaVersion (required)**

Defines the version of the schema that was used to encode the instance.
This allows parsers to understand the structure and nature of the properties in the entity.

**entityType (required**

A required property that enumerates the type of the entity.
A client receiving the OMC-JSON payload will know what any given entity is, so that it can parse it correctly.

**identifier (required)**

The identifier, or identifiers uniquely identify this entity within the described scope.
An entity can have multiple identifiers. For example a Creative Work may have an identifier with the production company's ID, the studio's ID, an IMDb ID, or an EIDR ID.

**name**

A human readable name for the entity.
This can be helpful for clients consuming the data, such as applications that need something like a label or tag for a UI. There is no requirement that it be unique and this should not be used as something canonical. Entities that need a canonical name (like Person or Location) will have a formal name property.

**description**

A human readable (preferably short) description of the entity. As with name, this is really meant for human consumption and should not be used for encoding structured information.

**customData**

The schema does not attempt to define every property that you might associate with any given entity. Our goal is to surface enough to allow a production to track, relate, and find things across distinct parts of the workflow.

See [Schema-Practices](./SchemaPractices.md) for more information.

<!--
Copyright 2021-2023 Motion Picture Laboratories, Inc.
SPDX-License-Identifier: APACHE-2.0
-->
