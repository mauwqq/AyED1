/*
Un comercio de electrodomésticos necesita para su línea de cajas un programa
que le indique al cajero el cambio que debe entregarle al cliente. Para eso
se ingresan dos números enteros, correspondientes al total de la compra y al
dinero recibido. Informar cuántos billetes de cada denominación deben ser
entregados como vuelto, de tal forma que se minimice la cantidad de billetes.
Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10.
Emitir un mensaje de error si el dinero recibido fuera insuficiente o si el
cambio no pudiera entregarse debido a falta de billetes con denominaciones
adecuadas. Ejemplo: Si la compra es de $3170 y se abona con $5000, el vuelto
debe contener 1 billete de $1000, 1 billete de $500, 1 billete de $200,
1 billete de $100 y 3 billetes de $10.
*/

use std::io;

struct Atm {
    b5000: u32,
    b1000: u32,
    b500: u32,
    b200: u32,
    b100: u32,
    b50: u32,
    b10: u32,
}

fn ask_input(message: String) -> u32 {
    loop {
        let mut input: String = String::new();
        println!("{}", message);
        io::stdin().read_line(&mut input).expect("Error al leer el input.");
        match input.trim().parse() {
            Ok(num) => {
                if num > 0 {
                    return num;
                } else {
                    println!("Debe ingresar un numero positivo.");
                }
            },
            Err(_) => {
                println!("Ingrese un numero valido.");
            }
        };
    }
}

fn enough_money(total: u32, money_received: u32) -> bool {
    if money_received >= total {
        true
    } else {
        false
    }
}

fn calculate_change(received: u32, total: u32, atm: &mut Atm) -> Vec<u32>{
    if received == total {
        return vec![0,0];
    }
    let mut change: u32 = received - total;
    atm.b5000 = change / 5000;
    let mut rest: u32 = change % 5000;
    atm.b1000 = rest / 1000;
    rest %= 1000;
    atm.b500 = rest / 500;
    rest %= 500;
    atm.b200 = rest / 200;
    rest %= 200;
    atm.b100 = rest / 100;
    rest %= 100;
    atm.b50 = rest / 50;
    rest %= 50;
    atm.b10 = rest / 10;
    rest %= 10;
    return vec![change, rest];
}

fn print_results(atm: &atm, total: i32, change: u32, rest: u32) {

}

fn main() {
    let mut atm = Atm {0,0,0,0,0,0,0};
    let total: u32 = ask_input("Ingrese el monto total a pagar: ".to_string());
    let received: u32 = ask_input("Ingrese el dinero suministrado: ".to_string());
    let mut change: Vec<u32> = calculate_change(received, total, &mut atm);
}