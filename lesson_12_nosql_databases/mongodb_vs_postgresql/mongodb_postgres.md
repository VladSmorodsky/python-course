# MongoDB vs Postgres

|                | PostgreSQL                                                                                                                                                                                      | MongoDB                                                                                                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Structure | Use tables to organize data. Data is stored in the form of rows and columns.Require a strict schema definition before inserting data.                                                           | Uses documents (usually in JSON format). Data can have a flexible structure, allowing different formats to be stored in the same collection. Do not require a strict schema definition. |
| Advantages     | Strong support for transactions (ACID). Complex queries and joins between tables. Attractive for structured data with a fixed schema. Many built-in functions for data analysis and processing. | Flexibility in changing data structures (schema-agnostic). Easily scalable horizontally. Optimized for handling large volumes of data and documents.                                    |
| Disadvantages  | Less flexible in changing schemas. May be less performant when dealing with large amounts of unstructured data.                                                                                 | Limited support for transactions (though recently improved). Can be more challenging to perform complex queries without using aggregations. Does not enforce strict data normalization. |

## Summary

The choice between a relational database and a NoSQL database depends on the specifics of the project.
Relational databases like PostgreSQL are suitable for structured data and complex relational queries and where
transaction needs,
while NoSQL solutions like MongoDB provide flexibility and scalability for working with large and varied datasets and
for projects where data structure is unknown. 