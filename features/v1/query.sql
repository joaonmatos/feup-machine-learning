with t as (
    select account_id, count(*) transaction_count, avg(amount) transaction_avg_amount, min(balance) transaction_min_balance,
           max(balance) transaction_max_balance, avg(balance) transaction_avg_balance
    from transactions
    group by account_id
)
select l.date loan_date, l.amount loan_amount, l.duration loan_duration , l.payments loan_payments,
       a.date account_creation, t.transaction_count, t.transaction_avg_amount, t.transaction_min_balance,
       t.transaction_max_balance, t.transaction_avg_balance, l.status loan_status
from loans l
    join accounts a on l.account_id = a.id
    join t on t.account_id = a.id
;
