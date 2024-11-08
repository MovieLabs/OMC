Common data models and data structures used in multiple places and in multiple ways in a larger system.
#### address


#### annotation

| Field Name | Operator | Type         | Description                         |
| ---------- | -------- | ------------ | ----------------------------------- |
| author     |          | string, null | Who wrote or added this annotation  |
| title      |          | string, null | A title for the note or annotation. |
| text       |          | string, null | The text of the note or annotation. |

#### basicName


#### boundingBox
The minimum axis-aligned right rectangular prism in the local space of the Geometry that fully encloses the Geometry.

| Field Name | Operator | Type              | Description |
| ---------- | -------- | ----------------- | ----------- |
| corner1    |          | [point3](#point3) |             |
| corner2    |          | [point3](#point3) |             |

#### completeName
A detailed description of a person, or other entities, name and variants of their name.

| Field Name          | Operator | Type             | Description                                                                                                                            |
| ------------------- | -------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| firstGivenName      |          | string,&nbspnull | A person's first name, also referred to as given name.                                                                                 |
| secondGivenName<br> |          | string,&nbspnull | A persons second given name, also referred to as middle name.                                                                          |
| familyName          |          | string,&nbspnull | A persons family name, also referred to as surname.                                                                                    |
| fullName            |          | string,&nbspnull | A complete name, typically a conjunction of familyName, firstGivenName and possibly other fields.                                      |
| birthName           |          | string,&nbspnull | A persons name at birth, also referred to as maiden name.                                                                              |
| primaryName         |          | string,&nbspnull | A persons primary name, one they typically use, also often a combination of first, second and family name.                             |
| pseudonym           |          | string,&nbspnull |                                                                                                                                        |
| altName             |          | string,&nbspnull |                                                                                                                                        |
| translatedName      |          | string,&nbspnull |                                                                                                                                        |
| nickname            |          | string,&nbspnull |                                                                                                                                        |
| moniker             |          | string,&nbspnull |                                                                                                                                        |
| alias               |          | string,&nbspnull | An alias being used by a person often used to disguise someones real identity, sometimes used when booking hotel rooms or restaurants. |
| contractualName     |          | string,&nbspnull |                                                                                                                                        |
| displayName         |          | string,&nbspnull |                                                                                                                                        |
| sortName            |          | string,&nbspnull |                                                                                                                                        |
| scriptName          |          | string,&nbspnull |                                                                                                                                        |
| prefix              |          | string,&nbspnull | A prefix that can indicate a persons gender or title.                                                                                  |
| suffix              |          | string,&nbspnull | A suffix, often used to indicate a title or classification                                                                             |


#### contact


#### coordinates




#### coordinateOrientation
The direction and handedness of the axes used in the geometry.

| Field Name | Operator | Type                    | Description                      |
| ---------- | -------- | ----------------------- | -------------------------------- |
| handedness | enum     | `"left", "right", null` | The handedness of the third axis |
| upAxis     | enum     | `"y-up", "z-up", null`  |                                  |
#### country

| Field Name | Operator | Type | Description |
| ---------- | -------- | ---- | ----------- |
|            |          |      |             |

#### customData


#### email



#### gender


#### identifier

| Field Name | Operator | Type                                          | Description                                                            |
| ---------- | -------- | --------------------------------------------- | ---------------------------------------------------------------------- |
| identifier |          | [&nbsp[identifierItem](#identifierItem)&nbsp] | An identifier uniquely identifies an entity within a particular scope. |

#### identifierItem

| Field Name      | Operator | Type   | Description                                                                                              |
| --------------- | -------- | ------ | -------------------------------------------------------------------------------------------------------- |
| identifierScope | required | string | The universe within which an identifier is valid and unique.                                             |
| identifierValue | required | string | A string of characters that uniquely identifies an object within a particular scope.                     |
| combinedForm    |          | string | A combination of the Identifier Scope and Value that is useful for utilizing the identifier in a system. |
| url             |          | string | A URL or IRI that can be used for resolving the Identifier Value within the Identifier Scope.            |

#### language


#### levelOfDetail
Percentage of the screen that an object can reasonably take up.

| Field Name | Operator           | Type          | Description |
| ---------- | ------------------ | ------------- | ----------- |
|            | min: 1<br>max: 100 | integer, null |             |

#### materialType




#### point2
A point with two coordinates.

| Field Name | Operator | Type   | Description           |
| ---------- | -------- | ------ | --------------------- |
| x          |          | number | x coordinate of point |
| y          |          | number | y coordinate of point |
#### point3
A point with three coordinates.

| Field Name | Operator | Type   | Description           |
| ---------- | -------- | ------ | --------------------- |
| x          |          | number | x coordinate of point |
| y          |          | number | y coordinate of point |
| z          |          | number | z coordinate of point |

#### provenance


#### purpose
A suggested or intended use for the object in a pipeline.

| Field Name | Operator  | Type         | Description |
| ---------- | --------- | ------------ | ----------- |
|            | ctrlValue | string, null |             |

| Value       | Definition                                                                       |
| ----------- | -------------------------------------------------------------------------------- |
| annotation  | 3D elements that provide additional information or commentary on other geometry. |
| collision   | Simplified geometry for collision detection and physics simulations.             |
| general     |                                                                                  |
| guide       | Geometry used as a visual guide or reference in animation and VFX.               |
| matte/paint | Geometry that acts as a background or underlay for visual atmosphere creation.   |
| printing    | Geometry built as input for a 3D printer process                                 |
| proxy       | Lower-resolution geometry used for faster pre-visualization and playback.        |
| rendering   | Final high-quality visual output of 3D geometry.                                 |


#### scale

#### tag


#### telephone


#### time



#### unitOfMeasurement

#### versionNumber



## Reference

Description of reference