# Shopify 2019 Developer Challenge
# Author: Kashyap Achar
# Date: 2019-01-0-12
# Python Version: 3.7.2
# README available at https://github.com/kashrocks/Shopify-Developer-Challenge

from flask import Flask, jsonify, request

app = Flask(__name__)

# global dictionary of shoes that customer will see
all_shoes = [
    {
        "title": "nike",
        "price": 100,
        "inventory_count": 3
    },
    {
        "title": "adidas",
        "price": 120,
        "inventory_count": 15
    },
    {
        "title": "allbirds",
        "price": 90,
        "inventory_count": 0
    },
    {
        "title": "reebok",
        "price": 60,
        "inventory_count": 30
    }

]

# customers cart initialization
cart = [{}, {'total_value': 0}]


@app.route('/', methods=['GET'])
def welcome():
    # displays the welcome text and complete inventory

    return jsonify({'customer_shopping_cart': cart},
                   {'welc_message': 'Welcome to the greatest backend market '
                                    'place for all things shoes! Please see '
                                    'below for our complete inventory'},
                   {'all_shoes': all_shoes})


@app.route('/inventory', methods=['GET'])
def inventory():
    # displays inventory of shoes only of which have inventory greater than 0

    to_show = []
    for shoe in all_shoes:
        if shoe['inventory_count'] > 0:
            to_show.append(dict.copy(shoe))
    return jsonify({'inventory': to_show})


@app.route('/inventory/<string:brand>', methods=['GET'])
def oneBrand(brand):
    # displays a selected brand of shoe and shows inventory count, price
    # and title

    check = urlcheck(brand)
    if not check:
        return jsonify({'error': 'Invalid brand, please try again.'})
    for shoe in all_shoes:
        if shoe['title'] == brand:
            return jsonify({'brand': shoe})
    return


@app.route('/inventory/<string:brand>/add', methods=['GET'])
def addCart(brand):
    # adds the selected brand to the shopping cart
    # makes sure there is inventory of the shoe

    check = urlcheck(brand)
    if not check:
        return jsonify({'error': 'Invalid brand, please try again.'})

    for shoe in all_shoes:
        if shoe['title'] == brand:
            select = shoe
            break
    if select['inventory_count'] <= 0:
        return jsonify({'error': 'The shoes you have selected are no longer '
                                 'available'})
    elif brand not in cart[0]:
        # adds the brand to the cart if it was not there previously
        cart[0][brand] = 0
    elif select['inventory_count'] == cart[0][brand]:
        # checks to see if there is actually enough inventory for the desired
        # order
        return jsonify(
            {'msg': 'For this brand of shoe, you already have our stores '
                    'inventory worth in your cart. Thus we are unable to '
                    'add more of this brand to your cart.'})

    cart[1]['total_value'] += select['price']  # updates the total value of cart
    cart[0][brand] += 1  # updates quantity of the brand in cart
    return jsonify(
        {'msg': 'The shoes have been added to your cart. Please look at our '
                'other shoes!'})


@app.route('/cart', methods=['GET'])
def showCart():
    # shows customers shopping cart with its total value

    # if the cart is empty will tell customer to shop more
    if cart[1]['total_value'] == 0:
        return jsonify({'msg': 'Your cart is empty. Shop some more!'})
    return jsonify({'customer_cart': cart})


@app.route('/cart/del/<string:brand>', methods=['DELETE'])
def delfrCart(brand):
    # deletes one instance of a brand of shoe from the stores inventory

    check = urlcheck(brand)
    if not check:
        return jsonify({'error': 'Invalid brand, please try again.'})

    for shoe in all_shoes:
        if shoe['title'] == brand:
            s_val = shoe['price']

    for shoe in cart[0]:
        if brand in shoe:
            cart[0][brand] -= 1  # lowers the count of the brand by one
            if cart[0][brand] == 0:
                # if the count is now 0, removes brand from cart
                del cart[0][brand]
            cart[1]['total_value'] -= s_val
            # lowers the value of cart by value of the one brand
            break
    return showCart()


@app.route('/cart/buy', methods=['POST'])
def buyAll():
    # purchases all shoes in the shopping cart and decreases inventory of each

    if cart[0] == {}:  # if cart is empty will display message
        return jsonify({'msg': 'Your cart is empty. Shop some more!'})

    for shoe in all_shoes:  # decreases inventory of respective brand
        if shoe['title'] in cart[0]:
            shoe['inventory_count'] -= cart[0][shoe['title']]

    cart[0], cart[1]['total_value'] = {}, 0  # resets the shopping cart
    return jsonify(
        {'msg': 'The shoes have been purchased and your shopping cart has '
                'been reset. Thanks for shopping!'})


@app.route('/new', methods=['POST'])
def addBrand():
    # adds a new brand of shoe to the stores inventory
    params = request.get_json('Params')

    all_shoes.append(params)  # adds the brand to the story inventory
    return inventory()


@app.route('/del/<string:brand>', methods=['DELETE'])
def delBrand(brand):
    # deletes a brand of shoe from the stores inventory
    check = urlcheck(brand)
    if not check:
        return jsonify({'error': 'Invalid brand, please try again.'})

    for shoe in all_shoes:
        if shoe['title'] == brand:
            # finds index of brand and deletes from inventory
            del all_shoes[all_shoes.index(shoe)]
            break
    return inventory()


def urlcheck(brand):
    # checks to see if the brand entered in url is valid

    for b in all_shoes:
        if b['title'] == brand:
            return True
    return False


if __name__ == '__main__':
    app.run(debug=True, port=6020)
