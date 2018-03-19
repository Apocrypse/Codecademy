SELECT months.month, COUNT(*)
FROM newspaper
CROSS JOIN months
WHERE start_month < month AND end_month > month
GROUP BY months.month;
