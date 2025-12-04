This 2.8 version includes all updates to the formal v2.7 spec as well as additions and updates from v2.8

### Asset
Additional functional types (classes):
- `cgPointCloud` - A set of data points in 3D space
- `cgRig.biped`- A CG Rig for something that walks on two feet.
- `cgRig.quadruped` - A CG Rig for something that walks on four feet.
- `cgRig.polyped`- A CG Rig for something that walks on more than four feet.
- `cgRig.avian` - A CG Rig for something whose motion is bird like.
- `cgRig.serpentine` - A CG Rig for something that slithers.
- `cgRig.appendage` - A CG Rig for a separately controlled extension.
- `material.shader` - A programmable or software-defined Material.
- `cgVolume` - A volume used in a CG pipeline.
- `udimTile` - A numbered sub-piece of a UV Map.

Additional functional properties:
- `audioTrackName` - Further differentiation for the Audio Track.
- `udimTileNumber` - A numbered sub-piece of a UV Map.
- `cgVolumePurpose` - The intended use of a CG Volume in the CG pipeline.
- `mapFormat` - New vocabulary was added ('emissive' and 'emissiveColor').

### AssetSC
Additional structural types (classes):
- `digital.volume` - A non-mesh representation of 3D data.
- `digital.pointCloud` - A set of data points in 3D space.

Additional structural properties:
- `numberPoints` - The number of individual points in the point cloud.
- `axisAligned` - True if the volume is aligned with the three axes of the coordinate space.

### Composition
Additional composition properties:
- `materialType` - A categorization of what the material is intended to simulate.

### Collection
A new top-level entity type of Collection was added. Collections are a mechanism for grouping any OMC entities into a named collection for organizational purposes

### Service
- `software` - New property (see below).

### software
A new utility object, used to describe a piece, or pieces, of software that are coupled with a particular entity.
This is a high level description only, and not intended to be able to drive automated configuration or workflows, but rather assist someone in either determining what created something or guide the setup their own environment.
It is a property of Composition, AssetSC, Service
- `softwareName` - The name of the software.
- `softwareVersion` - A version ascribed to the software that was used.
- `apiVersion` - For applications or SAAS services where an API is used.
- `plugin` - A list of required plugins, these are also software.
- `operatingSystem` - he operating system that used, which is 'software.
- `parameters` - Parameters used when executing the software, such as in a command line.
- `configurationFile`: Optional reference to an file(Asset) containing additional configuration or other information.

### customData
This has now been formalized with some structure to allow multiple parties to add custom data and the source of the
data to be understood and disambiguated from other sources.
- `domain` - Indicates the set or system in which the custom data is relevant or defined.
- `namespace` - The namespace used by the custom data.
- `schema` - URL for the schema used by the custom data.
- `value` - The user defined custom data.
