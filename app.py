from flask import Flask, jsonify, request

app = Flask(__name__)

# global dictionary of shoes that customer will see
all_shoes = [
    {
        "Title": "nike",
        "Price": 100,
        "Inventory_count": 3
    },
    {
        "Title": "adidas",
        "Price": 120,
        "Inventory_count": 15
    },
    {
        "Title": "allbirds",
        "Price": 90,
        "Inventory_count": 6
    },
    {
        "Title": "reebok",
        "Price": 60,
        "Inventory_count": 30
    }

]

# customers cart
cart = [{}, {'Total value': 0}]


@app.route('/', methods=['GET'])
def welcome():
    # displays the welcome text and complete inventory
    return jsonify({'Your shopping cart': cart},
                   {'welc_message': 'Welcome to the greatest backend market '
                                    'place for all things shoes! Please see '
                                    'below for our complete inventory'},
                   {'all_shoes': all_shoes})


@app.route('/inventory', methods=['GET'])
def inventory():
    # displays inventory of shoes only of which have inventory greater than 0
    to_show = []
    for shoe in all_shoes:
        if shoe['Inventory_count'] > 0:
            to_show.append(dict.copy(shoe))
    return jsonify({'Products': to_show})


@app.route('/inventory/<string:brand>', methods=['GET'])
def oneBrand(brand):
    # displays a selected brand of shoe and shows inventory count, price
    # and title
    check = urlcheck(brand)
    if not check:
        return jsonify({'Error': 'Invalid brand, please try again.'})
    for shoe in all_shoes:
        if shoe['Title'] == brand:
            return jsonify({'Shoe': shoe})
    return



@app.route('/inventory/<string:brand>/add', methods=['GET'])
def addCart(brand):
    # adds the selected brand to the shopping cart
    # makes sure there is inventory of the shoe
    check = urlcheck(brand)
    if not check:
        return jsonify({'Error': 'Invalid brand, please try again.'})

    for shoe in all_shoes:
        if shoe['Title'] == brand:
            select = shoe
            break
    if select['Inventory_count'] <= 0:
        return jsonify('The shoes you have selected are no longer '
                       'available')
    elif brand not in cart[0]:
        cart[0][brand] = 0
    elif select['Inventory_count'] == cart[0][brand]:
        return jsonify('For this brand of shoe, you already have our stores '
                       'inventory worth in your cart. Thus we are unable to '
                       'add more of this brand to your cart.')
    cart[1]['Total value'] += select['Price']
    cart[0][brand] += 1
    return jsonify('The shoes have been added to your cart. Please look at our '
                   'other shoes!')


@app.route('/cart', methods=['GET'])
def showCart():
    # shows customers shopping cart with total value
    if cart[1]['Total value'] == 0:
        return jsonify({'Error': 'Your cart is empty. Shop some more!'})
    return jsonify({'Your cart': cart})


@app.route('/cart/del/<string:brand>', methods=['DELETE'])
def delfrCart(brand):
    # deletes one instance of a brand of shoe from the stores inventory
    check = urlcheck(brand)
    if not check:
        return jsonify({'Error': 'Invalid brand, please try again.'})

    for shoe in all_shoes:
        if shoe['Title'] == brand:
            s_val = shoe['Price']
    for shoe in cart[0]:
        if brand in shoe:
            cart[0][brand] -= 1
            if cart[0][brand] == 0:
                del cart[0][brand]
            cart[1]['Total value'] -= s_val
            break
    return showCart()


@app.route('/cart/buy', methods=['POST'])
def buyAll():
    # purchases all shoes in the shopping cart and decreases inventory of each
    # if cart is empty will display message
    if cart[0] == {}:
        return jsonify({'Error': 'Your cart is empty. Shop some more!'})

    for shoe in all_shoes:
        if shoe['Title'] in cart[0]:
            shoe['Inventory_count'] -= cart[0][shoe['Title']]

    cart[0], cart[1]['Total value'] = {}, 0
    return jsonify('The shoes have been purchased and your shopping cart has '
                   'been reset. Thanks for shopping!')


@app.route('/new', methods=['POST'])
def addBrand():
    # adds a new brand of shoe to the stores inventory
    params = request.get_json('Params')

    all_shoes.append(params)
    return inventory()


@app.route('/del/<string:brand>', methods=['DELETE'])
def delBrand(brand):
    # deletes a brand of shoe from the stores inventory
    check = urlcheck(brand)
    if not check:
        return jsonify({'Error': 'Invalid brand, please try again.'})

    for shoe in all_shoes:
        if shoe['Title'] == brand:
            del all_shoes[all_shoes.index(shoe)]
            break
    return inventory()


def urlcheck(brand: str):
    # checks to see if the brand entered is valid
    for b in all_shoes:
        if b['Title'] == brand:
            return True
    return False



if __name__ == '__main__':
    app.run(debug=True, port=6020)
