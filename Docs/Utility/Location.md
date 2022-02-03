# Location

Location encompass both Physical Locations and Narrative Locations. Physical Locations exists in the real world, they  can have things like coordinates or addresses. Narrative Locations can also exist in the real world, but may also be entirely fictional. However fictional locations may also exhibit properties of physical locations, like having an address.



### Country, Region, Locality

The Country, Region & Locality types follows the schema.org definition https://schema.org/PostalAddress

| Attribute | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| Country   | string | The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). |
| Region    | String | The region in which the locality is, and which is in the country. For example, California or another appropriate first-level |
| Locality  | String | The locality in which the street address is, and which is in the region. For example, Mountain View. |



### Address
The address type follows the schema.org definition https://schema.org/PostalAddress

| Attribute       | Type     | Description                                                  |
| --------------- | -------- | ------------------------------------------------------------ |
| streetAddress   | string   | The street address. For example, 1600 Amphitheatre Pkwy.     |
| addressLocality | Locality | The locality in which the street address is, and which is in the region. For example, Mountain View. |
| addressRegion   | Region   | The region in which the locality is, and which is in the country. For example, California or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country) |
| addressCountry  | Country  | The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). |
|                 |          |                                                              |



### GPS Coordinate

The GPS coordinate type follows the Schema.org definition: https://schema.org/GeoCoordinates

It utilizes WGS 84

| Attribute | Type               | Description                                                  |
| --------- | ------------------ | ------------------------------------------------------------ |
| latitude  | String             | The latitude of a location. For example `37.42242` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). |
| longitude | String             | The longitude of a location. For example `-122.08585` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). |
| elevation | Linear Measurement | (e.g., '1,000 m', '3,200 ft') while numbers alone should be assumed to be a value in meters. |





Geo Coordinates - Ignore for now
