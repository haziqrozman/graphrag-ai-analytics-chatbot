"""
============================================================================================
Script  : graph_schema_prompt.py
Purpose : Defines the graph schema context string injected into the agent prompt,
          describing available vertices, edges, and properties for Gremlin query generation.
============================================================================================
"""

GRAPH_SCHEMA_PROMPT = """
Only use the node labels, edge labels, and properties defined below.
Do not assume any additional nodes, edges, or properties.

Nodes are the following:

- Customer:
    properties:
        - name: customer_key
          type: Int
          description: Unique identifier of the customer node.
        - name: customer_id
          type: Int
          description: Business identifier of the customer.
        - name: customer_number
          type: String
          description: Customer number.
        - name: first_name
          type: String
          description: Customer first name.
        - name: last_name
          type: String
          description: Customer last name.
        - name: country
          type: String
          description: Customer country.
        - name: marital_status
          type: String
          description: Customer marital status.
        - name: gender
          type: String
          description: Customer gender.
        - name: birthdate
          type: Date
          description: Customer birth date.
        - name: create_date
          type: Date
          description: Customer record creation date.

- Product:
    properties:
        - name: product_key
          type: Int
          description: Unique identifier of the product node.
        - name: product_id
          type: Int
          description: Business identifier of the product.
        - name: product_number
          type: String
          description: Product number.
        - name: product_name
          type: String
          description: Product name.
        - name: category_id
          type: String
          description: Product category identifier.
        - name: category
          type: String
          description: Product category.
        - name: sub_category
          type: String
          description: Product sub-category.
        - name: product_line
          type: String
          description: Product line.
        - name: maintenance
          type: String
          description: Product maintenance classification.
        - name: cost
          type: Int
          description: Product cost.
        - name: start_date
          type: Date
          description: Product start or availability date.

Edges are the following:

- PURCHASED:
    from: Customer
    to: Product
    properties:
        - name: order_number
          type: String
          description: Order number of the purchase transaction.
        - name: product_key
          type: Int
          description: Referenced product key in the transaction.
        - name: customer_key
          type: Int
          description: Referenced customer key in the transaction.
        - name: order_date
          type: Date
          description: Order date.
        - name: shipping_date
          type: Date
          description: Shipping date.
        - name: due_date
          type: Date
          description: Due date.
        - name: price
          type: Int
          description: Unit price in the transaction.
        - name: quantity
          type: Short
          description: Quantity purchased.
        - name: sales_amount
          type: Int
          description: Total sales amount for the transaction.

The relationships are the following:
    g.V().hasLabel('Customer').out('PURCHASED').hasLabel('Product'),
    g.V().hasLabel('Product').in('PURCHASED').hasLabel('Customer'),

Canonical graph pattern:
    (Customer)-[PURCHASED]->(Product)

The properties order_number, order_date, shipping_date, due_date, price, quantity, and sales_amount are edge properties on PURCHASED.
When filtering, sorting, or aggregating using these properties, use edge traversals such as outE('PURCHASED') or inE('PURCHASED') rather than vertex property filters.
"""