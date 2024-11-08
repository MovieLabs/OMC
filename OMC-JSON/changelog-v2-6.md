

### Composition

A new top-level entity type of Composition was added

### Context
`contextCategory` was added as a new property to allow a canonical way to describe finer grained categorization then just the `contextType`.

### CreativeWork
Additional properties were added to extend functionality and provide more detailed information about the creative work and add support for episodic works.
`creativeWorkType`: Describes the type or sub-class of creative work (creativeWork, series, season, episode).
`creativeWorkCategory`: Describes the category of the creative work (movie, tv short).
`seasonNumber`: The season number of the creative work when applicable.
`episodeSequence`: The episode sequence description of the creative work when applicable.
`title`: deprecated in favor of `creativeWorkTitle`.
`creativeWorkTitle`: The title of the creative work, the structure now provides for adding a language code to the title. 
`Series`: A new intrinsic relationship to relate a creative work to another Creative Work describing the series.
`Season`: A new intrinsic relationship to relate a creative work to another Creative Work describing the season.
`Episode`: A new intrinsic relationship to relate a creative work to other Creative Works that are episodes.
`ProductionCompany`: A new intrinsic relationship to relate a creative work to a company that produced it.

### Depiction

The property Depicter used in 2.0 has been deprecated and replaced with Depiction. The schema will continue to support Depicter for backwards compatibility, but it is recommended that new implementations use Depictor.
This was an spelling error that was corrected, and now aligns with the formal documentation.

Depiction can now have Compositions as the depicted entity, this allows for more complex depictions to be described.

### NarrativeAudio
The property `narrativeType` has new enumerated values to align the naming schema with other narrative types.
audio -> narrativeAudio
soundEffect -> narrativeSoundEffect
music -> narrativeMusic

### NarrativeAction

NarrativeAction was the development name, the release version should have been 'SpecialAction'. NarrativeAction has been deprecated and replaced with SpecialAction. The schema will continue to support NarrativeAction for backwards compatibility, but it is recommended that new implementations use SpecialAction.

### NarrativeLocation
The property `narrativeType` was added, with a single enumerated value of `narrativeLocation`. This is for consistency
with other narrative types and for any future expansion of the narrative types.

### NarrativeScene
The property `narrativeType` was added, with a single enumerated value of `narrativeScene`. This is for consistency
with other narrative types and for any future expansion of the narrative types.

### identifier
The optional properties `combinedForm` and `url` have been added to the identifier property. These can be useful for
utilizing or resolving the identifier in systems.  

### Asset
Formal definitions for asset functional properties:

- `mapFormat` - A set of controlled values
- `mapType` - A set of controlled values
- `cameraMetadata` - Properties for camera metadata
- `lensMetadata` - Properties for lens metadata
- `recorderMetadata` - Properties for recorder metadata

### Utility
`tag`: A new property to allow for internal tags to be included along with a domain indicating their source.


## Additional refactoring and bug fixes

`entityInfo`: Deprecated in favor of `instanceInfo`, which is a more accurate representation of the data that is. 
`instanceInfo`: Replaces `entityInfo`, and should be considered Beta, it is only available in the OMC-JSON schema and not in the OMC-RDF.
Properties can describe basic info about the instances such as `createdOn, createdBy, lastUpdatedOn, lastUpdatedBy`.

### baseEntity
Entity schema are now created using the union of a baseEntity schema and a schema with properties specific to the entity. This allows for a more consistent structure across all entities.
`tag` and `note` have been added to the baseEntity schema, allowing for these properties to be used across all entities.

#### controlledValue
A new annotation property `controlledValues` has been added to multiple properties.

Controlled values signify values for this property are official terms we encourage the use of when constructing
controlled OMC instances. However, these are not enumerated, because it is possible the list does not cover all
possible values. They should be used whenever possible, but other values are allowed.



### Schema Refactoring
Some entities had unintentionally been left out of the object representation of OMC, these are now included.

The schema for the array representation now uses if/then rather than oneOf, this provides performance optimizations
and more concise error messages.

All entities now share a base schema that is extended, this provides a simplification of the schema itself and ensures
that all entities are consistent in their structure.

Some properties would have failed validation if `null` was provided, this has been fixed.

The schema can now accept a single entity as an object, previously single entities had to be wrapped in an array.