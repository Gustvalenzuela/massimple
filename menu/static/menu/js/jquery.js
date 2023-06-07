//PAGINA CREAR CUENTA
$(document).ready(function () {
    $("#form1").submit(function (e) {
        e.preventDefault();
        var nombre = $("#name").val();
        var correoc = $("#email").val();
        var clave = $("#password").val();
        var fecha = $("#fecha").val();

        let msjMostrar = "";
        let enviar = false;

        if (nombre === '' || correoc === '' || clave === '' || fecha === '') {
            alert("Todos los campos son requeridos");
            e.preventDefault();
            return false;
        }

        if (nombre.trim().length < 4 || nombre.trim().length > 10) {                        //validar nombre
            msjMostrar = msjMostrar + "El nombre debe tener entre 4 y 10 caracteres";
            enviar = true;
        }
        else if (/\d/.test(nombre)) {
            msjMostrar += "<br> El nombre no puede contener números";
            enviar = true;
        }

        var letra = nombre.trim().charAt(0);
        if (!esMayuscula(letra)) {
            msjMostrar += "<br>El nombre debe comenzar con mayúscula";
            enviar = true;
        }
        if (isValidEmail(correoc)) {
            enviar = true;

        } else {
            // El correo no es válido, mostrar un mensaje de error
            msjMostrar += "<br> El correo ingresado no es válido";

        }
        if (clave.trim().length < 8) {
            msjMostrar += "<br>La contraseña debe tener al menos 8 carácteres";
            
        }
        else if (!/\d/.test(clave)) {
            msjMostrar += "<br>La contraseña debe contener al menos un número";
            
        }
        else if (!/[a-z]/.test(clave)) {
            msjMostrar += "<br>La contraseña debe contener al menos una letra minúscula";
            

        }
        else if (!/[A-Z]/.test(clave)) {
            msjMostrar += "<br>La contraseña debe contener al menos una letra mayúscula";
            

        }
        else if (!/[!@#$&*]/.test(clave)) {
            msjMostrar += "<br>La contraseña debe contener al menos un carácter especial";
            

        }


        //Validar fecha de nacimiento, no permite menores de edad 

        if (Date.parse(fecha)) {
            var edadMilisegundos = Date.now() - Date.parse(fecha);
            var edad = new Date(edadMilisegundos).getUTCFullYear() - 1970;
            if (edad >= 18) {
                // El usuario tiene al menos 18 años
            } else {
                msjMostrar += "<br>Debes tener al menos 18 años para registrarte";
                enviar = true;
            }
        } else {

        }
        if (enviar) {
            $("#warnings").html(msjMostrar);
        }
        else {
            $("#warnings").html("Ingrese algún dato para continuar");
        }
        

        




    });

    //Función que permite reconocer si la primera letra esta en mayúscula
    function esMayuscula(letra) {
        console.log("Estoy aqui");
        console.log(letra);
        console.log(letra.toUpperCase());

        if (letra == letra.toUpperCase()) {
            return true;
        }
        else {
            return false;
        }
    }
    //Función que permite validar si el correo lleva @ y .
    function isValidEmail(correoc) {
        var pattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return pattern.test(correoc);
    }





});



//PAGINA LOGIN
$(document).ready(function () {
    $("#form2").submit(function (e) {
       

        var correo = $("#correo").val();
        var clave = $("#password").val();


        let msjMostrar = "";
        let enviar = false;

        if (correo == 'amoprogramacion@gmail.com' && clave == 'Taylorswift#13') {
             e.preventDefault();
            // La palabra es correcta, permitir el acceso
            $('#mi-boton').click(function () {
                window.location.href = 'perfilusuario.html';
            });
            msjMostrar += "Bienvenido, haz click nuevamente!";
            enviar = true;

        } else {
            // La palabra no es correcta, mostrar un mensaje de error
            msjMostrar += "<br> El correo ingresado o contraseña son incorrectos";


        }




        if (isValidEmail(correo)) {
            enviar = true;

        } else {
            // El correo no es válido, mostrar un mensaje de error
            msjMostrar += "<br> Incluye un @ para poder continuar"


        }

        if (enviar) {
            $("#warnings").html(msjMostrar);
        }
        else {
            $("#warnings").html("Ingrese algún dato para continuar");
        }
    });

    //Función que permite validar si el correo lleva @ y .
    function isValidEmail(correo) {
        var pattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return pattern.test(correo);
    }


});

//pagina editar perfil

$(document).ready(function () {
    $("#form3").submit(function (e) {
        e.preventDefault();
        var nombre = $("#name").val();
        var correo = $("#email").val();
        var fecha = $("#fecha").val();

        let msjMostrar = "";
        let enviar = false;

        if (nombre.trim().length < 4 || nombre.trim().length > 10) {
            msjMostrar = msjMostrar + "El nombre debe tener entre 4 y 10 caracteres";
            enviar = true;
        }
        else if (/\d/.test(nombre)) {
            msjMostrar += "<br> El nombre no puede contener números";
            enviar = true;
        }

        var letra = nombre.trim().charAt(0);
        if (!esMayuscula(letra)) {
            msjMostrar += "<br>El nombre debe comenzar con mayúscula";
            enviar = true;
        }
        if (isValidEmail(correo)) {
            enviar = true;

        } else {
            // El correo no es válido, mostrar un mensaje de error
            msjMostrar += "<br> El correo ingresado no es válido";

        }




        if (Date.parse(fecha)) {                                                             //Validar fecha de nacimiento, no permite menores de edad 
            var edadMilisegundos = Date.now() - Date.parse(fecha);
            var edad = new Date(edadMilisegundos).getUTCFullYear() - 1970;
            if (edad >= 18) {
                // El usuario tiene al menos 18 años
            } else {
                msjMostrar += "<br>Debes tener al menos 18 años para registrarte";
                enviar = true;
            }
        } else {

        }

        if (enviar) {
            $("#warnings").html(msjMostrar);
        }
        else {
            $("#warnings").html("Su perfil se ha actualizado correctamente");
        }




    });

    //Función que permite reconocer si la primera letra esta en mayúscula
    function esMayuscula(letra) {
        console.log("Estoy aqui");
        console.log(letra);
        console.log(letra.toUpperCase());

        if (letra == letra.toUpperCase()) {
            return true;
        }
        else {
            return false;
        }
    }
    //Función que permite validar si el correo lleva @ y .
    function isValidEmail(correo) {
        var pattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return pattern.test(correo);
    }





});




//cambiar contraseña
$(document).ready(function () {
    $("#form4").submit(function (e) {
        e.preventDefault();

        var antigua = $("#current-password").val();
        var newPassword = $('#new-password').val();
        var confirmPassword = $('#confirm-password').val();

        let msjMostrar = "";
        let enviar = false;



        if (antigua === '' || newPassword === '' || confirmPassword === '') {
            alert("Todos los campos son requeridos");
            e.preventDefault();
            return false;
        }

        if (antigua === 'Taylorswift#13') {

            enviar = true;

            if (newPassword == confirmPassword) {
                msjMostrar += "La contraseña se ha cambiado exitosamente";
                enviar = true;

            } else {
                msjMostrar += "Las contraseñas no coinciden, intente nuevamente ";
                enviar = true;
            }


        } else {
            msjMostrar += "La contraseña actual no es correcta";
            enviar = true;

        }
        //validar contraseña
        if (newPassword.trim().length < 8) {
            msjMostrar += "<br>La contraseña debe tener al menos 8 carácteres";
            enviar = true;
        }
        else if (!/\d/.test(newPassword)) {
            msjMostrar += "<br>La contraseña debe contener al menos un número";
            enviar = true;
        }
        else if (!/[a-z]/.test(newPassword)) {
            msjMostrar += "<br>La contraseña debe contener al menos una letra minúscula";
            enviar = true;

        }
        else if (!/[A-Z]/.test(newPassword)) {
            msjMostrar += "<br>La contraseña debe contener al menos una letra mayúscula";
            enviar = true;

        }
        else if (!/[!@#$&*]/.test(newPassword)) {
            msjMostrar += "<br>La contraseña debe contener al menos un carácter especial";
            enviar = true;

        }
        //Validar si son iguales



        if (enviar) {
            $("#warnings").html(msjMostrar);
        }
        else {
            $("#warnings").html("La contraseña se ha cambiado exitosamente");
        }
    });
});
//recuperar contraseña
$(document).ready(function () {
    $("#form5").submit(function (e) {
        e.preventDefault();
        var correo = $("#email").val();

        let msjMostrar = "";
        let enviar = false;

        if (correo == 'amoprogramacion@gmail.com') {
            msjMostrar += "Se le ha enviado un correo a " + correo + " para recuperar su contraseña";
            enviar = true;
        } else {
            msjMostrar += "El correo ingresado no existe";
            enviar = true;
        }

        if (enviar) {
            $("#warnings").html(msjMostrar);
        }
        else {
            $("#warnings").html("");
        }



    });


});

$(document).ready(function () {
    $("#form6").submit(function (e) {
        
        var id = $("#id").val();
        var nombre = $("#nombre").val();
        var descripcion = $("#descripcion").val();
        var marca = $("#marca").val();
        var stock = $("#stock").val();
        var precio = $("#precio").val();

        let msjMostrar = "";
        let enviar = false;

        if (descripcion.trim().length < 8) {
            e.preventDefault();
            msjMostrar += "<br>La contraseña debe tener al menos 8 carácteres";
            
        }

        if (enviar) {
            $("#warnings").html(msjMostrar);
        }
        else {
            $("#warnings").html("");
        }



    });


});










