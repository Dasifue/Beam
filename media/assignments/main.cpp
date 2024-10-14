#include <iostream>
#include <string>
#include <vector>

#include "include/product.h"
#include "include/cart.h"
#include "include/wallet.h"
#include "include/user.h"


int main(){

    Product banana("Banana", "Fruits", 120.0);
    Product potato("Potato", "Vegetables", 30.5);
    Product meat("Beef", "Meat", 500);

    std::vector<Product> products{banana, potato, meat, banana};

    Cart cart;
    cart.addToCartMany(products);
    cart.removeProduct(banana);

    for (Product& product: cart.getProducts()) {
        std::cout << product.getName() << " " << product.getPrice() << std::endl;
    }
    return 0;
}