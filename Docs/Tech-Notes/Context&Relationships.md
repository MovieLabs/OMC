
# Relationships
Relationships between entities are an essential part of the ontology. 

JSON does not have a native mechanism for expressing relationships (this is not JSON-LD schema) so OMC-JSON needs a means to express them

Identifiers are the foundation of relationships, all entities must have a unique identifier within a scope. Relationships in OMC always have a direction (from one entity to another),  typically relationships have an inverse.  The names of the relationships between entities carries semantic meaning that indicate how A is related to B, which is not the same as how B is related to A.

Relationships in ontology can exist either directly on an entity or as part of context. Exactly when and how to use each mechanism is a recommended practice in the ontology but is enforced in OMC-JSON to make schema development and validation more manageable. For relationships to entities that are intrinsic properties of another entity these are placed on the entity, relationships that describe an entities context must be used in a Context (see below for more details on Context).

An example of a relationship that is in intrinsic property is a Participants Structural Characteristics. It is represented in JSON like this. As per the schema conventions, the property name is capitalized, indicating it is a relationship to another entity, in this case the property can only reference single entity, so it is not an array. In this case it references a Person entity with the associated unique identifier.

``` JSON
{
	"Participant": {
		"entityType": "Participant",
		"identifier": [{
			"identifierScope": "Movielabs",
			"identifierValue": "prt-1234"
		}],
		"ParticipantSC": {
			"entityType": "Person",
			"identifier": [{
				"identifierScope": "Movielabs",
				"identifierValue": "per-5678"
			}],
		}
	}
}
```

The producer of the payload can elect to serialize the properties of the Person and include any or all of those properties in the payload, or leave it to the consumer to request those details with another lookup.

It is worth pointing out that the relationship name is implied here, has.ParticipantSC or has.Person, this direct relationship is used to simplify the JSON a little by removing a layer of nesting.

Relationships that are not an intrinsic property, are held in a Context, see below.





The following table describes entity types and the relationships they have to other entity types.

