# Depictions & Portrayals
Depictions are the mechanism used to relate narrative concepts to their production counterparts. Narrative elements are generally depicted by a production asset. A Portrayal is the depiction of a Character.

In the RDF ontology depictions and portrayals are reified relationships. In OMC-JSON we do not need to do this when dealing with objects such as props or locations; we can represent these using a named relationship:
```
NarrativeProp isDepictedBy -> Asset
Asset -> depicts -> NarrativeProp
```
The Asset's ``functionalType`` describes the thing, i.e. a prop or production set.


Portrayals are a little different. A Character may be portrayed by several different people, and it is the combination of a person and their role. For example a character may have a principal actor, a stunt double and someone else doing voiceover work. In addition a person may have more than one role on the production, i.e. and actor/director, the portrayal connects the Participant (the combination of the person with the role of actor) and the Character.

It is necessary to be able to disambiguate all these; for example, you would not want the schedule the voiceover artist instead of the principal actor on the day of a shoot.

Therefore the Portrayal entity combines a Participant and a role.
