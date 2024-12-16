# Functional & Structural
OMC uses a mechanism on several entity types to differentiate what we call an entity’s functional and structural characteristics. Structural characteristics describe its underlying nature, i.e., what it is, and functional characteristics describe how it is used.

It is useful to separate these two concepts because sometimes one thing can be used for more than one purpose, and something with the same functional purpose can have more than one form. Some parts of the workflow care more about what something is, some care more about what it does, and some care about both.

Assets and Participants each have structural and functional characteristics. It is not always necessary for an entity to have both characteristics; sometimes it may just have one. There is also no requirement or necessity that an entity has specific properties; sometimes just declaring its type is enough.

*Note: Tasks and Infrastructure also have structural and functional properties, but these will be covered in a future release.*

**Structural & Functional Types**

The ontology does not formally declare or impose a set of enumerated values for naming the functional and structural types. There are a lot of these, and we expect this list will evolve over time, as well as some being specific to a particular production. However, in the interest of a common understanding we are developing a set of preferred or suggested terms for many commonly used structural and functional types, some of which are already part of OMC.

In OMC-RDF the structural and functional characteristics are classes and sub-classes. In OMC-JSON they are expressed through the `structuralType` or `functionalType` property of the structural or functional characteristics.

In OMC-JSON for the Participant and Assets functional characteristics we have made this a simple property of the entity. It is not a reference to another entity and therefore does not require an identifier.

The naming convention for the types uses dot notation and camel case for each term. This can imply a hierarchical naming structure, which is mostly followed. However, there is an inevitable discussion as to whether something is a digital.image, or an image.digital. There is no right answer but establishing an agreed order can help parsers. We also consider the strings to be splittable, and the individual terms can be used for categorization.

The sections below show some examples.

**Structural & Functional Properties**

Along with a structural or functional type there may also be a set of properties that further describe the nature of the entity, these help further define the exact nature of the essence.

For example, a blob of data would structurally be `digital.data`. If that data had two representations, XML and JSON, then including a property describing it’s mimetype would differentiate the two and allow the correct representation to be selected for a given application.

