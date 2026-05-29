select year(posting_date) as year, supplier_description, sum(net_amount) as net_spend
from {{ ref('stg_spending') }}
group by year, supplier_description