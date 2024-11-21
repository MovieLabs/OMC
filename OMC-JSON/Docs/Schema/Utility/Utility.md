# Utility
Common data models and data structures used in multiple places and in multiple ways in a larger system.

## General

#### annotation
Human readable commentary, explanation, or information.

| Property | Constraint | Type         | Description                         |
| -------- | ---------- | ------------ | ----------------------------------- |
| author   |            | string, null | Who wrote or added this annotation  |
| title    |            | string, null | A title for the note or annotation. |
| text     |            | string, null | The text of the note or annotation. |

#### customData
A user defined set of custom data in the payload of the instance, used where the formal schema lacks required properties.

| Constraint | Type         | Description |
| ---------- | ------------ | ----------- |
|            | object, null |             |

#### identifier
An identifier uniquely identifies an entity within a particular scope.

| Property   | Constraint | Type                                          | Description                                                            |
| ---------- | ---------- | --------------------------------------------- | ---------------------------------------------------------------------- |
| identifier |            | [&nbsp[identifierItem](#identifierItem)&nbsp] | An identifier uniquely identifies an entity within a particular scope. |
#### identifierItem

| Property        | Constraint | Type           | Description                                                                                              |
| --------------- | ---------- | -------------- | -------------------------------------------------------------------------------------------------------- |
| identifierScope | required   | string         | The universe within which an identifier is valid and unique.                                             |
| identifierValue | required   | string         | A string of characters that uniquely identifies an object within a particular scope.                     |
| combinedForm    |            | string<br>null | A combination of the Identifier Scope and Value that is useful for utilizing the identifier in a system. |
| url             |            | string<br>null | A URL or IRI that can be used for resolving the Identifier Value within the Identifier Scope.            |

#### language
An IETF BCP 47 language code.

| Constraint | Type         | Description                   |
| ---------- | ------------ | ----------------------------- |
|            | string, null | An IETF BCP 47 language code. |
*Note: OMC-JSON users are expected to comply with valid language codes*

#### tag
A short string from a particular set, used for categorization and description.

| Property | Constraint | Type                | Description                                                                         |
| -------- | ---------- | ------------------- | ----------------------------------------------------------------------------------- |
| domain   |            | string, null        | An indication of the set or system in which the tag values are relevant or defined. |
| value    |            | [ string ]<br> null | A set of tags taken from the domain.                                                |

## People and Place

### Object Properties
#### address
A postal address or identifiable location of a place or building.

| Property   | Constraint | Type                | Description                                                              |
| ---------- | ---------- | ------------------- | ------------------------------------------------------------------------ |
| street     |            | string null         | The street address                                                       |
| locality   |            | string null         | The locality in which the street address is, and which is in the region. |
| region     |            | string null         | The region in which the locality is, and which is in the country.        |
| postalCode |            | string<br>null      | A zip or postal code.                                                    |
| country    |            | [country](#country) | The country as an ISO 3166-1 alpha-2 country code.                       |

#### country
An ISO 3166-1 alpha-2 country code.

| Constraint              | Type         | Description                         |
| ----------------------- | ------------ | ----------------------------------- |
| pattern: `^[A-Z][A-Z]$` | string, null | An ISO 3166-1 alpha-2 country code. |
*Note: OMC-JSON constrains this to two capital letters, the users are expected to comply with valid country codes*
#### coordinates
A global positioning coordinate in compliance with WGS 84.

| Property  | Constraint            | Type         | Description |
| --------- | --------------------- | ------------ | ----------- |
| latitude  | min: -90<br>max: 90   | number, null |             |
| longitude | min: -180<br>max: 180 | number, null |             |
#### contact
Means by which the subject of an entity may be contacted in the production.

| Property      | Constraint | Type                    | Description       |
| ------------- | ---------- | ----------------------- | ----------------- |
| email         |            | [email](#email)         | Email address'    |
| telephone<br> |            | [telephone](#telephone) | Telephone numbers |
#### email

| Property | Constraint | Type         | Description            |
| -------- | ---------- | ------------ | ---------------------- |
| business |            | string, null | Business email address |
| personal |            | string, null | Personal email address |
#### telephone

| Property | Constraint | Type         | Description               |
| -------- | ---------- | ------------ | ------------------------- |
| business |            | string, null | Business telephone number |
| personal |            | string, null | Personal telephone number |

#### gender
A person, or others, expressed or preferred gender and pronoun.

| Property      | Constraint | Type                                               | Description                                   |
| ------------- | ---------- | -------------------------------------------------- | --------------------------------------------- |
| identifiesAs  | enum       | `"male", "female", "other", "unknown", null`       | The gender by which an individual identifies. |
| genderPronoun | enum       | `"he/him", "she/her", "ze/hir", "they/them", null` | An individual's pronoun of choice.            |

#### basicName
A canonical name and alternative name for the entity.

| Property    | Constraint | Type             | Description                                        |
| ----------- | ---------- | ---------------- | -------------------------------------------------- |
| fullName    |            | string,&nbspnull | The full an complete name of the entity.           |
| altName<br> |            | string,&nbspnull | An alternate, often shortened name for the entity. |

#### completeName
A detailed description of a person, or other entities, name and variants of their name.

| Property            | Constraint | Type             | Description                                                                                                                             |
| ------------------- | ---------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| firstGivenName      |            | string,&nbspnull | A person's first name, also referred to as given name.                                                                                  |
| secondGivenName<br> |            | string,&nbspnull | A person's second given name, also referred to as middle name.                                                                          |
| familyName          |            | string,&nbspnull | A person's family name, also referred to as surname.                                                                                    |
| fullName            |            | string,&nbspnull | A complete name, typically a conjunction of familyName, firstGivenName and possibly other fields.                                       |
| birthName           |            | string,&nbspnull | A person's name at birth, sometimes referred to as maiden name.                                                                         |
| primaryName         |            | string,&nbspnull | A person's primary name, one they typically use, also often a combination of first, second and family name.                             |
| pseudonym           |            | string,&nbspnull | A fictitious name.                                                                                                                      |
| altName             |            | string,&nbspnull | An alternate, often shortened name for the person.                                                                                      |
| translatedName      |            | string,&nbspnull | A person's name translated to a different language.                                                                                     |
| nickname            |            | string,&nbspnull | A familiar, sometimes humorous, name given to a person used in place of their real name.                                                |
| moniker             |            | string,&nbspnull | A nickname or per name for a person,                                                                                                    |
| alias               |            | string,&nbspnull | An alias being used by a person often used to disguise someone's real identity, sometimes used when booking hotel rooms or restaurants. |
| contractualName     |            | string,&nbspnull | The name a person uses for contractual purposes.                                                                                        |
| displayName         |            | string,&nbspnull | A version of the name used when displaying in user interfaces and the like.                                                             |
| sortName            |            | string,&nbspnull | A name useful for sort algorithms, e.g. by in order familyName, firstGivenName.                                                         |
| scriptName          |            | string,&nbspnull | A name used in a script for a character, often capitalized.                                                                             |
| prefix              |            | string,&nbspnull | A prefix that can indicate a person's gender or title.                                                                                  |
| suffix              |            | string,&nbspnull | A suffix, often used to indicate a title or classification.                                                                             |

## Time and Measurement

#### dateTime
Should be formatted to comply with ISO 8601

| Constraint                                                                                                                                                                                                         | Type         | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ----------- |
| pattern: `^(?:19\|20)\d{2}-(?:0[1-9]\|1[0-2])-(?:0[1-9]\|[12]\d\|3[01])T(?:[01]\d\|2[0-3]):[0-5]\d:[0-5]\d(?:\|\.\d\d)(?:Z\|-0[1-9]\|-1\d\|-2[0-3]\|-00:?(?:0[1-9]\|[1-5]\d)\|\+[01]\d\|\+2[0-3])(?:\|:?[0-5]\d)$` | string, null |             |

#### date
Should be formatted to comply with ISO 8601: yyyy-mm-dd

| Constraint                      | Type         | Description |
| ------------------------------- | ------------ | ----------- |
| pattern: `\d{4}-[01]\d-[0-3]\d` | string, null |             |
**Examples**
2024-11-20
#### durationTime
Should be formatted to comply with ISO 8601:
yyyy-mm-dd'T'hh:mm:ss.sss'Z'

| Constraint                                                                       | Type         | Description |
| -------------------------------------------------------------------------------- | ------------ | ----------- |
| pattern: `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z\|[+-]\d{2}:\d{2})$` | string, null |             |
|                                                                                  |              |             |
**Examples**
2013-02-14T13:15:03Z
2013-02-14T13:15:03.100Z
2013-02-14T13:15:03-08:00

#### timeCode
SMPTE Timecode in the format HH:MM:SS:FF. 

| Constraint                                                  | Type         | Description |
| ----------------------------------------------------------- | ------------ | ----------- |
| pattern: `^([01]\d\|2[0-3]):([0-5]\d):([0-5]\d):([0-2]\d)$` | string, null |             |
*Note: Assumes the frame rate is 23.98, 24, 25, 29.97 NDF, or 30*

#### weight
| Constraint                                                    | Type         | Description       |
| ------------------------------------------------------------- | ------------ | ----------------- |
| pattern: `^(\d+kg)?(\d+g)?$`<br>pattern: `^(\d+lb)?(\d+oz)?$` | string, null | 3kg7g<br>12lb14oz |
#### dimensions

| Property | Constraint | Type                              | Description |
| -------- | ---------- | --------------------------------- | ----------- |
| height   |            | [linearDistance](#linearDistance) |             |
| width    |            | [linearDistance](#linearDistance) |             |
| depth    |            | [linearDistance](#linearDistance) |             |

#### linearDistance

| Constraint                                                                                | Type         | Description    |
| ----------------------------------------------------------------------------------------- | ------------ | -------------- |
| pattern: `^-?(\d+km)?(\d+m)?(\d+cm)?(\d+mm)?$`<br>pattern: `^-?(\d+mi)?(\d+ft)?(\d+in)?$` | string, null | 100m<br>2000ft |

## CG Graphics
#### boundingBox
The minimum axis-aligned right rectangular prism in the local space of the Geometry that fully encloses the Geometry.

| Property | Constraint | Type              | Description                                      |
| -------- | ---------- | ----------------- | ------------------------------------------------ |
| corner1  |            | [point3](#point3) | A point representing a corner of a bounding box. |
| corner2  |            | [point3](#point3) | A point representing a corner of a bounding box. |

#### coordinateOrientation
The direction and handedness of the axes used in the geometry.

| Property   | Constraint | Type                    | Description                                                            |
| ---------- | ---------- | ----------------------- | ---------------------------------------------------------------------- |
| handedness | enum       | `"left", "right", null` | A means of expressing a left-handed or right-handed coordinate system. |
| upAxis     | enum       | `"y-up", "z-up", null`  | The elevation axis of 3-dimensional coordinate.                        |

#### levelOfDetail
Percentage of the screen that an object can reasonably take up.

| Constraint         | Type          | Description |
| ------------------ | ------------- | ----------- |
| min: 1<br>max: 100 | integer, null |             |
#### point2
A point with two coordinates.

| Property | Constraint | Type   | Description            |
| -------- | ---------- | ------ | ---------------------- |
| x        |            | number | x coordinate of point. |
| y        |            | number | y coordinate of point. |
#### point3
A point with three coordinates.

| Property | Constraint | Type   | Description           |
| -------- | ---------- | ------ | --------------------- |
| x        |            | number | x coordinate of point |
| y        |            | number | y coordinate of point |
| z        |            | number | z coordinate of point |

#### scale
The number of “real” units represented by a single unit in the coordinate space of the Geometry.

| Constraint | Type                              | Description |
| ---------- | --------------------------------- | ----------- |
|            | [linearDistance](#linearDistance) |             |
### Controlled Values
#### materialType
A categorization of what the material is intended to simulate.

| Value                  |
| ---------------------- |
| gasOrLiquid            |
| gasOrLiquid.atmosphere |
| gasOrLiquid.fire       |
| gasOrLiquid.fog        |
| gasOrLiquid.oil        |
| gasOrLiquid.water      |
| inorganic              |
| inorganic.glass        |
| inorganic.metal        |
| inorganic.plastic      |
| inorganic.stone        |
| organic                |
| organic.fur            |
| organic.hair           |
| organic.leather        |
| organic.plant          |
| organic.scales         |
| organic.skin           |
| organic.wood           |
| textile                |
| textile.cotton         |
| textile.silk           |
| textile.wool           |

#### purpose
A suggested or intended use for the object in a pipeline.

| Value | Description |
|-------|-------------|
| annotation | 3D elements that provide additional information or commentary on other geometry. |
| collision | Simplified geometry for collision detection and physics simulations. |
| general | N/A |
| guide | Geometry used as a visual guide or reference in animation and VFX. |
| matte/paint | Geometry that acts as a background or underlay for visual atmosphere creation. |
| printing | Geometry built as input for a 3D printer process |
| proxy | Lower-resolution geometry used for faster pre-visualization and playback. |
| rendering | Final high-quality visual output of 3D geometry. |

## Versions

#### provenance
A record of when something was changed and by whom.

| Field Name | Constraint | Type                                         | Description |
| ---------- | ---------- | -------------------------------------------- | ----------- |
| CreatedBy  |            | [Participant](../Participant/Participant.md) |             |
| createdOn  |            | [dateTime](#dateTime)                        |             |
| Role       |            | [Role](../Participant/Role.md)               |             |
| Origin     |            | [Asset](../Asset/Asset.md)                   |             |
| reason     |            | string, null                                 |             |
| annotation |            | [ [annotation](#annotation) ]                |             |
