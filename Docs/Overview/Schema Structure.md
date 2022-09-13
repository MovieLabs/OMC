# JSON Schema Overview

OMC is written in RDF, which provides a useful degree of formality, especially for relationships and complex classes. JSON, of course, can also be used for data modelling, but it has different mechanics for classes, properties, and types, and less emphasis on relationships than RDF.

The JSON schema retains the vocabulary, concepts, and top-level structures of the RDF, although some changes are necessary to support expressing the details of the concepts in JSON. In particular, the JSON schema provides standard mechanisms for relationships (in the RDF sense) and complex classes.

## Key Concepts

There are three pervasive concepts in the JSON schema:

- Entities
- Identifiers and references
- Relationships

### Entities
RDF is a class based system. JSON does not use a class based model or the idea of class inheritance.

For the JSON schema we use a compositional model, where a set of individual schemas are used to create entities that align with the RDF classes. These schemas can then be composed (via referencing) to create new entities. Each entity can be nested or included in sets.

Each entity requires a property of ``entityType``, knowing the entityType allows for applications to reference the correct schema when validating or a parsing function to act on the data.

**Entity**: A top level concept in the ontology that includes a set of properties with associated values.

**Property**: A ``<key> <value>`` pair where the value can be an entity, complex type (object or array of objects) or primative value (string, number, Boolean or null)

The schema follow some general conventions:
- Each entity is defined as its own JSON schema.
- The first letter of any defined entity is capitalized.
- Entities are required to declare their ``entityType`` and have a unique ``identifier``

Here is section of the schema for Narrative Location, which illustrates how the identifier subSchema is included by reference. The Location is itself an entity and therefore capitalized; it includes an identifier for for the Location ***(see Identifiers and references)*** and two attribute, a name and a description.

**JSON Schema**
```JSON
{
    "entityType": {
        "type": "string",
        "title": "Entity Type",
        "const": "NarrativeLocation"
    },
    "identifier": {
        "title": "identifier",
        "$ref": "../Utility/identifier.json#/properties/identifier"
    },
    "Location": {
        "$ref": "../Utility/Location.json"
    },
    "name": {
        "type": "string",
        "title": "Name"
    },
    "description": {
        "type": "string",
        "title": "Description"
    }
}
```

**JSON Instance**
```JSON
{
    "entityType": "NarrativeLocation",
    "identifier": [{
        "identifierValue": "1234",
        "identifierScope": "Movielabs"
    }],
    "Location": {
        "identifier": [{
            "identifierValue": "5678",
            "identifierScope": "Movielabs"
        }],
    },
    "name": "221B Baker Street - exterior"
    "description": "Sherlock Holmes' residence"
}
```



## Identifiers and References

### Identifiers
The example above used an identifier. In the ontology, an Identifier is "a string of characters that uniquely identifies an object within a particular scope." An identifier is really just a way of referring to something; undifferentiated strings and URIs/IRIs are common forms for an identifier, and there are many more specialized ones as well. 

