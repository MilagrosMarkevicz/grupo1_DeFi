/*!
* Start Bootstrap - Blog Home v5.0.9 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
// archivo ajax.js
$(document).ready(function () {
    // Función para enviar una petición POST a la URL especificada
    function enviarPeticion(url, data) {
      return $.ajax({
        url: url,
        type: 'POST',
        data: data,
        dataType: 'json',
      });
    }
  
    // Función para manejar la creación de una nueva publicación
    $('#crear-publicacion-form form').submit(function (event) {
      event.preventDefault();
      const form = $(this);
      enviarPeticion(form.attr('action'), form.serialize())
        .done(function (response) {
          // Actualizar el contenido del bloque "content" con los nuevos datos
          $('#content').html(response.html);
        })
        .fail(function (error) {
          // Manejar errores, si es necesario
        });
    });
  
    // Función para manejar la eliminación de una publicación
    $('.eliminar-publicacion-btn').click(function () {
      const publicacionId = $(this).data('id');
      enviarPeticion('{% url "eliminar-publicacion" 0 %}'.replace('0', publicacionId), {})
        .done(function (response) {
          // Actualizar el contenido del bloque "content" con los nuevos datos
          $('#content').html(response.html);
        })
        .fail(function (error) {
          // Manejar errores, si es necesario
        });
    });
  });
  