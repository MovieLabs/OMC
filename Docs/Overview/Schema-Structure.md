# JSON Schema Overview
OMC is written in RDF, which provides a useful degree of formality, especially for relationships and complex classes. JSON, of course, can also be used for data modelling, but it has different mechanics for classes, properties, and types, and less emphasis on relationships than RDF.

The JSON schema retains the vocabulary, concepts, and top-level structures of the RDF, although some changes are necessary to support expressing the details of the concepts in JSON. In particular, the JSON schema provides mechanisms for encoding relationships (in the RDF sense) and complex classes.

## Key Concepts
There are three pervasive concepts in the JSON schema:
- Entities
- Identifiers and references
- Relationships

### Entities
RDF is a class based system. JSON does not use a class based model or the idea of class inheritance.

For the JSON schema we use a compositional model, where a set of individual schemas is used to create entities that align with the RDF classes. These schemas can then be composed (via referencing) to create new entities. Each entity can be nested inside other entities or included in an array of entities.

Each entity requires the property ``entityType``. Knowing the entity type allows applications to reference the correct schema when validating or parsing the data.

> **Entity**: A top level concept in the ontology that includes a set of properties with associated values.

> **Property**: A \<key\>\<value\> pair where the value can be an entity, complex type (object or array of objects), or primitive value (string, number, Boolean or null)

The schema follows some general conventions:
- Each entity is defined as a separate JSON schema.
- The first letter of a defined entity is capitalized.
- Entities are required to declare their ``entityType`` and have a unique ``identifier``.

Below we show a section of the schema for Narrative Location, which illustrates how the ``identifier`` sub-Schema is included by reference. The Location is itself an entity and therefore capitalized; it references the Location entity using an identifier. The properties ``name`` and ``description`` follow.

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
		"$ref": "../Utility/identifier#/properties/identifier"
	},
	"name": {
		"type": "string",
		"title": "Name"
	},
	"description": {
		"type": "string",
		"title": "Description"
	},
	"Location": {
		"$ref": "../Utility/Location"
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
		"entityType": "Location",
		"identifier": [{
			"identifierValue": "5678",
			"identifierScope": "Movielabs"
		}]
	},
	"name": "221B Baker Street - exterior",
	"description": "Sherlock Holmes' residence"
}
```



## Identifiers and References

### Identifiers
The example above uses an identifier in two places. In the ontology, an Identifier is "a string of characters that uniquely identifies an object within a particular scope." An identifier is really just a way of referring to something; undifferentiated strings and URIs/IRIs are common forms for an identifier, and there are many more specialized ones as well.

For the production system (and any system that consists of multiple cooperating systems) it is essential to know the *scope* of the identifier - the universe within which the identifier is valid and unique. For example, "42" is a perfectly good identifier, but without knowing the scope, there is no way of knowing what it represents. See [OMC Part 9: Utilities](https://mc.movielabs.com/docs/omc/utilities/concepts) for further details, including some meanings of "42".

Below is the JSON schema for an identifier/scope pair, as shown here, followed by an example of an instance.

**JSON Schema**
``` JSON
{
	"identifier": {
		"type": "array",
		"title": "identifier",
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
		"identifierScope": "MovieLabs",
		"identifierValue": "1234"
  	}]
}
```



### References
The use of identifiers is a central component of all entities; every entity must be uniquely identified with an identifier.

Using identifiers allows any entity to be included either by reference or by inclusion; the decision is left to the application. Where only an identifier is included in a payload the presumption is the receiving party can make a follow up request using the reference identifier if it needs more detailed information.

Which of the two methods to use (identifier vs full data) will differ across applications and workflows, thinking about things like latency (or even availability) of identifier resolution, caching behavior in applications, etc.  It is always possible to send full data for any entity to any depth, with the usual warnings about the size of the data and the fact that it is graph-based.

The example below shows a Narrative Location, where the Location itself is only referenced by its identifier. A client receiving this could then make a request using the Location's identifier to get the full set of attributes if it needs them.

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
		}]
	},
	"description": "Sherlock Holmes' residence"
}
```

