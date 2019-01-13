# Welcome to Kashyaps Online Shoe Market Place
 Download all files and make sure the requirements are installed. Once downloaded, please use command line to run the python file by going to the files location in cmd and running command `python app.py`. This will run a server with the address http://127.0.0.1:6020/. You can interact with the API through *Postman*. Put the given url above into the url section of Postman, and use the commands below, **entered after the url above**. Please remember all words are caps sensitive. Please also note, the first slash in all the below is already included in the url. 
## Features - As a customer:
  - Front page - Used to show cart and all brands, including those with O inventory. 
    ```````
    GET /
    ```````
  - See whole store inventory - Does not show brands with O inventory
    ```````
    GET /inventory
    ```````
  - See one brand from the inventory (e.g `/inventory/asics`)
    ```````
    GET /inventory/<brand_name>
    ```````
  - Add one brand to cart (e.g `/inventory/asics/add`)
    ```````
    GET /inventory/<brand_name>/add
    ```````
  - View the cart
    ```````
    GET /cart
    ```````
  - Delete one instance of a brand from cart (e.g `/cart/del/asics`)
    ```````
    DELETE /cart/del/<brand_name>
    ```````
  - Purchase all items in the cart
    ```````
    POST /cart/buy
    ```````
## Features - As a store employee:
  - Add a shoe brand to the inventory 
    ```````
    POST /new
    ```````
    **And** the following code in the body section of Postman
    e.g `{"title" : "asics", "price": 47, "inventory_count": 12}`
    ```````
    {"title" : str, "price": num, "inventory_count": num}
    ```````
  - Delete a shoe brand from the inventory (e.g `/del/asics`)
    ```````
    DELETE /del/<brand_name>
    ```````
 
