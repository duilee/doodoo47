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
### _**ERD(Element Relationship Diagram)**_
### _**Data Type**_
### _**With Statment**_
### _**Window Function**_
### _**REGEXP**_
### _**MySQL Function**_
### _**If Statment**_
