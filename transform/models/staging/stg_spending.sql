with

source as (

    select * from {{ source('occ_spending', 'raw_spending') }}

),

renamed as (

    select
        "Supplier: Description" as supplier_description,
        "Document Number" as document_number,
        "Posting Date" as posting_date,
        case when "Service" = '' then 'Uncategorised' else "Service" end as service,
        "GL Code: ID" as gl_code_id,
        "GL Code: Description" as gl_code_description,
        cast("Net Amount" as decimal) as net_amount
    from source

)

select * from renamed