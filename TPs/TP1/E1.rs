/*
Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.
*/
use std::io;

fn input_number(message: &str) -> Vec<u8> {
    let mut data = Vec::new();
    while data.len() < 3 {
        let n: u8;
        let mut str = String::new();
        println!("{} {}:", message, data.len() + 1);
        io::stdin()
            .read_line(&mut str)
            .expect("No se pudo leer el input.");
        match str.trim().parse::<u8>() {
            Ok(value) => {
                n = value;
                data.push(n);
            }
            Err(_) => {
                println!("Valor invalido, vuelva a intentarlo.");
            }
        }
    }
    data
}

fn greater(data: Vec<u8>) -> Result<u8, bool> {
    let n: u8;
    let count: u8;
    n = *data.iter().max().unwrap();
    count = data.iter().filter(|&&x| x == n).count() as u8;
    if count > 1 {
        Err(false)
    } else {
        Ok(n)
    }
}

fn main() {
    let data: Vec<u8> = input_number("Ingrese el numero");
    match greater(data) {
        Ok(n) => println!("El numero mayor estricto es: {}.", n),
        Err(_) => println!("No hubo numero mayor estricto."),
    }
}
