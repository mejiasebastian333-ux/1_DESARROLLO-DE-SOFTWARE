// Array
Un array es una lista ordenada de elementos indexados. 
- Cada elemento tiene una posición (índice).

// Objeto
colección de pares clave-valor.

// Array de objetos
lista ordenada donde cada elemento es un objeto.


=========================================================


// foreach 

Primero definimos un arreglo llamado productos. Este arreglo contiene varios objetos, y cada objeto representa un producto con tres propiedades: el id, el nombre y el precio.

Después usamos el método .forEach(). Este método sirve para recorrer todos los elementos de un arreglo y ejecutar una acción con cada uno de ellos. En este caso, la acción que queremos es mostrar en la consola el nombre del producto y su precio.
Dentro de .forEach(), usamos una función flecha que recibe cada objeto del arreglo como parámetro, al que llamamos p. Con ese objeto, accedemos a sus propiedades nombre y precio, y las combinamos en un mensaje usando plantillas de texto.

El resultado es que el código imprime en la consola una línea por cada producto, mostrando su nombre y cuánto cuesta. Es decir, el arreglo completo se recorre y se transforma en una lista de mensajes legibles.


=========================================================


// Ejemplo práctico: Tienda de productos

Primero, definimos un arreglo llamado carrito. Este arreglo contiene varios objetos, y cada objeto representa un producto con tres propiedades: el nombre del producto, la cantidad que se está comprando y el precio unitario. En este caso tenemos dos productos: café y pan, con sus respectivas cantidades y precios.

Luego, usamos el método .reduce(). Este método sirve para recorrer todo el arreglo y acumular un resultado. Lo que hacemos aquí es calcular el total a pagar. Para cada producto, multiplicamos la cantidad por el precio, y ese resultado lo vamos sumando en un acumulador que empieza en cero. En la primera vuelta, el acumulador suma el costo del café, y en la segunda vuelta suma el costo del pan. Al final, el acumulador contiene el total de la compra.

Finalmente, mostramos ese total en la consola con console.log. Usamos una plantilla de texto para que el mensaje se vea claro, diciendo “Total: $16”.


=========================================================


DOM

Primero, en el HTML tenemos una lista vacía con el identificador lista. Luego, en el código JavaScript definimos un arreglo de objetos llamado productos, donde cada objeto representa un producto con su nombre y su precio.
Después, usamos document.getElementById("lista") para obtener la referencia al elemento <ul> en el DOM. Con esa referencia podemos manipular la lista desde JavaScript.
A continuación, recorremos el arreglo con .forEach(). Para cada producto, creamos un nuevo elemento de lista (<li>), le asignamos un texto que combina el nombre y el precio, y finalmente lo agregamos dentro del <ul> usando appendChild.
El resultado es que la lista que estaba vacía en el HTML se llena dinámicamente con los productos y sus precios. Es decir, el código transforma datos de un array de objetos en contenido visible en la página.


=========================================================


APIs

Primero, en el HTML tenemos una lista vacía con el identificador lista. Luego, en el código JavaScript definimos un arreglo de objetos llamado productos, donde cada objeto representa un producto con su nombre y su precio.
Después, usamos document.getElementById("lista") para obtener la referencia al elemento <ul> en el DOM. Con esa referencia podemos manipular la lista desde JavaScript.
A continuación, recorremos el arreglo con .forEach(). Para cada producto, creamos un nuevo elemento de lista (<li>), le asignamos un texto que combina el nombre y el precio, y finalmente lo agregamos dentro del <ul> usando appendChild.
El resultado es que la lista que estaba vacía en el HTML se llena dinámicamente con los productos y sus precios. Es decir, el código transforma datos de un array de objetos en contenido visible en la página.
