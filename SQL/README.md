## SQL notes
### _**Data Query Lanaguage**_
- SELECT
	>SELECT * // column name or names seperated by comma  
	FROM customers 
- LIMIT
	>SELECT * // column name or names seperated by comma  
	FROM customers   
	LIMIT 2 // show only two  == HEAD(2)
- WHERE
	>SELECT * // column name or names seperated by comma  
	FROM customers   
	WHERE CONDITION // i.e. columnname = 'some string'  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// COND OR/AND COND  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// =, <>, <=, >=  
	LIMIT 2 // show only two  == HEAD(2)
- LIKE
	>WHERE columnname LIKE 'br%' // % any string after, _ wildcard for one character  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// RLIKE to use regular expression  
	 WHERE columnname IN ('Germany', 'France')  
	 WHERE columnname BETWEEN a AND b  
	 WHERE columnname IS NULL  
- DISTINCT
	> SELECT DISTINCT(columname)
- ORDER BY
	> ORDER BY columnname  DESC/ASC(default)
- SUBSTR, LEFT, RIGHT
	> SUBSTR(columnname, start_position, length)  
	LEFT(columnname, length) // from left  
	RIGHT(columnname, length) // from right  
- Decimal control
	> CEIL() // CEIL(3.3) => 4  
	FLOOR() // FLOOR(3.6) => 3  
	ROUND(number, digits) // ROUND(3.142592, 2) => 3.14

- Aggregation
	>COUNT(colmnname) // count except NULL, COUNT(*) => count all  
	COUNT(DISTINCT columnname) // to count distinct values  
	SUM, AVG, MIN, MAX

- GROUP BY
	>SELECT *   
	FROM customers  
	GROUP BY reference_column // can also have multiple columns  
	HAVING condition // after GROUP BY use HAVING instead of WHERE  
- AS (Use as to add short call name)
- CASE
	> SELECT CASE  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; WHEN condition THEN sth // add desired result here  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; WHEN condition THEN sth  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ...  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; END  
- JOIN, INNER JOIN, OUTER LEFT/RIGHT JOIN
	>SELECT *  
	FROM customers  
	INNTER JOIN datatable_name ON condition // RIGHT JOIN or LEFT JOIN also possible  
- UNION
	>SELECT *  
	FROM customers 2  
	UNION  
	SELECT *  
	FROM cusomers 1  
	// ORDER BY should always come at the last  
	// UNION takes distinct values only, so use UNION ALL to include all  
- DATE functions
	> DATE_ADD() // for addition  
	DATE_SUB() // for subtration  
	DATE() // get the date only, HOUR, DAY, YEAR, MONTH all available
	
### _**Data Manipulation Language**_
- INSERT
	> INSERT INTO table_name VALUES (value_list);
	INSERT INTO table_name (column_list) VALUES (value_list);
- UPDATE
	> UPDATE table_name SET column = value;
	UPDATE table_name SET column = value WHERE cond;
- DELETE 
	> DELETE FROM table_name WHERE cond

### _**SubQuery**_
- SubQuery uses queried result within new query
	> SELECT sub.column_name  
	, AVG(sub.column_name)  
	FROM(  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SELECT colum_name  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FROM original_table  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GROUP BY column_name, column_name  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;) sub  
	WHERE ..  
	GROUP BY ...  
	> WHERE column_name = (SELECT MIN(column_name) FROM table)  
	WHERE column_name IN (SELECT column_name FROM table ORDER BY column_name DESC LIMIT 5)  
	
### _**ERD(Element Relationship Diagram)**_
- Consists of Entity, Attribute, and Relationship
	> [<img src="ERD.png" width="400"/>](ERD.png)  
	> -l-l-  = ONE  
	o<- = Many
	
### _**Data Type**_
- Integer : tinyint(), smallint(), mediumint(), int(), bigint()  
float: decimal(), double(), float()  
- chracter: varchar(), char()
- string to datetime: str_to_date()

### _**With Statment**_
- Use with for repetitive use of query
	> WITH subquery AS (  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SELECT ...  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; FROM ...  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ...  
	
### _**Window Function**_
- windon functions include SUM, AVG, COUNT, ROW_NUMBER(), RANK(), DENSE_RANK()
	> Function(column) OVER (PARTITION BY column_name ORDER BY column_name)
- LEAD(column_name, step, null_value) OVER (ORDER BY column_name) AS 'alias'; // move one up  
  LAG() // move one down

### _**REGEXP**_
- https://regexr.com/
- https://regexone.com/lesson/introduction_abcs

### _**MySQL Function**_
- FORMAT goes...
	> CREATE FUNCTION 'function name' ('parameter_name', 'datatype')  
	RETURN 'datatype' (DETERMINISTIC) // to get consistant output for same input  
	BEGIN  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DECLARE 'variable name' 'datatype'  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SET ;  
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RETURN (variable name)  
	END  

### _**If Statment**_
- if statement goes ...
	> IF (condition, value if True, value if False)

### _**More LIMIT**_
- more LIMIT usage!
	> LIMIT 5, 10 //row from 6~15  
	LIMIT 5, 1 // row 6  
	LIMIT N, 1 // row n+1  
	LIMIT 1 OFFSET N // row n+1  
