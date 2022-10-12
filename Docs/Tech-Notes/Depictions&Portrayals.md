# Depictions & Portrayals
Depictions are the mechanism used to relate narrative concepts to their production counterparts. Narrative elements are generally depicted by a production asset, A portrayal is the depiction of a Character.

In the RDF ontology depictions and portrayals are reified relationships. In OMC-JSON we do not need to do this when dealing with objects such as props or locations; we can represent these using a named relationship:
```
NarrativeProp -> isDepictedBy -> Asset
Asset -> depicts -> NarrativeProp

Character -> isPortrayedBy -> Participant
Participant -> portrays - Character
Character -> isPortrayedBy -> Asset
```

When depicting Assets, it is the Assets ``functionalType`` that describes the thing, i.e. whether it is a prop or production set.

Portrayals use a similar mechanism, but portrayals can be done by either a Participant or an Asset. For example when a character is modeled in 3D, the portrayal will refer to an Asset. More often than not a character will be portrayed by a person, which is a Participant, but this would also be the case if an animal were portraying the character. A service might be used to portray a character, for example an AI driven voiceover.

The functional type of the Asset or Participant describes the nature of the portrayal, for example:
```
actor
voiceover
stunt
```

The example shows a Character that references the Participant portraying it. A depiction follows the same pattern but would use the 'isDepictedBy' and 'depicts' relationships to reference an Asset.

```JSON
{  
  "entityType": "Character",  
  "identifier": [  
    {  
      "identifierValue": "chr-1234",  
      "identifierScope": "Movielabs"  
    }  
  ],  
  "name": "Sven",  
  "description": "An unassuming sattelite repair man",  
  "Context": {  
    "entityType": "Context",  
    "identifier": [  
      {  
        "identifierValue": "cxt-1234",  
        "identifierScope": "Movielabs"  
      }  
    ],  
    "isPortrayedBy": {  
      "entityType": "Participant",  
      "identifier": [  
        {  
          "identifierValue": "pct-5678",  
          "identifierScope": "Movielabs"  
        }  
      ]  
    }  
  }  
}
```

```JSON
{  
  "entityType": "Participant",  
  "identifier": [  
    {  
      "identifierValue": "pct-5678",  
      "identifierScope": "Movielabs"  
    }  
  ],  
  "name": "J. Warren Trezevant",  
  "description": "Stunt actor doing mo-cap for Sven",  
  "structuralCharacteristics": {  
    "structuralType": "person"  
  },  
  "functionalCharacteristics": {  
    "functionalType": "stunts"  
  },  
  "Context": {  
    "entityType": "Context",  
    "identifier": [  
      {  
        "identifierValue": "cxt-4567",  
        "identifierScope": "Movielabs"  
      }  
    ],  
    "portrays": {  
      "entityType": "Character",  
      "identifier": [  
        {  
          "identifierValue": "chr-1234",  
          "identifierScope": "Movielabs"  
        }  
      ]  
    }  
  }  
}
```