The schema currently has a very limited set of definitions for structural and functional properties, future work will look to expand this for a set of properties, although the expectation is custom properties will be need, for which the [customData](../Schema/Utility/Utility.md#customData) property exists.

## Assets
Asset entities are likely to be the vast majority of entities in any given production and will make up the bulk of the structural and functional types.

Following are two possible scenarios splitting the structural and functional characteristics and how they might evolve during production.

- A storyboard often starts life as a hand drawn sketch. Structurally this is a physical object, but once digitized it becomes a digital object, while still functionally being the same thing, a storyboard. The structural properties of the two objects will be different, i.e., the physical drawing has a physical location or dimensions in inches, whereas the digital object is more likely to be held in cloud storage with dimensions in pixels.
- Digital images share many of the same structural properties, such as size, color depth, and encoding. However, their functional uses can vary dramatically and are independent of these attributes. They may be textures for a 3D model, concept artwork, technical reference material, continuity photos, etc. A single image (essence) may be more than one of those things in different parts of the workflow: i.e., a technical reference photo may become a texture at some point.

The following example shows an Asset.

- The functional characteristics have a type of `artwork.storyboard.frame`, which describe its purpose. Additional `functionalProperties`, can be used to convey additional information.
- The structural characteristics (AssetSC) has a type of `digital.image` and some example `structuralProperties` are shown.

OMC-JSON: Asset
```JSON
{
  "entityType": "Asset",
  "identifier": [
    {
      "identifierScope": "labkoat",
      "identifierValue": "ast/Q5r4wyLeFY4CWYkp6-ZSp"
    }
  ],
  "name": "water",
  "description": "Rough water wondering if Sven makes the surface",
  "AssetSC": {
    "identifier": [
      {
        "identifierScope": "labkoat",
        "identifierValue": "astsc/8bb0yQX3cgN4AvaKRw8Yi"
      }
    ]
  },
  "assetFC": {
    "functionalType": "artwork.storyboard.frame",
    "functionalProperties": {
      "cameraFraming": "Wide"
    }
  }
}
```
OMC-JSON: AssetSC
```JSON
{
  "entityType": "AssetSC",
  "identifier": [
    {
      "identifierScope": "labkoat",
      "identifierValue": "astsc/8bb0yQX3cgN4AvaKRw8Yi"
    }
  ],
  "structuralType": "digital.image",
  "structuralProperties": {
    "linkset": {
      "recordType": "item",
      "mediaType": "image/jpeg"
    },
    "fileDetails": {
      "fileExtension": "jpeg",
      "fileName": "storyboard_beach_water.jpeg"
    },
    "dimensions": {
      "width": "8064px",
      "height": "6048px"
    }
  }
}
```    
**Example Structural Types**
```
digital.image
physical.image
digital.movingImage
digital.structuredDocument
```
**Example Functional Types**
```
artwork.storyboard
artwork.storyboard.frame
capture.video.ocf
video.debayered
proxy.daily
proxy.editorial
capture.audio
capture.audio.track
capture.audio.onSetMix
audio.stem
```
See [Assets](./Assets.md) for more detailed examples and descriptions.

## Participants
Following are two possible scenarios splitting the structural and functional characteristics of a Participant.

- During pre-production it is often known that people will need to be hired to fulfill certain roles on the production; however, the specific individuals may not have selected or hired. A Participant with the appropriate Role can be created with no structural characteristics. The Participant entity can be related to other entities, Depiction, ProductionScene, etc. This allows for planning things like scheduling and budgeting and when a Person is identified, they are added as the structural characteristics.
- A Person may fulfil multiple roles on a Production, e.g., actor and director. The same Person can be related to different Participants each with the appropriate Role. The actor Participant is then related to other parts of the production appropriately, i.e. to costumes, props, scenes they appear in, the director likewise. Each can be managed within the appropriate scope.

The following example shows a Participant:
- The Participant’s structural characteristics are related to a Person entity, which describes the properties specific to that Person only.
- The Participant’s functional characteristics carry details about the Roles this Participant carries out on the production.

OMC-JSON: Participant
```JSON
{
  "entityType": "Participant",
  "identifier": [
    {
      "identifierScope": "labkoat",
      "identifierValue": "ptc/X_jT_v3bnC5_mdT8WyJ56"
    }
  ],
  "name": "John Rene",
  "description": null,
  "ParticipantSC": {
    "identifier": [
      {
        "identifierScope": "labkoat",
        "identifierValue": "ptsc/MFlCPsgmu_5xPCpQp7gGH"
      }
    ]
  },
  "participantFC": {
    "functionalType": "writer",
    "Role": [
      {
        "identifier": [
          {
            "identifierScope": "labkoat",
            "identifierValue": "rol/zMHMDLktboZFV4Q9l0637"
          }
        ]
      }
    ]
  }
}
```

OMC-JSON: Person
```JSON
{
  "entityType": "Person",
  "identifier": [
    {
      "identifierScope": "labkoat",
      "identifierValue": "ptsc/MFlCPsgmu_5xPCpQp7gGH"
    }
  ],
  "structuralType": "person",
  "name": "John Rene",
  "description": null,
  "personName": {
    "firstGivenName": "John",
    "familyName": "Rene"
  },
  "contact": {
    "email": {
      "business": "rene@labkoat.media"
    },
    "telephone": {
      "business": "213-555-0161"
    }
  }
}
```
OMC-JSON: Role
```JSON
{
  "entityType": "Role",
  "identifier": [
    {
      "identifierScope": "labkoat",
      "identifierValue": "rol/zMHMDLktboZFV4Q9l0637"
    }
  ],
  "roleType": "screenWriter"
}
```

**Example Structural Types**
```
person
department
organization
service
```
**Example Functional Types**
```
director
actor
actor.stunt
actor.voiceover
camera (department)
art (department)
```
See [Participants](./Participant.md) for more detailed examples and descriptions.

## Task
OMC-JSON currently has a placeholder entity for Task.

*Note: Development of the details including its functional and structural characteristics will be in later revisions of the schema.*


## Infrastructure
OMC-JSON currently has a placeholder entity for Infrastructure. 

*Note: Development of the details including its functional and structural characteristics will be in later revisions of the schema.*

<!--
Copyright 2021-2023 Motion Picture Laboratories, Inc.
SPDX-License-Identifier: APACHE-2.0
-->
