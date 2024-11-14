# root

### Properties
This forms the top level structure of an OMC-JSON object or payload.

| Operator | Type                                                   | Description                                                                                                    |
| -------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| oneOf    | [rootEntity](#rootEntity)<br>[rootObject](#rootObject) | An array of any entity type<br>An object where the property name carries an array of the declared entity type. |
*Note: In either case (notably for the rootObject) if the producer elects to embed related entities in a top level object then entities of different types can appear in the same JSON structure*

### Object Properties
#### rootEntity
An array of OMC entities of any type

| Property | Constraint | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| -------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
|          | anyOf      | [ <br>[Asset](../Asset/Asset.md)<br>[AssetSC](../Asset/AssetSC.md)<br>[Character](../MediaCreationContext/Character.md)<br>[Context](../MediaCreationContext/Context.md)<br>[CreativeWork](../MediaCreationContext/CreativeWork.md)<br>[Depiction](../MediaCreationContext/Depiction.md)<br>[Effect](../MediaCreationContext/Effect.md)<br>[NarrativeAudio](../MediaCreationContext/NarrativeAudio.md)<br>[NarrativeLocation](../MediaCreationContext/NarrativeLocation.md)<br>[NarrativeObject](../MediaCreationContext/NarrativeObject.md)<br>[ProductionLocation](../MediaCreationContext/ProductionLocation.md)<br>[ProductionScene](../MediaCreationContext/ProductionScene.md)<br>[Slate](../MediaCreationContext/Slate.md)<br>[SpecialAction](../MediaCreationContext/SpecialAction.md)<br>[Participant](../Participant/Participant.md)<br>[Organization](../Participant/Organization.md)<br>[Department](../Participant/Department.md)<br>[Person](../Participant/Person.md)<br>[Service](../Participant/Service.md)<br>[Role](../Participant/Role.md)<br>[Infrastructure](../Infrastructure/Infrastructure.md)<br>[InfrastructureSC](../Infrastructure/InfrastructureSC.md)<br>[Task](../Task/Task.md)<br>[TaskSC](../Task/TaskSC.md)<br>[Composition](../Utility/Composition.md)<br>[Location](../Utility/Location.md)<br> ] |             |

#### rootObject
An object where the property name carries an array of the declared entity type.

| Property           | Constraint | Type                                                                    | Description |
| ------------------ | ---------- | ----------------------------------------------------------------------- | ----------- |
| Asset              |            | [ [Asset](../Asset/Asset.md) ]                                          |             |
| AssetSC            |            | [ [AssetSC](../Asset/AssetSC.md) ]                                      |             |
| Character          |            | [ [Character](../MediaCreationContext/Character.md) ]                   |             |
| Context            |            | [ [Context](../MediaCreationContext/Context.md) ]                       |             |
| CreativeWork       |            | [ [CreativeWork](../MediaCreationContext/CreativeWork.md) ]             |             |
| Depiction          |            | [ [Depiction](../MediaCreationContext/Depiction.md) ]                   |             |
| Effect             |            | [ [Effect](../MediaCreationContext/Effect.md) ]                         |             |
| NarrativeAudio     |            | [ [NarrativeAudio](../MediaCreationContext/NarrativeAudio.md) ]         |             |
| NarrativeLocation  |            | [ [NarrativeLocation](../MediaCreationContext/NarrativeLocation.md) ]   |             |
| NarrativeObject    |            | [ [NarrativeObject](../MediaCreationContext/NarrativeObject.md) ]       |             |
| ProductionLocation |            | [ [ProductionLocation](../MediaCreationContext/ProductionLocation.md) ] |             |
| ProductionScene    |            | [ [ProductionScene](../MediaCreationContext/ProductionScene.md) ]       |             |
| Slate              |            | [ [Slate](../MediaCreationContext/Slate.md) ]                           |             |
| SpecialAction      |            | [ [SpecialAction](../MediaCreationContext/SpecialAction.md) ]           |             |
| Participant        |            | [ [Participant](../Participant/Participant.md) ]                        |             |
| Organization       |            | [ [Organization](../Participant/Organization.md) ]                      |             |
| Department         |            | [ [Department](../Participant/Department.md) ]                          |             |
| Person             |            | [ [Person](../Participant/Person.md) ]                                  |             |
| Service            |            | [ [Service](../Participant/Service.md) ]                                |             |
| Role               |            | [ [Role](../Participant/Role.md) ]                                      |             |
| Infrastrcuture     |            | [ [Infrastructure](../Infrastructure/Infrastructure.md) ]               |             |
| InfrastructureSC   |            | [ [InfrastructureSC](../Infrastructure/InfrastructureSC.md) ]           |             |
| Task               |            | [ [Task](../Task/Task.md) ]                                             |             |
| TaskSC             |            | [ [TaskSC](../Task/TaskSC.md) ]                                         |             |
| Composition        |            | [ [Composition](../Utility/Composition.md) ]                            |             |
| Location           |            | [ [Location](../Utility/Location.md) ]                                  |             |

## Examples

A CreativeWork and a Character shown in the array format.

```JSON
[
	{  
	  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
	  "entityType": "CreativeWork",  
	  "identifier": [  
	    {  
	      "identifierScope": "labkoat",  
	      "identifierValue": "cw/hlDTz5s8IStbxWvdRVfSh"  
	    }  
	  ],  
	  "creativeWorkType": "creativeWork",  
	  "creativeWorkCategory": "short",  
	  "creativeWorkTitle": [  
	    {  
	      "title": "Hyperspace Madness",  
	      "titleType": "releaseTitle",  
	      "titleLanguage": "en"  
	    }
	  ],
	  "description": "Sven is a bumbling intergalactic repair man sent off to investigate a malfunctioning satellite.. He is quickly ambushed by the dreaded Killamari who have taken over the planet and plan to use it as a base to invade earth.",  
	  "approximateLength": "PT5M",  
	  "originalLanguage": [  
	    "en"  
	  ],  
	  "countryOfOrigin": [  
	    "US"  
	  ]
	},
	{  
	  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
	  "entityType": "Character",  
	  "identifier": [  
	    {  
	      "identifierScope": "labkoat",  
	      "identifierValue": "chr/HNvHjXqJY9wv1IwjG-Hf1"  
	    }  
	  ],  
	  "characterName": {  
	    "fullName": "Sven",  
	    "firstGivenName": "Sven",  
	    "scriptName": "SVEN"  
	  },  
	  "description": "Sven is an unassuming Satellite repair man. He spends his time alone in his ship traveling to remote planets on the outskirt of the galaxy maintaining a network of exploration satellites. He is more of a lover than a fighter.",  
	}
]
```


A CreativeWork and a Character shown in the object format.
```JSON
{
	"CreativeWork": [
		{  
		  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
		  "entityType": "CreativeWork",  
		  "identifier": [  
		    {  
		      "identifierScope": "labkoat",  
		      "identifierValue": "cw/hlDTz5s8IStbxWvdRVfSh"  
		    }  
		  ],  
		  "creativeWorkType": "creativeWork",  
		  "creativeWorkCategory": "short",  
		  "creativeWorkTitle": [  
		    {  
		      "title": "Hyperspace Madness",  
		      "titleType": "releaseTitle",  
		      "titleLanguage": "en"  
		    }
		  ],
		  "description": "Sven is a bumbling intergalactic repair man sent off to investigate a malfunctioning satellite.. He is quickly ambushed by the dreaded Killamari who have taken over the planet and plan to use it as a base to invade earth.",  
		  "approximateLength": "PT5M",  
		  "originalLanguage": [  
		    "en"  
		  ],  
		  "countryOfOrigin": [  
		    "US"  
		  ]
		}	
	],
	"Character": [
		{  
		  "schemaVersion": "https://movielabs.com/omc/json/schema/v2.6",  
		  "entityType": "Character",  
		  "identifier": [  
		    {  
		      "identifierScope": "labkoat",  
		      "identifierValue": "chr/HNvHjXqJY9wv1IwjG-Hf1"  
		    }  
		  ],  
		  "characterName": {  
		    "fullName": "Sven",  
		    "firstGivenName": "Sven",  
		    "scriptName": "SVEN"  
		  },  
		  "description": "Sven is an unassuming Satellite repair man. He spends his time alone in his ship traveling to remote planets on the outskirt of the galaxy maintaining a network of exploration satellites. He is more of a lover than a fighter.",  
		}
	]
}
```