# Relationships
Relationships between entities are a critical part of the ontology. JSON does not natively have a mechanism for expressing relationships so the JSON implementation needs to define one.

Relationships are contained within a Context. A Context is itself an entity and so Contexts can be constructed and used in multiple places, most entities support the inclusion of a Context.

Conceptually a context takes the following format, an identifier the named relationships, the entityType to which it's related and then the entity instance itself

```
<identifier>,
<relationship>
	<entityType>
			[<entityInstance>]
```

The example below shows how a Character entity may look (other properties were omitted for clarity)

```JSON
{
	"entityType": "Character",
	"identifier": [{
		"identifierScope": "movielabs",
		"identifierValue": "chr/1234"
	}],
	"Context": {
		"entityType": "Character",
		"identifier": [{
			"identifierScope": "movielabs",
			"identifierValue": "cxt/1234"
		}],
		"hasConceptArt": {
			"Asset": [
				{
					"entityType": "Asset",
					"identifier": [{
						"identifierScope": "movielabs",
						"identifierValue": "ast/1234"
					}]
				}
			]
		},
		"hasProp": {
			"NarrativeProp": [
				{
					"entityType": "NarrativeProp",
					"identifier": [{
						"identifierScope": "movielabs",
						"identifierValue": "nprp/1234"
					}]
				}
			]
		}
	}
}

```

Relationships are typically bidirectional and almost always have a direction, i.e. the name of the relationship indicates how A is related to B, which is not the same as how B is related to A. Therefore it is generally true that for any given relationship there is an inverse relationship also. 

The name of the relationship carries semantic meaning and therefore can be used to infer the nature of the relation between two entities.

The following table describes entity types and the relationships they have to other entity types.

| Entity Type          | Relationship            | Entity Type           | Inverse                 |
|:-------------------- |:----------------------- |:--------------------- |:----------------------- |
| Asset                | hasNarrativeScene       | NarrativeScene        | isFromScript            |
|                      | isConceptArtFor         | Character             | hasConceptArt           |
|                      |                         | NarrativeLocation     |                         |
|                      |                         | NarrativeProp         |                         |
|                      |                         | NarrativeScene        |                         |
|                      |                         | NarrativeWardrobe     |                         |
|                      | isScriptFor             | CreativeWork          | hasScript               |
|                      | isStoryboardFor         | NarrativeScene        | hasStoryboard           |
|                      |                         | ProductionScene       |                         |
|                      | isUsedIn                | ProductionScene       | uses                    |
|                      |                         |                       | usesCostume             |
|                      |                         |                       | usesProp                |
|                      |                         |                       | usesSetDressing         |
|                      |                         | Sequence              | usesShot                |
|                      | depicts                 | NarrativeProp         | isDepictedBy            |
|                      |                         | NarrativeSetDressing  |                         |
|                      |                         | NarrativeWardrobe     |                         |
| Character            | appearsIn               | NarrativeScene        | features                |
|                      | hasConceptArt           | Asset                 | isConceptArtFor         |
|                      | hasProp                 | NarrativeProp         | isPropFor               |
|                      | hasWardrobe             | NarrativeWardrobe     | isWardrobeFor           |
|                      | isPortrayedBy           | Portrayal             | portrays                |
| CreativeWork         | hasScript               | Asset                 | isScriptFor             |
|                      | hasDirector             | Participant           | isDirectorFor           |
|                      | hasProductionCompany    |                       | isProductionCompanyFor  |
| NarrativeLocation    | hasProductioLocation    | ProductionLocation    | isProductionLocationFor |
|                      | hasConceptArt           | Asset                 | isConceptArtFor         |
| NarrativeProp        | appearsIn               | NarrativeScene        | features                |
|                      | isPropFor               | Character             | hasProp                 |
|                      | isDepictedBy            | Asset                 | depicts                 |
| NarrativeScene       | hasConcepArt            | Asset                 | isConceptArtFor         |
|                      | hasNarrativeLocation    | NarrativeLocation     | isNarrativeLocationFor  |
|                      | hasProductionScene      | ProductionScene       | isProductionSceneFor    |
|                      | hasStoryboard           | Asset                 | isStoryboardFor         |
|                      | isFromScript            | Asset                 | isScriptFor             |
|                      | isFromWork              | CreativeWork          | hasNarrativeScene       |
|                      | features                | Character             | appearsIn               |
|                      |                         | NarrativeProp         |                         |
|                      |                         | NarrativeSetDresssing |                         |
|                      |                         | NarrativeWardrobe     |                         |
| NarrativeSetDressing | appearsIn               | NarrativeScene        | features                |
|                      | isDepictedBy            | Asset                 | depicts                 |
| NarrativeWardrobe    | appearsIn               | NarrativeScene        | features                |
|                      | hasConceptArt           | Asset                 | isConceptArtFor         |
|                      | isDepictedBy            | Asset                 | depicts                 |
|                      | isWardrobeFor           | Character             | hasWardrobe             |
| Participant          | isDirectorFor           | CreativeWork          | hasDirector             |
|                      | isProductionCompanyFor  | CreativeWork          | hasProductionCompany    |
| Portrayal            | portrays                | Character             | isPortrayedBy           |
| ProductionLocation   | isProductionLocationFor | NarrativeScene        | hasProductionLocation   |
|                      |                         | ProductionScene       |                         |
| ProductionScene      | hasSlate                | Slate                 | isSlateFor              |
|                      | hasNarrativeScene       | NarrativeScene        | hasProductionScene      |
|                      | hasStoryboard           | Asset                 | isStoryboardFor         |
|                      | uses                    |                       | isUsedIn                |
|                      | usesCostume             |                       |                         |
|                      | usesProp                |                       |                         |
|                      | usesSetDressing         |                       |                         |
| Sequence             | usesShot                | Asset                 | isUsedIn                |
| Slate                | isSlateFor              | Asset                 | hasSlate                |
|                      |                         | ProductionScene       |                         |

*Note: This is not a complete list, and new relationships will be added as development continues*

*Note: Some relationships have been updated and may differ from the published ontology, this will be corrected in a future version*

