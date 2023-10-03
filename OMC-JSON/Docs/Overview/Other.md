#### Reification
Reification is the process of taking an abstract idea or concept and making it something concrete. In graphs and RDF this is often done to a relationship because RDF does not support having properties on a relationship itself. A new intermediate node is created that can express the concepts you wish to associate with that relationship.

The ontology uses this in a number of places, Context, Depiction/Portrayal, Participants.

For example,  a person working on a production could simply be related directly to the scenes they appear in, the characters they play, or the locations they need to be at. But often there is more information that we need to convey than that they simply appear in something. We probably want to know why they appear, or what they are supposed to be doing. Using a Participant allows to us associate other information, such as their Role. The same Person may be both acting and directing in a film, by having two Participants we can separate these different responsibilities,  if a given day they are acting in a scene their call sheet will be different than if they were only directing.

A Portrayal (a sub-class of Depiction) is another example. An actor portrays a Character, but often a character is portrayed by multiple actors, the stunt person, body double, voiceover, or cg model. Which of these portrayals is needed on any given day and for what tasks will different. Another example is a character that has different manifestations, a werewolf or human form for example. Each of these is a different portrayal of the same character, but even if played by the actor the werewolf version of the character will have very different requirements for makeup, costume, etc. Portrayals are a mechanism that allow us to associate different properties and relationships to different portrayals.

#### Sub-Classing
JSON does not support the concept of classes, and by extension, sub-classing, something the RDF model uses extensively. Therefore OMC-JSON uses a type property on some entities that allow the sub-class to be expressed. This was done in large part to help manage the schema overall, by not requiring every sub-class need to be expressed as it's own entity.

For example in RDF a parent class of NarrativeObject has various sub-classes NarrativeProp, NarrativeSetDressing, NarativeGreenery, etc.

```JSON
{
	"NarrativeObject": {
		"entityType": "NarrativeObject",
		"narrativeType": "prop"
	}
}
```

We use a similar mechanism for Asset `functionalType` and `structuralType`

#### Schema Simplifications
Some structures in OMC-JSON are only represented as a top down hierarchy, notably groups such as Asset groups and Participant groups. In JSON a hierarchy can inherently be represented in the structure, as one object can be nested inside another. This allows it's relationship to be easily inferred and does not need to be explicitly expressed.

Where this is used it is presumed that the consuming application can infer the relationship (and name) and recreate the graph in both directions if it so desires.

A similar simplification is used when an entity has an intrinsic property that is another entity. For example, Assets have the property ParticipantSC which is a direct reference to the entity that represents their structural class. In RDF this would be a named relationship, but for OMC-JSON the name however can be inferred if needed.

A graph uses a named relationship to associate all nodes
```
(Asset) -> [has.StructuralCharacteristic] -> (AssetStructuralClass)
```

The JSON schema simplifies this and the relationship can be inferred.
``` JSON
{
	"Asset": {
		"entityType": "Asset",
		"identifier": [{
			"identifierScope": "movielabs",
			"identifierValue": "ast-01"
		}],
		"AssetSC": {
			"entityType": "AssetSC",
			"identifier": [{
				"identifierScope": "movielabs",
				"identifierValue": "astsc-01"
			}]
		}
	}
}
```


#### Relationship Naming
As previously mentioned, relationships are a first class citizen in OMC, and representing these in JSON comes with some challenges as they are not a native construct of JSON. 

In RDF relationship names typically carry semantic meaning, with an ontology as complex as OMC this results in lot of different names, it can be challenging to know which name to use. To help manage this OMC only specifies a subset of relationships, in theory an entity can be related to any other and in certain applications new relationships that help answer specific queries can be created at will. For OMC we look to define enough to create a core set, the graph can then always be interrogated for the full path.

Our naming convention broadly breaks down into a set of 'verbs' followed with 'noun', separated using dot notation. There are a set of verbs such as `has, for, features, featuresIn, uses`. Generally verbs are paired, to represent each direction of the relationship i.e. `for` & `has`, or `uses` & `usedIn`, almost all relationships are bi-directional and even when not explicitly stated can be inferred. The different verbs refer to broadly different types of relationship, if `features` & `featuresIn` this will refer to two narrative entities being related, `uses` & `usedIn` are for production entities. A larger set is detailed in the section on [[Context&Relationships]].

The 'noun' is typically the entity type to which the relationship exists, i.e. `has.NarrativeObject`.

In OMC-JSON this is realized through the structure of the JSON itself, it is shown here inside a Context which is discussed further in the section on [[Context&Relationships]]

```JSON
{
	"Context": {
		"has": {
			"NarrativeObject": [
				{
					"entityType": "NarrativeObject",
					"identifier": [{
						"identifierScope": "movielabs",
						"identifierValue": "nrto-01"
					}]
				}
			]
		}
	}
}
```



