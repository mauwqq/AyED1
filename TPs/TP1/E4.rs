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

#[derive(Default)]
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
    let change: u32 = received - total;
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

fn print_results(atm: &Atm, total: u32, change: u32, rest: u32, received: u32) {
    if rest > 0 {
        println!("El cambio no puede ser entregado debido a falta de billetes con denominacion adecuada.");
    } else {
        println!("La compra fue de: ${}.", total);
        println!("El monto recibido fue de: ${}.", received);
        if change == 0 {
            println!("No hay vuelto.");
        } else {
            println!("El vuelto es de: ${}.", change);
            if atm.b5000 > 0 { println!("Billetes de 5000: {}.", atm.b5000)};
            if atm.b1000 > 0 { println!("Billetes de 1000: {}.", atm.b1000)};
            if atm.b500 > 0 { println!("Billetes de 500: {}.", atm.b500)};
            if atm.b200 > 0 { println!("Billetes de 200: {}.", atm.b200)};
            if atm.b100 > 0 { println!("Billetes de 100: {}.", atm.b100)};
            if atm.b50 > 0 { println!("Billetes de 50: {}.", atm.b50)};
            if atm.b10 > 0 { println!("Billetes de 10: {}.", atm.b10)};
        }
    }
}

fn main() {
    let mut atm = Atm::default();
    let total: u32 = ask_input("Ingrese el monto total a pagar: ".to_string());
    let received: u32 = ask_input("Ingrese el dinero suministrado: ".to_string());
    if !enough_money(total, received) {
        println!("No hay suficiente dinero para pagar la compra.");
    } else {
        let change: Vec<u32> = calculate_change(received, total, &mut atm);
        print_results(&atm, total, change[0], change[1], received);
    }
}