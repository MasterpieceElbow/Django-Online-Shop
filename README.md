# Django-Online-Shop

## Feature list:
* Trigram similarity search on Product and Category
* Session cart
* Recommended items for Product and Products in cart, depends on the products ordered with it. Implemented with Redis
* Category chats. Implemented throught ASGI with WebSockets and channels

## Home page.
* Link to login/logout
* Search form and cart across the site. 
* Category list 

![home_page](https://user-images.githubusercontent.com/80070761/140937441-4f3f09aa-62b8-4b54-9caf-1299b1a2c61b.png)

## List by category
* Category list with badges with products count. Inactive link if there is no product
* Link to category chat right to category name
* Product list by category

![image](https://user-images.githubusercontent.com/80070761/140939431-6c73951b-9ddb-492b-a7b5-d850fbccb315.png)

## Product detail
* Product price, views, description
* Add to a cart form
* Recommended products based on products are ordered with it
* Reviews and a form for review

![product_detail](https://user-images.githubusercontent.com/80070761/141020955-0ac06d1a-9b8b-4e67-9400-8a24ecd7b09b.png)

## Search page
* Searching on Category name, Product name and description
* Searching by PostgreSQL trigram similarity, you don't need exact query to find an item.

![image](https://user-images.githubusercontent.com/80070761/141021952-dd66853c-2c10-438a-9183-46dca232fb20.png)

## Category chat page
* Chat implemented with WebSochet and channels

![image](https://user-images.githubusercontent.com/80070761/141022424-52f77dea-fbcb-4d44-be0c-467f10aa4b76.png)

