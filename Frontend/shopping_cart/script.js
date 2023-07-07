function showModal(productId) {
    var product = {
        title: "Product " + productId,
        description: "This is a description of Product " + productId + ".",
        price: "$" + (5 * productId)
    };

    document.getElementById("product-modal-title").textContent = product.title;
    document.getElementById("product-modal-description").textContent = product.description;
    document.getElementById("product-modal-price").textContent = product.price;
    document.getElementById("product-modal").style.display = "block";
}

function addToCart(productName) {
    var cartItem = document.createElement("div");
    cartItem.className = "cart-item";
    cartItem.innerHTML = `
    <div class="cart-item-name">${productName}</div>
        <div class="cart-item-actions">
          <button onclick="decreaseQuantity(this)">-</button>
          <span class="cart-item-quantity">1</span>
          <button onclick="increaseQuantity(this)">+</button>
        </div>
      `;
    document.getElementById("cart-items").appendChild(cartItem);
}

function increaseQuantity(button) {
    var quantityElement = button.parentNode.querySelector(".cart-item-quantity");
    var quantity = parseInt(quantityElement.textContent);
    quantity++;
    quantityElement.textContent = quantity;
}

function decreaseQuantity(button) {
    var quantityElement = button.parentNode.querySelector(".cart-item-quantity");
    var quantity = parseInt(quantityElement.textContent);
    if (quantity > 1) {
        quantity--;
        quantityElement.textContent = quantity;
    }
}
