# Welcome to Kashyaps Online Shoe Market Place
Please use command line to run the python file, this will run a server with the address
 http://127.0.0.1:6020/ . You can interact with the API through Postman using the commands below, entered after the url abvove. Please remember all words are caps sensitive.
## Features - As a customer:
  - Front page - Shows cart and inventory of brands including those with O inventory
    ```````
    GET /
    ```````
  - See whole store inventory - Does not show brands with O inventory
    ```````
    GET /inventory
    ```````
  - See one brand from the inventory (e.g /inventory/nike)
    ```````
    GET /inventory/<brand_name>
    ```````
  - Add one brand to cart (e.g /inventory/nike/add)
    ```````
    GET /inventory/<brand_name>/add
    ```````
  - View the cart
    ```````
    GET /cart
    ```````
  - Delete one instance of a brand from cart (e.g /cart/del/nike)
    ```````
    DELETE /cart/del/<brand_name>
    ```````
  - Purchase all items in the cart
    ```````
    POST /cart/buy
    ```````
## Features - As a store employee:
  - Add a shoe brand to the inventory 
  e.g {"Title" : "nike", "Price": 47, "Inventory_count": 12}
    ```````
    POST /new
    {"Title" : str, "Price": num, "Inventory_count": num}
    ```````
  - Delete a shoe brand from the inventory (e.g /del/nike)
    ```````
    DELETE /del/<brand_name>
    ```````
 