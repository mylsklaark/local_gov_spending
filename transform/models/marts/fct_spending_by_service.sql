select year(posting_date) as year, service, sum(net_amount) as net_spend
from {{ ref('stg_spending') }}
group by year, service


