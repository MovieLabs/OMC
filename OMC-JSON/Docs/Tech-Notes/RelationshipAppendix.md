# Relationship Appendix
As described in other [Relationships and Context](RelationshipContext.md), relationships (in the graph and RDF sense) are not native to JSON. OMC-JSON uses two mechanisms to express these.

- When a property is considered an intrinsic to the entity, it is held directly on the entity. Intrinsic properties are named using pascal case (capitalized) indicating an identifier(s) will be part of the value and will refer to the included entities.
- An entity can be related to another as part of a Context, meaning that as part of the production these two entities are meaningful to one another.

In OMC and OMC-RDF relationships carry semantic meaning. For intrinsic properties, OMC-JSON omits the relationship name as it can be inferred by the consuming party. For example, `NarrativeLocation → has.Location → Location` in OMF-RDF would be simply `NarrativeLocation.Location` in OMF-JSON.

With OMC-RDF being class based, sub-class of things are named, for example `Script` is a sub-class of an `AssetFunctionalCharacteristics`. In OMC-JSON, without inheritance, we replace sub-classes with a `type` property, so the Asset entity has `functionalType:` `"``script"`. In OMC-RDF a relationship would be written as `CreativeWork → has → Context → hasScript → Asset`. JSON is often expressed with dot between properties, in OMC-JSON this would read: `CreativeWork.Context.has.Asset`.


In the tables below, each Asset that contains a property that references another is described. The columns are as follows:


- **Property:** The property name. Properties enclosed in brackets indicate an array.
- **Name:** Only used for Contexts. This is the name of the relationship in the Context.
- **Target entity:** The entity or entities that are the target of the relationship.
- **Target Type:** Where the relationship is to specific types, this indicates at least a subset of those types.

**Asset**

| **Property**  | **Name**   | **Target entity**  | **Target type**     |
| ------------- | ---------- | ------------------ | ------------------- |
| [ Asset ]     |            | Asset              |                     |
| AssetSC       |            | AssetSC            | Any structural type |
| [ Context ]   | for        | NarrativeScene     |                     |
|               |            | Sequence           |                     |
|               | has        | NarrativeScene     |                     |
|               |            | Participant        | screenWriter        |
|               |            | Slate              |                     |
|               | represents | ProductionScene    |                     |
|               | usedIn     | ProductionLocation |                     |
|               |            | ProductionScene    |                     |
| [ Depiction ] |            | Depiction          | portrayal           |

----------

**AssetSC**

| **Property** | **Name** | **Target entity** | **Target type**   |
| ------------ | -------- | ----------------- | ----------------- |
| Carrier      |          | Inrastructure     | thumbdrive<br>lto |

----------

**Character**

| **Property**  | **Name**   | **Target entity** | **Target type**                                       |
| ------------- | ---------- | ----------------- | ----------------------------------------------------- |
| [ Context ]   | featuresIn | NarrartiveScene   |                                                       |
|               | needs      | Effect            | sfx, vfx                                              |
|               |            | NarrativeAudio    | narrativeSoundEffect, narrativeMusic                  |
|               |            | NarrativeObject   | narrativeProp, narrativeSetDressing, narrativeVehicle |
|               |            | NarrativeStyling  | narrativeHair,<br>narrativeMakeup                     |
|               |            | NarrativeWardrobe |                                                       |
|               |            | SpecialAction     | stunt, choreography                                   |
| [ Depiction ] |            | Depiction         | portrayal                                             |

----------

**Context**

| **Property** | **Name** | **Target entity**       | **Target type** |
| ------------ | -------- | ----------------------- | --------------- |
| [ Context ]  |          | Context                 |                 |
| [ For ]      |          | Anything with a Context |                 |


**CreativeWork**

| **Property** | **Name** | **Target entity** | **Target type** |
| ------------ | -------- | ----------------- | --------------- |
| [ Context ]  | has      | Asset             | script          |
|              |          | NarrativeScene    |                 |

----------

-**Depiction**

| **Property** | **Name** | **Target entity** | **Target type**                                       |
| ------------ | -------- | ----------------- | ----------------------------------------------------- |
| [ Context ]  | uses     | Asser             |                                                       |
|              | usedIn   | ProductionScene   |                                                       |
| Depicts      |          | Character         |                                                       |
|              |          | NarrativeLocation |                                                       |
|              |          | NarrativeObject   | narrativeProp, narrativeSetDressing, narrativeVehicle |
|              |          | NarrativeStyling  | narrativeHair,<br>narrativeMakeup                     |
|              |          | NarrativeWardrobe |                                                       |
| Dipictor     |          | Asset             |                                                       |
|              |          | Participant       |                                                       |

----------

**Effect**

| **Property**  | **Name**   | **Target entity** | **Target type** |
| ------------- | ---------- | ----------------- | --------------- |
| [ Context ]   | featuresIn | NarrativeScene    |                 |
|               | neededBy   | Character         |                 |
| [ Depiction ] |            | Depiction         | portrayal       |

----------

**Infrastructure**

| **Property**     | **Name** | **Target entity** | **Target type** |
| ---------------- | -------- | ----------------- | --------------- |
| [ Context ]      |          |                   |                 |
| Infrastructure   |          | Infrastrcuture    |                 |
| InfrastructureSC |          | InfrastructureSC  |                 |


