# Depictions & Portrayals
Depictions are a mechanism used to relate narrative concepts to their production counterparts, narrative elements are generally depicted by a production asset. A Portrayal is the depiction of a Character.

In the RDF ontology depictions and portrayals are reified relationships. In OMC-JSON we do not need to do this when dealing with objects such as props or locations, we can represent these using a named relationship:
```
NarrativeProp isDepictedBy -> Asset
Asset -> depicts -> NarrativeProp
``` 
The Assets ``functionalType`` describes the thing, i.e. a prop or production set.


Portrayals are a little different, a Character may be portrayed by several different people, and it is the combination of a person and their role. For example a character may have a principal actor, a stunt double and someone else doing voiceover work. In addation a person may have more than one role on the production, i.e. and actor/director, the portrayal would the combination of the person with the role of actor.

It is necessary to be able to disambiguate all these, you would not want the schedule the voiceover artist instead of the principal actor on the day of a shoot.

Therefore the Portrayal entity combines a Participant and a role.