For the production system (and any system that consists of multiple cooperating systems) it is essential to know the *scope* of the identifier - the universe within which the identifier is valid and unique. For example, "42" is a perfectly good identifier, but without knowing the scope, there is no way of knowing what it represents. See [OMC Part 9: Utilities](https://mc.movielabs.com/docs/omc/utilities/concepts) for further details, including some meanings of "42".

There is a JSON schema for an identifier/scope pair, as shown here, followed by an example of an instance.

**JSON Schema**
``` JSON
{
    "identifier": {
        "type": "array",
        "title": "identifier",
        "additionalItems": true,
        "items": {
            "type": "object",
            "required": ["identifierScope", "identifierValue"],
            "properties": {
                "identifierScope": {
                    "type": "string",
                    "title": "Identifier Scope",
                    "description": "The universe within which an identifier is valid and unique."
                },
                "identifierValue": {
                    "type": "string",
                    "title": "Identifier Value",
                    "description": "A string of characters that uniquely identifies an object within a particular scope."
                }
            },
            "additionalProperties": false
        }
    }
}
```

**JSON Instance**
```json
    {
        "identifier": [{
          "identifierValue": "1234",
          "identifierScope": "MovieLabs"
        }]
    }
```



### References
The use of identifiers is a central component of all entities; an entity must be uniquely identifiable with an identifier.

Using identifiers allows any entity to be included by reference or by inclusion; the decision is left to the application. Where only an identifier is included in a payload the presumption is the receiving party would make a follow up request to retrieve additional information.

The example below shows a Narrative Location, where the Location itself is only referenced by it's identifier. A client receiving this could then make a request using the Location's identifier to get the full set of attributes.

**JSON Instance, example 1**
```JSON
{
    "entityType": "NarrativeLocation",
    "identifier": [{
        "identifierValue": "1234",
        "identifierScope": "Movielabs"
    }],
    "Location": {
        "identifier": [{
            "identifierValue": "221B",
            "identifierScope": "LocationDB"
        }],
    },
    "description": "Sherlock Holmes' residence"
}
```

The next example shows how the Location entity can be de-referenced and included in the payload.

**JSON Instance, example 2**
```JSON
{
    "entityType": "NarrativeLocation",
    "identifier": [{
        "identifierValue": "1234",
        "identifierScope": "Movielabs"
    }],
    "Location": {
        "entityType": "Location",
        "identifier": [{
            "identifierValue": "221B",
            "identifierScope": "LocationDB"
        }],
        "name": "Sherlock Holmes' residence",
        "address": {
            "street": "221b Baker St.",
            "region": "London",
            "postalCode": "NW1 6XE"
            "country": "uk"
        }
    },
    "description": "Sherlock Holmes' residence"
}
```

The schemas are structured in such a way that objects could be nested *ad infinitum*, it is the decision of the sending and recieving applications to decide how and what is exchanged, however developers should be aware that given the graph based nature circular references can be easily created.

When the decision is made to pass just a reference it is likely that the recieving client may want to make a follow up request for additional information. This does raise some potential issues, a decoupled system may not even know which application prepared the data and the client will need to know API endpoints and have required credentials etc.

The 2030 vision also proposes the use of a resolution mechanism. A resolver can be used for both retrieving files and/or additional data. When an identifier is resolved with a resolver the response is one or more URL's that can then be used to retrieve information. ==For more on resolvers go here==

## Relationships
Relationships are a fundamental construct in the ontolgy.

There are not really standard mechansims for encoding relationships in JSON, we do not use JSONLD, so we have adopted the following patterns for referencing other entities. There are primarily two situations where you may wish to include references:
- When another entity is an intrinsic property of an entity
- When you wish to use a named relationship, typically as part of a Context

When another entity is an intrinsic property then the entity type to which you are refering is often the name of the property, this can be seen for Location in the example above. However, another name can be used, such as the propery ``source`` in a shot
```JSON
"functionalProperties": {
	"source": {
		"entityType": "Asset",
		"identifier": [{
		}]
	}
}

```


The Context entity demonstrates the use of named relationships, the following example shows how a NarrativeScene is related to entities such as props or characters that appear in that scene. This follows the pattern:

``<Context>.<relationship>.[<entity>]``

**JSON Schema**
```JSON
{
    "entityType": {
        "type": "string",
        "title": "Entity Type",
        "const": "NarrativeLocation"
    },
    "identifier": {
        "title": "identifier",
        "$ref": "../Utility/identifier.json#/properties/identifier"
    "name": {
        "type": "string",
        "title": "Name"
    },
    "description": {
        "type": "string",
        "title": "Description"
    }
	"Context": {  
	      "type": "object",  
	      "required": [  
	         "entityType",  
	         "identifier"  
	      ],  
	      "properties": {  
	         "entityInfo": {  
	            "title": "Entity Information",  
	            "$ref": "../Model/definitions.json#/properties/entityInfo"  
	         },  
	         "entityType": {  
	            "type": "string",  
	            "title": "Entity Type",  
	            "const": "Context"  
	         },  
	         "identifier": {  
	            "$ref": "../Utility/identifier.json"  
	         },  
	         "usesProp": {  
	            "type": "object",  
	            "title": "usesProp",  
	            "properties": {  
	               "NarrativeProp": {  
	                  "type": "array",  
	                  "items": {  
	                     "$ref": "../MediaCreationContext/NarrativeProp.json"  
	                  }  
	               }  
	            }  
	         },  
	         "features": {  
	            "type": "object",  
	            "title": "features",  
	            "properties": {  
	               "Character": {  
	                  "type": "array",  
	                  "items": {  
	                     "$ref": "../MediaCreationContext/Character.json"  
	                  }  
	               }  
	            }  
	         }
		 }
	   }  
	}
}
```

**JSON Instance**
```JSON
      {
        "entityType": "NarrativeScene",
        "identifier": [
          {
            "identifierScope": "labkoat",
            "identifierValue": "nscn/St_Hh-LxAQo4ICUAtbZ0v"
          }
        ],
        "name": "Space",
        "description": "Sven repairs satellite and is ambushed by Trilobot",
        "sceneNumber": "2",
        "Context": {
          "isFromScript": {
            "Asset": [
              {
                "entityType": "Asset",
                "identifier": [
                  {
                    "identifierScope": "labkoat",
                    "identifierValue": "ast/lHz-ua3XG-xQzDyCDbbKZ"
                  }
                ],
                "name": "mls_hsm_script_vshootingfd_2021_12_17_v004.pdf",
                "description": null,
                "structuralCharacteristics": {
                  "structuralType": "document",
                  "identifier": [
                    {
                      "identifierScope": "labkoat",
                      "identifierValue": "astsc/vxFhewUHgTpM78A4tm5TN"
                    }
                  ],
                  "structuralProperties": {
                    "linkset": {
                      "recordType": "item",
                      "mediaType": "application/pdf"
                    },
                    "fileDetails": {
                      "fileName": "mls_hsm_script_vshootingfd_2021_12_17_v004.pdf",
                      "filePath": "/1_pre-production/story",
                      "fileExtension": "pdf"
                    }
                  }
                },
                "functionalCharacteristics": {
                  "functionalType": "script"
                }
              }
            ]
          },
          "features": {
            "Character": [
              {
                "entityType": "Character",
                "identifier": [
                  {
                    "identifierScope": "labkoat",
                    "identifierValue": "chr/HNvHjXqJY9wv1IwjG-Hf1"
                  }
                ]
              },
              {
                "entityType": "Character",
                "identifier": [
                  {
                    "identifierScope": "labkoat",
                    "identifierValue": "chr/ya1HLUS2xbRpDf2JYQ-wv"
                  }
                ]
              }
            ]
          },
          "usesProp": {
            "NarrativeProp": [
              {
                "entityType": "NarrativeProp",
                "identifier": [
                  {
                    "identifierScope": "labkoat",
                    "identifierValue": "nprp/ozmg19-jNdhIlO1HwVP5G"
                  }
                ]
              },
              {
                "entityType": "NarrativeProp",
                "identifier": [
                  {
                    "identifierScope": "labkoat",
                    "identifierValue": "nprp/YESjEAVPVMJL"
                  }
                ]
              }
            ]
          }
        }
      }
```


## Standard Properties
There are some properties that are used consistently throughout the schema


##### entityType
A required property that enumerates the type of the entity.

A client recieving the OMC-JSON will need to know what any given entity is, so that it can parse it correctly.

##### identifier
The identifier, or identifiers unqiuely identify this entity within the described scope.

An entity can have multiple idetifiers, for example a Creative Work may have an identifier with the production company, the studio, imdb or EIDR.

##### name
A human readable name for the entity, helpful for people consuming the data, maybe used as a label or tag. There is no requirement that it be unique and should not be used as structured information or an identifier.

##### description
A human readable (preferably short) description of the entity. As with name, this is really meant for human consumption and should not be used for encoding structured information.

##### customData
The schema does not attempt to define every property that you might be associate with any given entity, our goal is to surface enough to allow a production to track, relate and find things across distinct parts of the workflow.

However, sometimes it may be desirable to embed data beyond the defined properties of an entity. This propery is unrestriced, beyond those imposed by JSON itself, allowing additional JSON, other serialized encodings or base64 for example. It is the responsibility of the sending and receiving parties to know what to do with the data.

Generally we recommend that more extensive metadata be held separately, as its own object a probably in a standardized format like IMF, JPG, etc. These blobs of data can be uniquely identified as assets in their own right and in turn be related or grouped using relationships or asset groups for example.

##### entityInfo
For encoding information specific to the entity itself, not what it is representing that may need to be communicated.

This can include properties like the version of the schema used, a version of the contained data, provenance, creatation or updated times.