**NarrativeAudio**

| **Property**  | **Name**   | **Target entity** | **Target type** |
| ------------- | ---------- | ----------------- | --------------- |
| Context       | featuresIn | NarrativeScene    |                 |
|               | neededBy   | Character         |                 |
| [ Depiction ] |            | Depiction         | portrayal       |

----------

**NarrativeLocation**

| **Property**  | **Name**   | **Target entity** | **Target type** |
| ------------- | ---------- | ----------------- | --------------- |
| [ Context ]   | featuresIn | NarrativeScene    |                 |
| [ Depiction ] |            | Depiction         |                 |
| Location      |            | Location          |                 |

----------

**NarrativeObject**

| **Property**  | **Name**   | **Target entity** | **Target type** |
| ------------- | ---------- | ----------------- | --------------- |
| Context       | featuresIn | NarrativeScene    |                 |
|               | neededBy   | Character         |                 |
| [ Depiction ] |            | Depiction         | portrayal       |

----------

**NarrativeStyling**

| **Property**  | **Name**   | **Target entity** | **Target type** |
| ------------- | ---------- | ----------------- | --------------- |
| [ Context ]   | featuresIn | NarrativeScene    |                 |
|               | neededBy   | Character         |                 |
| [ Depiction ] |            | Depiction         | portrayal       |

----------

**NarrativeWardrobe**

| **Property**  | **Name**   | **Target entity** | **Target type** |
| ------------- | ---------- | ----------------- | --------------- |
| [ Context ]   | featuresIn | NarrativeScene    |                 |
|               | neededBy   | Character         |                 |
| [ Depiction ] |            | Depiction         | portrayal       |

----------

**NarrativeScene**

| **Property** | **Name** | **Target entity** | **Target type**                                       |
| ------------ | -------- | ----------------- | ----------------------------------------------------- |
| [ Context ]  | features | Character         |                                                       |
|              |          | NarrativeAction   |                                                       |
|              |          | NarrativeAudio    | narrativeSoundEffect, narrativeMusic                  |
|              |          | NarrativeEffect   | sfx, vfx                                              |
|              |          | NarrativeLocation |                                                       |
|              |          | NarrativeObject   | narrativeProp, narrativeSetDressing, narrativeVehicle |
|              |          | NarrativeStyling  | narrativeHair,<br>narrativeMakeup                     |
|              |          | NarrativeWardrobe |                                                       |
|              | for      | CreativeWork      |                                                       |
|              | has      | ProductionScene   |                                                       |
|              |          | Asset             |                                                       |

----------

**Participant**

| **Property**    | **Name** | **Target entity** | **Target type** |
| --------------- | -------- | ----------------- | --------------- |
| [ Context ]     | for      | Asset             |                 |
|                 |          | Slate             |                 |
| [ Depiction ]   |          | Depiction         | portrayal       |
| [ Participant ] |          | Participant       |                 |
| ParticipantSC   |          | Person            |                 |
|                 |          | Department        |                 |
|                 |          | Organization      |                 |
|                 |          | Service           |                 |

----------

**ProductionLocation**

| **Property** | **Name** | **Target entity** | **Target type** |
| ------------ | -------- | ----------------- | --------------- |
| [ Context ]  | usedIn   | ProductionScene   |                 |
| Location     |          | Location          |                 |

----------

**ProductionScene**

| **Property** | **Name**      | **Target entity**  | **Target type**                                             |
| ------------ | ------------- | ------------------ | ----------------------------------------------------------- |
| [ Context ]  | for           | NarrativeScene     |                                                             |
|              | has           | Slate              |                                                             |
|              | related       | ProductionScene    |                                                             |
|              | representedBy | Asset              | capture                                                     |
|              | uses          | Asset              | prop, setDressing, greenery, vehicle, costume, hair, makeup |
|              |               | Depiction          |                                                             |
|              |               | ProductionLocation |                                                             |

----------

**Sequence**

| **Property** | **Name** | **Target entity** | **Type** |
| ------------ | -------- | ----------------- | -------- |
| [ Context ]  | for      | ProductionScene   |          |
| SCD          |          | Asset             | scf      |

----------

**Slate**

| **Property** | **Name** | **Target entity** | **Target type** |
| ------------ | -------- | ----------------- | --------------- |
| [ Context ]  | has      | Infrastructure    | camera          |
|              |          | Participant       | cameraUnit      |
|              | for      | Asset             |                 |
|              |          | ProductionScene   |                 |
| CreativeWork |          | CreativeWork      |                 |
| Director     |          | Participant       |                 |

----------

**SpecialAction**

| **Property** | **Name**   | **Target entity** | **Target type** |
| ------------ | ---------- | ----------------- | --------------- |
| [ Context ]  | featuresIn | NarrativeScene    |                 |
|              | neededBy   | Character         |                 |

----------

**Task**

| **Property** | **Name** | **Target entity** | **Target type** |
| ------------ | -------- | ----------------- | --------------- |
| [ Context ]  | has      | NarrativeAction   |                 |
| Task         |          | Task              |                 |
| TaskSC       |          | TaskSC            |                 |






