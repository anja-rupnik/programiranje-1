type 'a list_tree = Leaf of 'a | Node of 'a list_tree list

(* 1. a) *)

let rec map f = function
  |Leaf a -> Leaf (f a)
  |Node lst -> Node (List.map (map f) lst)

(* 1. b) *)

let count tree =
  let rec aux i tree =
    match tree with
    |Leaf a -> i + 1
    |Node lst -> List.fold_left aux i lst
  in
  aux 0 tree



(* 1. c) *)

let rec apply ftree tree =
  match ftree, tree with
  |Leaf f, Leaf a -> Leaf (f a)
  |Node flst, Node lst -> Node (List.map2 apply flst lst)
  |_ -> failwith "no"

(* 1. d) *)

let rec combine t1 t2 =
  match t1, t2 with
  |Leaf f, Leaf g -> Leaf (fun x -> f(g x))
  |Node flst, Node lst -> Node (List.map2 combine flst lst)
  |_ -> failwith "no"


(* 1. e) *)




let t1 = Node [ Node [ Leaf (fun x -> x) ]; Leaf (fun x -> x * 2) ]
let t2 = Node [ Leaf 1; Leaf 2 ]
let t3 = Node [ Node []; Leaf 2; Leaf 4 ]
let t4 = Node [ Node [ Leaf (fun x -> x) ]; Leaf (fun x -> x * 2) ]
let t5 = Node [ Node []; Leaf 2; Leaf 4 ]