The next example shows a full Location entity de-referenced and included directly in the payload.

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
			"postalCode": "NW1 6XE",
			"country": "uk"
		}
	},
	"description": "Sherlock Holmes' residence"
}
```

The schemas are structured in such a way that objects can be nested *ad infinitum*. It is up to the sending and receiving applications to decide how and what to exchange. However, developers should be aware that given the graph based nature of production data, circular references can be easily created.

When the decision is made to pass just a reference and the receiving client wants to make a follow up request for additional information there are some potential issues: a decoupled system may not even know which application prepared the data and the client will need to know API endpoints, have the required credentials, and so on to acquire the additional data.  Sometimes all that a particular application wants is an identifier so it can anchor the portions of the graph it cares about in a broader structure, in which case the identifier doesn't need to be dereferenced.

URLs can be used as identifiers but can be fragile in complex production systems: things can move or exist in more than one location. A `file:` URL can be used as an identifier, but this can make workflows fragile, since even a shared filesystem can be mounted differently on different systems.

The 2030 vision proposes the use of a resolution mechanism. A resolver can be used for retrieving files and/or additional data. When an identifier is resolved with a resolver the response is one or more URLs that can then be used to retrieve information.

For more information on resolvers see here: [Through the Looking Glass](https://movielabs.com/through-the-looking-glass/)

## Relationships
Relationships are a fundamental part of the ontology.

There are not really standard mechanisms for encoding relationships in JSON. We are using JSON Schema rather than JSON-LD, so we have adopted the following patterns for referencing other entities. There are two common situations where you may wish to include references:
- When another entity is an intrinsic property of an entity
- When you wish to use a named relationship, typically as part of a Context

When another entity is an intrinsic property then the entity type to which you are referring is often the name of the property; an example of this can be seen for Location above. However, another property name can be used, such as the property ``source`` in a Shot, which refers to an Asset. (The Asset can be, for example, captured video, motion capture, animation, or an animated storyboard.)
```JSON
{
	"entityType": "Asset",
	"identifier": [{
		"identifierValue": "1234",
		"identifierScope": "Movielabs"
	}],
	"functionalCharacteristics": {
		"functionalType": "shot",
		"functionalProperties": {
			"source": {
				"entityType": "Asset",
				"identifier": [{
					"identifierScope": "labkoat",
					"identifierValue": "nscn/St_Hh-LxAQo4ICUAtbZ0v"
				}]
			},
			"start": "0:10",
			"end": "0:17"
		}
	}
}
```


The Context example below demonstrates the use of named relationships. It shows how a `NarrativeScene` is related to entities such as props and characters that appear in that scene. This follows the pattern:

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
		"$ref": "../Utility/identifier.json#/properties/identifier",
		"name": {
			"type": "string",
			"title": "Name"
		},
		"description": {
			"type": "string",
			"title": "Description"
		},
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
				"features": {
					"type": "object",
					"title": "usesProp",
					"properties": {
						"NarrativeProp": {
							"type": "array",
							"items": {
								"$ref": "../MediaCreationContext/NarrativeProp.json"
							}
						},
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
	"identifier": [{
		"identifierScope": "labkoat",
		"identifierValue": "nscn/St_Hh-LxAQo4ICUAtbZ0v"
	}],
	"name": "Space",
	"description": "Sven repairs satellite and is ambushed by Trilobot",
	"sceneNumber": "2",
	"Context": {
		"entityType": "Context",
		"identifier": [{
			"identifierScope": "labkoat",
			"identifierValue": "cxt-4567"
		}],
		"isFromScript": {
			"Asset": [
				{
					"entityType": "Asset",
					"identifier": [{
						"identifierScope": "labkoat",
						"identifierValue": "ast/lHz-ua3XG-xQzDyCDbbKZ"
					}],
					"name": "mls_hsm_script_vshootingfd_2021_12_17_v004.pdf",
					"description": null,
					"structuralCharacteristics": {
						"structuralType": "document",
						"identifier": [{
							"identifierScope": "labkoat",
							"identifierValue": "astsc/vxFhewUHgTpM78A4tm5TN"
						}],
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
					"identifier": [{
						"identifierScope": "labkoat",
						"identifierValue": "chr/HNvHjXqJY9wv1IwjG-Hf1"
					}]
				},
				{
					"entityType": "Character",
					"identifier": [{
						"identifierScope": "labkoat",
						"identifierValue": "chr/ya1HLUS2xbRpDf2JYQ-wv"
					}]
				}
			],
			"NarrativeProp": [
				{
					"entityType": "NarrativeProp",
					"identifier": [{
						"identifierScope": "labkoat",
						"identifierValue": "nprp/ozmg19-jNdhIlO1HwVP5G"
					}]
				},
				{
					"entityType": "NarrativeProp",
					"identifier": [{
						"identifierScope": "labkoat",
						"identifierValue": "nprp/YESjEAVPVMJL"
					}]
				}
			]
		}
	}
}
```


## Standard Properties
There are some properties that are used throughout the schema

##### entityType
A required property that enumerates the type of the entity.

A client receiving the OMC-JSON will need to know what any given entity is, so that it can parse it correctly.

##### identifier
The identifier, or identifiers uniquely identify this entity within the described scope.

An entity can have multiple identifiers. For example a Creative Work may have an identifier with the production company's ID, the studio's ID, an IMDb ID, or an EIDR ID..

##### name
A human readable name for the entity, helpful for clients consuming the data; it is often useful for applications to have something like a label or tag for a UI. There is no requirement that it be unique and it should not be used as structured information or considered unique.

##### description
A human readable (preferably short) description of the entity. As with name, this is really meant for human consumption and should not be used for encoding structured information.

##### customData
The schema does not attempt to define every property that you might be associate with any given entity, our goal is to surface enough to allow a production to track, relate and find things across distinct parts of the workflow.

However, sometimes it may be desirable to embed data beyond the defined properties of an entity. This property is unrestricted, beyond the constraints imposed by JSON itself, allowing additional JSON, other serialized encodings, or base64 for example. It is the responsibility of the sending and receiving parties to know what to do with the data.

Generally we recommend that more extensive metadata be identified separately as a standalone object often in standardized formats like IMF, JPG, etc. These blobs of data are assets in their own right and therefore can be uniquely identified with the data as essence, they can then be related or grouped with the assets they describe.

See [Schema-Practices](./Schema-Practices#Extending%20the%20schema) for more information.

##### entityInfo
This is encodes information specific to the entity itself, not what it is representing. It might include one or all of the following:
 - Version of the schema used to create the instance
 - Version of the instance itself (under development; will change)
 - Provenance of the instance (under development; will change)

