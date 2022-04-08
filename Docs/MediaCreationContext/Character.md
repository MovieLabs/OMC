## Character





| Attribute   | Type         | Description                                   | Required |
| ----------- | ------------ | --------------------------------------------- | --- |
| Identifier  | [Identifier](../Utility/Identifier.md)   | A set of unique identifiers                   | Yes |
| Name        | [CompleteName](../Utility/CompleteName.md) | The name or names attributed to the character | No |
| Gender      | [Gender](../Utility/Gender.md) | The chosen gender of the character            | No |
| Profile     | [Profile](#Profile)     | A set of attributes that describe features of the character | No |
| description | string             | A brief description of the character          |
| Relationship | [Related](#Related) | Contexts and other entities the character is related to          | No |



##Profile

### Physical Characteristics

Allows for the the description of certain physical characteristics on a character, things that might be useful to an 
art department, wardrobe or casting for example. 

| Attribute  | Type              | Description | Required |
| ---------- | ----------------- | ----------- | ---- |
| species    | string            | A species to which this character belongs            | No |
| hairColor  | string            | The hair color of the character            | No |
| hairLength | string            | The length of hair of the character        | No |
| eyeColor   | string            | The color of the characters eyes            | No |
| height     | LinearMeasurement | The height of the character            | No |
| weight     | LinearMeasurement | The weight of the character            | No |



### physicalCharacteristics.species

**Type**: string

**Required**: No

**Examples**: ```'Human', 'Borg', 'Goblin', 'Frog'```

### physicalCharacteristics.haircolor

**Type**: string

**Required**: No

**Examples**: ```'Brown', 'Pink', 'Blond', 'Mixed'```


### physicalCharacteristics.hairLength

**Type**: string

**Required**: No

**Examples**: ```'Bald', 'Mullet', 'Wavy'```


### physicalCharacteristics.eyeColor

**Type**: string

**Required**: No

**Examples**: ```Blue', 'Greem', 'Brown'```


### physicalCharacteristics.height

**Type**: linearMeasurment

**Required**: No

**Examples**: ```'1m87cm', '5ft7in'```


### physicalCharacteristics.weight
**Type**: linearMeasurment

**Required**: No

**Examples**: ```'1m87cm', '5ft7in'```



## Related


| Predicate | Type  | Description |
| ---------- | ----------------- | ---- |
| hasNarrativeScene | [Scene](./NarrativeScene.md) | Narrative scenes the character appears in |
|  | NarrativeLocation | |
| uses | Prop | Props the character uses |
| | | |









unstructuredData: (figure out JSON schema & graphql types)
Should have a provenance
