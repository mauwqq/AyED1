/*
La función de Ackermann A(m,n) se define de la siguiente forma:
n+1                 si m = 0
A(m-1,1)            si n = 0
A(m-1,A(m,n-1))     de otro modo
Imprimir un cuadro con los valores que adopta la función para valores de
m entre 0 y 3 y de n entre 0 y 7.
*/


fn ackermann(m: i64, n: i64) -> i64{
    /* */
    if m < 0 || n < 0 {
        println!("The numbers must be positive.");
        return -1;
    } else if m == 0 {
        return n + 1;
    } else if n == 0 {
        return ackermann(m - 1, 1);
    } else {
        return ackermann(m - 1, ackermann(m, n - 1));
    }
}

fn print_result<I64>(results: &Vec<i64>) {
    print!("\t");
    for i in 0..=3 {
        print!("{}\t", i);
    }
    println!("\n____________________________________");
    for i in 0..=7 {
        print!("{}|\t", i);
        for j in 0..=3 {
            let result = results[i * 4 + j];
            print!("{}\t", result);
        }
        println!();
    }
}

fn main() {
    /* Main function of program */
    let mut result = Vec::new();
    for j in 0..=7 {
        for i in 0..=3 {
            result.push(ackermann(i, j))
        }
    }
    print_result::<i64>(&result);
}