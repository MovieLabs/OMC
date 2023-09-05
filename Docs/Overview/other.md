



Notes about reification and this being a way of grouping of things
#### Reification
Reification is the process of taking an abstract idea or concept and making it something concrete. In graphs and RDF this is often done with a relationship, RDF does not support having properties on a relationship itself, so a new intermediate node is created to express the concepts you wish to associate with that relationship.

The ontology uses this in a number of places, Context, Depiction/Portrayal, Participants.

For example a if a person is working on production we could just simply relate that person directly to the scenes they appear in, the characters they play or the locations they need to be at, but often there is more information that we need to convey than simply that they appear in something. We probably want to know why they appear, or what they are supposed to be doing. Using a Participant allows to us associate other information, such as their Role. The same Person may be both acting and directing in a film, by having two Participants we can separate the different responsibilities,  if they are acting in a scene their call sheet will be different than if they were only directing.

A Portrayal (a sub-class of Depiction) is another example. An actor portrays a Character, but often a character is portrayed by multiple actors, the stunt person, body double, voiceover, in the cg model. Which of these portrayals is needed on any given day and for what tasks will different. Another example is a character that has different manifestations, werewolf to human form, for example. Each of these a different portrayal of the same character, by the same actor but the werewolf will have very different requirements for makeup, costume, etc.


Notes about relationship naming conventions

#### Sub-Classing
JSON does not support the concept of classes, nor sub-classing, which RDF model uses extensively. Therefore the JSOM implementation uses a type property on some entities that allow the sub-class to be expressed. This was done in large part to help manage the schema overall, and not require every sub-class to need to be expressed as it's own entity.

For example in RDF a parent class of NarrativeObject has various sub-classes NarrativeProp, NarrativeSetDressing, NarativeGreenery, etc.

```
NarrativeObject: {
	entityType: "NarrativeObject",
	narrativeType: "prop"
}
```


#### Schema Simplifications

Some structures in JSON are only represented as a hierarchy, notably groups such as Asset groups and Participant groups. In JSON a hierarchy is inherently part of the structure, as one object can be nested inside another meaning it's relationship is easily inferred and does not need to be expressed.

Where this is used it is presumed that the consuming application can infer the relationship (and name) and recreate the graph if it so desires.

A similar pattern is used when an entity has a property that is another entity. In this case a consuming application can infer the relationship. For example, and Asset has the property ParticipantSC which is a direct reference to entity that represent the structural class.


A graph represent this with a relationship
```
(Asset) -> [has] - (AssetSC)
```

The JSON schema represents this as follows and the relationship is inferred.
```
Asset: {
	AssetSC: {
		entityType: "AssetSC"
		identifier: [{
			identifierScope: "scope"
			identifierValue: "value"
		}]
	}
}
```
