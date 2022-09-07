## TASK 3 solution

- Update item_cost of chips to 30

```sql
UPDATE costs
SET item_cost=30
WHERE item_name="chips";
```

- Delete all the rows with maximum item_cost
```sql
DELETE FROM costs WHERE item_cost IN (SELECT max(item_cost) from costs);
```

- Write a query to `find the total number of each item` and check the number of mappers and reducers executed by that query. 
```sql
SELECT item_name, count(*) as x FROM costs GROUP BY item_name
```
> Number of Mappers and Reducers is displayed in terminal.