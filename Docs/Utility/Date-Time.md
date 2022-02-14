# Measurements of Time

## Date & Time

A date with optional time stamp related to an entity. Can be used to denote start times, end times, creation times and a multiplicity of other uses.

Dates and time should conform to the ISO 8601 standard

| Attribute | **Type** | **Description**                             |
| --------- | -------- | ------------------------------------------- |
| dateTime  | string   | A date and time (2018-11-13T20:20:39+00:00) |
| date      | string   | A date only (2018-11-13)                    |
| time      | string   | A time only (20:20:39+00:00)                |

** *Should we have separate named terms for year, date, time and dateTime - added complication but covers widest 
range of use cases.*
** *Need to provide a more extensive list of examples, use of +- for dates prior to year 0(BC).*
** *Best practices around use of local time or UTC*


    date: yyyy-mm-dd
    year: yyyy
    time: hh:mm:ss
    dateTime: yyyy-mm-dd

**(Missing the 8601 'type' designation (PT, T))

## TimeStamp

The Unix timestamp tracks time as running total of seconds starting from the Unix Epoch of January 1st, 1970 UTC. It is commonly used in computers to generate a number to represent a point in time, and many operating systems, tools and libraries offer a means to convert this to a specific time/date.

| Attribute | **Type** | **Description**                                              |
| --------- | -------- | ------------------------------------------------------------ |
| timestamp | number   | A count of the number of seconds since the Unix Epoch if January 1st, 1970 UTC. |





## Period of Time

A measurement of time from a fixed starting point

| Attribute          | **Type** | **Description**                    |
| ------------------ | -------- | ---------------------------------- |
| startTime/end      | string   | A date and time in ISO 8601 format |
|                    |          |                                    |
| startTime/duration |          |                                    |
| duration/endTime   |          |                                    |
|                    |          |                                    |

** *Make use of ISO 8601 duration naming for the unitOfTime, provide examples (Y, M, W, D, H, etc.)*



## Duration of Time

A duration of time


| **Property** | **Type** | **Description**                       |
| ------------ | -------- | ------------------------------------- |
| durationTime | string   | A duration of time in ISO 8601 format |

The time interval is specified in the following form "PnYnMnDTnHnMnS" where:

- P indicates the period (required)
- nY indicates the number of years
- nM indicates the number of months
- nD indicates the number of days
- T indicates the start of a time section (required if you are going to specify hours, minutes, or seconds)
- nH indicates the number of hours
- nM indicates the number of minutes
- nS indicates the number of seconds



**Pattern**

```
^(-?)P(?=.)((\d+)Y)?((\d+)M)?((\d+)D)?(T(?=.)((\d+)H)?((\d+)M)?(\d*(\.\d+)?S)?)?$
```



**Example**

```JSON
[
    {"durationTime": "P5Y"}, // A duration of 5 years
    {"durationTime": "P5Y2M10DT15H"}, // A duration 5 years, 2 months, 10 days and 15 hours
    {"durationTime": "PT1H15M06S"}, // A duration of 1 hour, 15 minutes and 6 seconds
    {"durationTime": "-PT1H"} // A duration of minus 1 hour
]
```







## Descriptive Time

There are several ways that time or periods in time can be described outside of the literal contexts above.

Many of these relate to the story and script, which may not always make reference to specific dates and times

| **Property** | **Type** | **Description**                                              |
| ------------ | -------- | ------------------------------------------------------------ |
| periodInDay  | string   | Morning, noon, midnight, afternoon, night                    |
| relativeTime | string   | Later, continuous, 6 months earlier, a long time ago         |
| periodInTime | string   | Ming dynasty, World War II, Jurassic period, 20th century    |
| eventInTime  | string   | Hindenburg disaster, World Trade Center Attack, Queen Elizabeth coronation. |

** _Does relative time need a structure that allows for it to relative to some other point in time_




## Timecodes
    SMPTE
    Frame rate (Not sure if this is strictly time)



