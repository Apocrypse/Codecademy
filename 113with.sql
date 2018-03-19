WITH previous_query AS (
SELECT customer_id,
       COUNT(subscription_id) as subscriptions
FROM orders
GROUP BY customer_id
)
SELECT customers.customer_name, previous_query.subscriptions
FROM customers
JOIN previous_query
ON previous_query.customer_id = customers.customer_id;
