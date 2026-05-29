select gl_code_id, net_amount
from {{ ref('stg_spending') }}
where net_amount < 500