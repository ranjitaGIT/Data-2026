1. Sales Analytics Azure Databricks + Medallion Architecture Project.

2. Source Data: 4 objects or table data given by the customer.

3. Our responsibility as Data Engineers: ingest source data, clean and validate it, join the tables, calculate business metrics, and publish a Gold table for the Power BI team.

4. Business want from us:
The business wants a Power BI dashboard to answer these questions:
- What is the total sales revenue?
- Which products generate the highest revenue?
- Which customers purchase the most?
- Which regions perform best?
- How many orders are completed, pending, or cancelled? 

5.
Tables are: orders, customers, products and regions.

6. In Silver layer: Silver layer — Cleaned data
Remove duplicates, validate required IDs, standardize dates and data types, and check for invalid prices or quantities.

7 Gold layer — Business-ready data.
Join the 4 Silver tables and calculate sales metrics for reporting.

8.Power BI — Dashboard
Connect to gold_sales_report and build sales, product, customer, and regional dashboards.

9.
Table relationships and column mapping.
silver_orders
Primary business key: order_id
silver_customers
Primary business key: customer_id
silver_products
product_id

10.Source-to-target mapping:
    
Gold column	    Source table.column     	Transformation
order_id	    orders.order_id	            Direct mapping
order_date  	orders.order_date	        Convert to DATE
customer_id 	orders.customer_id	        Direct mapping
customer_name	customers.customer_name	Join on customer_id
region	        customers.region	Join on customer_id
region_manager	regions.region_manager	Join on region
product_id	    orders.product_id	Direct mapping
product_name	products.product_name	Join on product_id
category	    products.category	Join on product_id
quantity	    orders.quantity	Validate positive value
unit_price	    products.unit_price	Validate non-negative price
gross_sales	orders.quantity, products.unit_price	quantity × unit_price
status	        orders.status	Direct mapping

Important business rule: gross_sales is the order value before discounts or taxes. The Power BI team can calculate completed sales by summing gross_sales only where status = 'Completed'. Pending orders should not be counted as completed sales.