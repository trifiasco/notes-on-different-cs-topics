### Difference Between Stored Procedure and Functions

From [Stackoverflow answer](https://stackoverflow.com/a/1179778/9041122) - 

Functions are computed values and cannot perform permanent environmental changes to SQL Server (i.e. no INSERT or UPDATE statements allowed).

A function can be used inline in SQL statements if it returns a scalar value, or can be joined upon if it returns a result set.

A point worth noting from comments, which summarize the answer. Thanks to @Sean K Anderson:

`Functions follow the computer-sciency definition in that they MUST return a value and cannot alter the data they receive as parameters (the arguments). Functions are not allowed to change anything, must have at least one parameter, and they must return a value. Stored procs do not have to have a parameter, can change database objects, and do not have to return a value.`