| Entity Type (functional type) | Relationship            | Entity Type          | Inverse                 |
|:----------------------------- |:----------------------- |:-------------------- |:----------------------- |
| Asset                | usedIn       | ProductionScene       | uses            |
| Asset           | for         | Character            | has           |
|                               |                         | NarrativeLocation    |                         |
|                               |                         | NarrativeProp        |                         |
|                               |                         | NarrativeScene       |                         |
|                               |                         | NarrativeWardrobe    |                         |
| Asset (script)                | isScriptFor             | CreativeWork         | hasScript               |
| Asset (storyboard)            | isStoryboardFor         | NarrativeScene       | hasStoryboard           |
|                               |                         | ProductionScene      |                         |
| Asset (script)                | isUsedIn                | ProductionScene      | uses                    |
| Asset (costume)               |                         |                      | usesCostume             |
| Asset (prop)                  |                         |                      | usesProp                |
| Asset (setDressing)           |                         |                      | usesSetDressing         |
| Asset (sequence)              |                         | Sequence             | usesShot                |
| Asset (prop)                  | depicts                 | NarrativeProp        | isDepictedBy            |
| Asset (setDressing)           |                         | NarrativeSetDressing |                         |
| Asset (costume)               |                         | NarrativeWardrobe    |                         |
| Character                     | appearsIn               | NarrativeScene       | features                |
|                               | hasConceptArt           | Asset                | isConceptArtFor         |
|                               | hasProp                 | NarrativeProp        | isPropFor               |
|                               | hasWardrobe             | NarrativeWardrobe    | isWardrobeFor           |
|                               | isPortrayedBy           | Portrayal            | portrays                |
| CreativeWork                  | hasScript               | Asset                | isScriptFor             |
|                               | hasDirector             | Participant          | isDirectorFor           |
|                               | hasProductionCompany    |                      | isProductionCompanyFor  |
| NarrativeLocation             | hasProductionLocation   | ProductionLocation   | isProductionLocationFor |
|                               | hasConceptArt           | Asset                | isConceptArtFor         |
| NarrativeProp                 | appearsIn               | NarrativeScene       | features                |
|                               | isPropFor               | Character            | hasProp                 |
|                               | isDepictedBy            | Asset                | depicts                 |
| NarrativeScene                | hasConceptArt           | Asset                | isConceptArtFor         |
|                               | hasNarrativeLocation    | NarrativeLocation    | isNarrativeLocationFor  |
|                               | hasProductionScene      | ProductionScene      | isProductionSceneFor    |
|                               | hasStoryboard           | Asset                | isStoryboardFor         |
|                               | isFromScript            | Asset                | isScriptFor             |
|                               | isFromWork              | CreativeWork         | hasNarrativeScene       |
|                               | features                | Character            | appearsIn               |
|                               |                         | NarrativeProp        |                         |
|                               |                         | NarrativeSetDressing |                         |
|                               |                         | NarrativeWardrobe    |                         |
| NarrativeSetDressing          | appearsIn               | NarrativeScene       | features                |
|                               | isDepictedBy            | Asset                | depicts                 |
| NarrativeWardrobe             | appearsIn               | NarrativeScene       | features                |
|                               | hasConceptArt           | Asset                | isConceptArtFor         |
|                               | isDepictedBy            | Asset                | depicts                 |
|                               | isWardrobeFor           | Character            | hasWardrobe             |
| Participant (person)          | isDirectorFor           | CreativeWork         | hasDirector             |
| Participant (organization)    | isProductionCompanyFor  | CreativeWork         | hasProductionCompany    |
| Portrayal                     | portrays                | Character            | isPortrayedBy           |
| ProductionLocation            | isProductionLocationFor | NarrativeScene       | hasProductionLocation   |
|                               |                         | ProductionScene      |                         |
| ProductionScene               | hasSlate                | Slate                | isSlateFor              |
|                               | hasNarrativeScene       | NarrativeScene       | hasProductionScene      |
|                               | hasStoryboard           | Asset                | isStoryboardFor         |
|                               | uses                    |                      | isUsedIn                |
|                               | usesCostume             |                      |                         |
|                               | usesProp                |                      |                         |
|                               | usesSetDressing         |                      |                         |
| Sequence                      | usesShot                | Asset                | isUsedIn                |
| Slate                         | isSlateFor              | Asset                | hasSlate                |
|                               |                         | ProductionScene      |                         |

*Note: This is not a complete list, and new relationships will be added as development continues*

*Note: Some relationships have been updated and may differ from the published ontology; this will be corrected in a future version*


# Context
As we have stated previously Relationships are a first class citizen in OMC, a Context is one of the primary mechanisms through which we can establish and manage the relationships that entities have between one another.

Contexts are themselves an entity, that can related to another entity, for example a Character or ProductionScene. In simple terms they can be thought as a bucket where relationships can be stored. Organizing relationships in a Context allows for several benefits, Contexts can be shared, so sets of entities that share connections only need one Context between them, also a Context can have a Context, meaning that they can be composed of smaller Contexts. Lastly an entity may have lots of relationships, but for a given workflow only a subset is needed, having them separate from the entity themselves allows a Context specific to a workflow or situation to be created.

The example below shows how a Character entity with a Context can look. The Character has two pieces of concept art and one NarrativeObject.

```JSON
{
	"entityType": "Character",
	"identifier": [{
		"identifierScope": "movielabs",
		"identifierValue": "chr/1234"
	}],
	"Context": {
		"entityType": "Context",
		"identifier": [{
			"identifierScope": "movielabs",
			"identifierValue": "cxt/1234"
		}],
		"contextType": "narrative",
		"has": {
			"Asset": [
				{
					"entityType": "Asset",
					"identifier": [{
						"identifierScope": "movielabs",
						"identifierValue": "ast-1234"
					}]
				},
				{
					"entityType": "Asset",
					"identifier": [{
						"identifierScope": "movielabs",
						"identifierValue": "ast-1235"
					}]
				}
			]
		},
		"needs": {
			"NarrativeObject": [
				{
					"entityType": "NarrativeObject",
					"identifier": [{
						"identifierScope": "movielabs",
						"identifierValue": "nprp-1234"
					}]
				}
			]
		}
	}
}

```

*Need to cover composing Contexts*
*Need to cover contextType*
*Need diagrams to illustrate examples*