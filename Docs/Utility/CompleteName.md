





# CompleteName

Describes a Person of Character's complete name or names.

oneOf or anyOf the following may be used.

| Attribute       | **Type** | **Description**                                              |
| --------------- | -------- | ------------------------------------------------------------ |
| firstName       | string   | A person's first name, also refered to as given name         |
| middleName      | string   | A person's middle name or middle initial                     |
| lastName        | string   | A person's last name, also refered to as family name or surname |
| fullName        | string   | A conjunction of firstName, lastName and optionally middleName |
| birthName       | string   | A person’s given name at birth, therefore preceding any later name changes. |
| primaryName     | string   | The name primarily used by the person for credit in work.    |
| pseudonym       | string   | A fictitious name.                                           |
| alternateName   | string   | An alternate name, Also Known As (AKA)                       |
| translatedName  | string   | A translated name, for example a ‘western name’, used by an Asian actor |
| nickname        | string   | An often humorous or familiar name, often given to someone by friends. |
| moniker         | string   | A personal name, similar to a nickname, a name someone often goes by |
| alias           | string   | A false or assumed name, often one the person is better known as |
| contractualName | string   | A name used contractually, which may differ from any of the above |
| displayName     | string   | A name used for display purposes                             |
| sortName        | string   | A name used in sorting, often ‘last, first’                  |
| scriptName      | string   | Used in a script to refer to a character (this is often capitalized) |
| prefix          |          |                                                              |
| suffix          |          |                                                              |



**Mappings**

| mc/cw       | mddf            | schema.or       |
| ----------- | --------------- | --------------- |
| firstName   | FirstGivenName  | givenName       |
| middleName  | SecondGivenName | additionalName  |
| lastName    | FamilyName      | FamilyName      |
| moniker     | Moniker         |                 |
| displayName | DisplayName     |                 |
| sortName    | sortName        |                 |
| suffix      | Suffix          | honorificSuffix |
| prefix      |                 | honorificPrefix |
|             |                 |                 |
|             |                 |                 |

