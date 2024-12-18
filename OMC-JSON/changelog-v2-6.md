### Composition
A new top-level entity type of Composition was added. Compositions are a collection of Assets that when combined according with a set of instructions create a new Asset.

### Character
- `profile.background`: This should now use the annotation utility schema to express values regarding a characters background.

### Context
- `contextCategory`: A new property to allow a canonical way to describe finer grained categorization of a Context then just the `contextType`.
- `idea`: A relationship property to allow for the association of a narrative entity with an asset or composition representing a concept.
- `subject`: A relationship property to allow for the association of an asset or composition representing its narrative subject entity.

### CreativeWork
Additional properties were added to extend functionality and provide more detailed information about the creative work and add support for episodic works.
- `creativeWorkType`: Describes the type or sub-class of creative work (creativeWork, series, season, episode).
- `creativeWorkCategory`: Describes the category of the creative work (movie, tv short).
- `seasonNumber`: The season number of the creative work when applicable.
- `episodeSequence`: The episode sequence description of the creative work when applicable.
- `title`: deprecated in favor of `creativeWorkTitle`.
- `creativeWorkTitle`: The title of the creative work, the structure now provides for adding a language code to the title.
- `Series`: A new intrinsic relationship to relate a creative work to another Creative Work describing the series.
- `Season`: A new intrinsic relationship to relate a creative work to another Creative Work describing the season.
- `Episode`: A new intrinsic relationship to relate a creative work to other Creative Works that are episodes.
- `ProductionCompany`: A new intrinsic relationship to relate a creative work to a company that produced it.

### Depiction
- `Depicter`: Deprecated, spelling was not correct, use `Depictor` instead.
- `Depictor`: Replaces `Depicter`, spelling now aligns with the formal documentation.

Depiction can now have Compositions as the depicted entity, this allows for more complex depictions to be described.

### NarrativeAudio
The property `narrativeType` has new enumerated values to align the naming scheme with other narrative types.
audio -> narrativeAudio
soundEffect -> narrativeSoundEffect
music -> narrativeMusic

### NarrativeAction
NarrativeAction has been renamed to 'SpecialAction'. This was a bug in the 2.0 schema that has been corrected.

### NarrativeLocation
- `narrativeType`: This has a single enumerated value of `narrativeLocation`. This is for consistency with other narrative entities and for any future expansion.

### NarrativeScene
- `narrativeType`: This has a single enumerated value of `narrativeScene`. This is for consistency with other narrative entities and for any future expansion.

### Participant
- `contact`: Deprecated, contact information should be a property of the Participant Structural Characteristics.

### Asset
Formal definitions for asset functional properties were added as controlled values. These are not enumerated, but are considered best practice.

Additional functional properties:
- `audioChannelName` - The name of the audio channel on an audio asset
- `audioMixType` - The type of audio mix
- `audioProcesingAction` - A description of the processing carried out on audio asset
- `mapFormat` - A set of controlled values
- `mapType` - A set of controlled values
- `cameraMetadata` - Properties for camera metadata
- `lensMetadata` - Properties for lens metadata
- `recorderMetadata` - Properties for recorder metadata
- `scd` - Deprecated, now covered by sequences in Composition
- `timing` - Basic timing information for video clip 

### AssetSC
Formal definitions for asset structural properties were added as controlled values. These are not enumerated, but are considered best practice.

Additional structural properties
- `audioBitRate` - The bit rate of the audio
- `audioSampleRate` - The sample rate of the audio
- `audioSampleSize` - The sample size of the audio
- `geometryType` - The type of geometry
- `levelOfDetail` - The level of detail cg 3D assets
- `purpose` - The intended purpose for cg asset
- `scale` - The scale of a cg asset

### Utility
- `tag`: A new property to allow for internal tags to be included along with a domain indicating their source.
- `annotation`: A new property to allow for annotations to be included along with a domain indicating their source.
- `identifier`: The optional properties `combinedForm` and `url` have been added to the identifier property. These can be useful for
utilizing or resolving the identifier in systems.
- `codec` - The codec used for the asset
- `audioContent` - A description for audio assets
- `soundField` - A description of the soundfield for audio assets

## Additional refactoring and bug fixes
- `entityInfo`: Deprecated in favor of `instanceInfo`, which is a more accurate representation of the data that is. 
- `instanceInfo`: Replaces `entityInfo`, and should be considered Beta, it is only available in the OMC-JSON schema and not in the OMC-RDF.
Properties can describe basic info about the instances such as `createdOn, createdBy, lastUpdatedOn, lastUpdatedBy`.

### baseEntity
Entity schema are now created using the union of a baseEntity schema and a schema with properties specific to the entity. This allows for a more consistent structure across all entities.
`tag` and `note` have been added to the baseEntity schema, allowing for these properties to be used across all entities.

### controlledValues
An annotation property `x-controlledValues` has been added to the JSON-Schema in places where a controlled value should be used.
JSON-Schema validators should ignore this property, but it can be used by tools, like the MovieLabs validator, to provide additional information to users.
The `x-` follows an emerging convention for custom annotations in JSON-Schema and is widely adopted in other areas [Custom Annotations Will Continue](https://json-schema.org/blog/posts/custom-annotations-will-continue#how-did-we-arrive-at-as-the-prefix-of-choice).

Controlled values are official defined terms withing OMC, we strongly encourage the use of these when creating OMC instances because,
it allows consumers to understand the meaning of the value. However, these are not enumerated, because it is possible the list does not cover all
possible use cases. They should be used whenever possible, but other values are allowed.

### Schema Refactoring
Some entities had unintentionally been left out of the object representation of OMC, these are now included.

The schema for the array representation now uses if/then rather than oneOf, this provides performance optimizations
and more concise error messages.

Some properties would have failed validation if `null` was provided, this has been fixed.

The schema can now accept a single entity as an object, previously single entities had to be wrapped in an array.

