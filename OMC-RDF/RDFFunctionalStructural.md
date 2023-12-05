## Functional and Structural Classes in RDF

Starting with v2.0, AssetFunctionalClass and AssetStructuralClass have been renamed AssetAsFunction and AssetAsStructure, respectively (and similarly for Tasks and Participants). These classes should be understood as "Asset viewed in terms of its function" and "Asset viewed in terms of its stucture," respectively.

Besides the renaming, more importantly they were made to be subclasses of Asset (or Task or Participant).

The rationale for this is that objects in OWL - that is, instances of OWL classes - are essentially sets of properties. The relevant sets of properties are determined by the classes to which the object belongs. But an object can belong to more than one class.

The intention of AssetFunctionalClass and AssetStructuralClass in previous versions was to separate those properties that pertain to function from those that pertain to structure. However - this being the key point - they remain properties of the asset itself, which has both aspects. Thus, an instance of either of these classes is still an asset - just viewed in a particular way, that is, with a particular set of properties. The asset itself will typically have both function and structural properties; whether it is viewed in terms of its function or in terms of its structure, however, it remains the same asset, and in order to capture this fact, the asset funtional classes and asset structural classes must be made subclasses of the overall class of assets. 

This still allows for a set of structural characteristics to be used by more than one Asset, which is a requirement of OMC, e.g. for an image (structural) to be used as referene art and as a texture for CG work (which are fucntional), or a Person (structural) to be used in multiple Participants, e.g. as  a director and an actor (which are functional.)