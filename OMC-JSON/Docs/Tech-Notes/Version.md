# Version
In OMC, a “version” is roughly something that is “the same, but different” with respect to some other thing. Many versions can be thought of more precisely, and OMC supports ways to describe both the very coarse “version” and its finer-grained subtypes.  Often the distinction between two versions is clear-cut, but there are cases where a production will have to decide which subtype of version to use is right for them in a particular case.

OMC provides mechanism. It does not prescribe policy about how a production manages versions, or how a MAM manages them. For a full discussion of how OMC thinks of versions please see [OMC](https://mc.movielabs.com/docs/ontology/assets/versions/introduction/) [Part 3B: Versions of Assets](https://mc.movielabs.com/docs/ontology/assets/versions/introduction/) 

All of the subtypes of version can apply to an Asset or an AssetSC, except for Alternative, which only applies to an Asset, but the relationship is always between the same types of entities.

**Version**
A Version is a particular form, variant, or representation of an Asset that differs in some way from its source Asset. The following types of versions are recognized in OMC (and OMC-JSON):

**Revision**
A revision is an alteration to an asset that does not affect its fundamental use in the production. This includes, for example, refinements of drawings and adjustments to props. Revisions can be used to track intermediate phases of this iterative process.

**Variant**
A variant is a change or alteration to an Asset that results in a version of that Asset for use in a different context. For example, a model of a car with dents is a variant of the model of the car without dents.

**Derivation**
A derivation is an Asset that originates from some other source, e.g., by extraction, transformation, or borrowing. Examples include a production prop that is derived from an approved piece of concept art, or a CG curve that is derived from a point cloud.

**Representation**
Some Assets are used in multiple formats, and a representation is an Asset that differs only in technical format or structure from the Asset it represents. For example, a low-res proxy of a video is a representation of a high-res original.

**Alternative**
Sometimes there are multiple Assets, any one of which can be used. OMC calls these alternatives. Alternatives relate to whole assets, such as choosing one of multiple identical props, or asset groups, such as making a choice between two different sets of concept art.


## Standard Version Properties

All types of versions have the following properties:

**versionNumber**
A number or string used by the production to describe the version and differentiate it from other versions of the same object.

**name**
A human readable name to describe the version.

**description**
A human readable (preferably short) description the version.

**annotation**
Additional annotation or notes about the version, for example feedback forom a review of a revision.

**customData**
Additional proprietary data that is not included in the schema’s version object.


## Examples

Both Assets and Asset Structural Characteristics (AssetSC), can be versioned. The semantics for versioning both types are the same (with the exception of Alternate, which is only for Asset). However, a version can only be created of the same thing, i.e. an Asset can only be a version of another Asset and an AssetSC for an AssetSC. The diagrams show some examples of both entity types and how they can be used together.

**Revised AssetSC**
The first example shows a simple revision to an Asset’s Structural Characteristics, the essence. As an example, an image having some requested changes made to it.


- The Asset initially has the essence described by its structural characteristics (astsc-01a).
![](https://paper-attachments.dropboxusercontent.com/s_34BF47D80BCBC543B6735588A935BC1D139214D9BCEA8A02D7322080152DF85B_1695938646206_Version-1a.svg)

- After the image has been updated, the Asset identifier remains unchanged (ast-01), so that anything related to it remains related.
- The Asset now points to new a structural characteristic (astac-01b) that represents the updated image, and it has version information that relates it the prior version (astsc-01a). 
![](https://paper-attachments.dropboxusercontent.com/s_34BF47D80BCBC543B6735588A935BC1D139214D9BCEA8A02D7322080152DF85B_1696283745987_Version-1b.svg)


**Representation**
An AssetSC has a different representation created, for example a thumbnail of the image is created for a UI.

![](https://paper-attachments.dropboxusercontent.com/s_34BF47D80BCBC543B6735588A935BC1D139214D9BCEA8A02D7322080152DF85B_1695938689212_Version-2.svg)


**Single Asset with two different sets of structural characteristics**
This shows a single Asset that exists in two different forms, one digital and one physical. The physical copy might have a barcode or RFID tag that identifies it and a database entry that returns information about its physical location.

In this example, we show a physical image, drawn on paper and the scanned digital copy of this image. This is a good example of how production may apply their own policy, as this could be represented as single Asset where the physical copy has a representation in the digital copy (shown above), or where a new Asset is derived from the first (shown below).

![](https://paper-attachments.dropboxusercontent.com/s_34BF47D80BCBC543B6735588A935BC1D139214D9BCEA8A02D7322080152DF85B_1695938720450_Version-4.svg)


**Alternative** **Asset**
Often there is a desire to create alternative versions of something, so that a choice can be made, for example, two different helmet designs. These two designs are fundamentally different objects, and therefore a new Asset would be created as an alternative to the first.


- Asset (ast-01) is the original Asset.
    - It has AssetSC that is represented by astsc-01b, and a previous revision (astac-01a).
    - AssetSC (astSc-01b) also has a different representation (astac-01br), a thumbnail would be an example of a representation.
- The Art Director wants to see an alternative design based off the first.
    - Asset (ast-02) is created to represent this, it has an AssetSC (astsc-02a)
    - Because the new design is based off the existing one, (astac-02a) was derived from the original astsc-01b.

*Note: The fact that AssetSC (astsc-02a) is derived from the original is optional**. If* *the new alternative* *is* *something new altogether there* *is no* *derived relationship between astsc-01a and astsc-02a.*

![](https://paper-attachments.dropboxusercontent.com/s_34BF47D80BCBC543B6735588A935BC1D139214D9BCEA8A02D7322080152DF85B_1696437578214_Version-3.svg)



















