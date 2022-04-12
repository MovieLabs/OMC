# Namespaces



*Not sure if we need this anymore*





Namespaces are used to create logical and manageable collections of related entities and properties.

A namespace is unique unto itself, meaning any definitions and structural characteristics only apply within that namespace. However, things from other namespaces can be incorporated and included by reference, thereby extending the original. We typically refer to this a Connected Ontology.

The individual components inside a namespace are typically referred to by their qualified name, e.g., ``mmc:Slate``. The use of the prefix helps to identify and distinguish names of properties, especially as sometimes the same name is used in different namespaces, sometimes with different meaning.

| Prefix | Name                     | URI                          |
| ------ | ------------------------ | ---------------------------- |
| mmc    | MovieLabs Media Creation | https://mc.movielabs.com/mmc |
| mcw    | MovieLabs Creative Works | https://mc.movielabs.com/mcw |



```json
{
    "mmc": "https://mc.movielabs.com/mmc",
    "mcw": "https://mc.movielabs.com/mcw"
}
```



mc.movielabs.com/vocabulary/

[^]: *This includes all vocab terms, ontology and non, as well as other ontology terms, i.e. creative works*

mmc.movielabs.com/ontology/

mmc.movielabs.com/schema/



*Are we including the namespace in the definitions, this reduces overal readabiliity and adds to the payload, but if 
there is a need to expand or use other ontologies in our payloads in the future we are limiting ourselves, if not 
how are we going to include creative works classes now?*

*We could rev the schema version in the future to include namespaces if we need it*

```angular2html
    "mmc:Character": "properties"
    "mcw:Contribution": "properties"
```



