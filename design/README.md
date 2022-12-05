# Database Schema

## Programs Overview

Each of the following outline a table prototype. The basic heirarchy of a Program is a tree of Many-To-One relationships in the following order: 

Programs -> Phases -> Workouts -> Rounds -> Exercises

Additionally each Program has a One-To-One relation with a Schedule

## Note: 
>MtO = Many-to-One

## Tables:

### Programs:

| element | type | note |
| --- | --- | --- |
| id | int | primary key |
| name | string | 
| Phases | MtO relation | 
| Schedule | Foreign Key | 

### Phases:

| element | type | note |
| --- | --- | --- |
| id | int | primary key | 
| name| string | 
| objective| string | 
| note| string | 
| expectations | note | 
| frequency | string(?) | 
| Program parent | foreign key |  
| Workouts | MtO relation | 

### Workouts (aka "days")

| element | type | note |
| --- | --- | --- |
| id | int | primary key, id==0 is reserved for rest day| 
| name | string | 
| Phase parent | foreign key| 
| Rounds | MtO relation | 

### Rounds (association table between Workouts and Exercises)

| element | type | note |
| --- | --- | --- |
| id | int | primary key| 
| name| string | 
| Workout parent | foreign key | 
| Exercise | MtM  relation | Unidirectional |
| sets | int | 
| reps | int | 
| rest (inter-set) | duration |
| rest (inter-Round) | duration | 
| Regression Exercise | MtO relation | Null is no regression| 
| optional flag | bool|
| Round SuperSet children | MtO relation | Super set is executed by performing the parent Round, and then recursively performing all child rounds in order |
    
### Exercises

| element | type | note |
| --- | --- | --- |
| id | int | primary key | 
| name| string | 
| equiptment | enum | 
| difficulty | enum | 
| muscle group | int | Actually bitfield? | 
| image path | string | 
| video path | string | 

### Schedules

| element | type | note |
| --- | --- | --- |
| id | int | primary key|
| Program parent | foreign key |
| Schedule_Entrys | MtO relation | Ordered by  Schedule_Entry.order |

### Schedule_Entry (association table between Schedules and Workouts)

| element | type | note |
| --- | --- | --- |
| Schedule parent | foreign key, primary key |
| Workout parent | foreign key, primary key |
| order | int | equivalent to the "day" of the program |



## Links 
- Database structure prototyping: https://docs.google.com/spreadsheets/d/1Su0ZesLQG_JomHWT4xXZbXDonBw7AxLYssfnbZ3_G_g/edit?usp=sharing
- Exercise Index: https://docs.google.com/spreadsheets/d/1JXlsRK79gpSx6e8Mk89UvJKrWkPmOMt3zibdrUzvdqw/edit#gid=0
- Program Example: https://docs.google.com/spreadsheets/d/1GlnAioiR8HL8anQDXIo8aZw8ZLZlqPubG13GqZb7KHU/edit#gid=0
