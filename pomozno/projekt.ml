type vrednostt = {
  oznaka : string
}

type tocka = {
    oznaka : string;
    vrednost : int;
    okolica : tocka list
}

let poskus =
    let a = {oznaka = "a"; vrednost = 1; okolica = [b; c]}
    and b = {oznaka = "b"; vrednost = 0; okolica = [a; d]}
    and c = {oznaka = "c"; vrednost = 1; okolica = [a; d]}
    and d = {oznaka = "d"; vrednost = 1; okolica = [b; c]}
    in
    let rec sestej k = function
        |[] -> k
        |x :: xs -> sestej (x.vrednost + k) xs
    in
    let funkcija t = {
      t with vrednost = sestej t.vrednost t.okolica
      }
    {
        zacetno_stanje_grid = [a; b; c; d]
                
    }
let korak avt = avt with zacetno_stanje = 
