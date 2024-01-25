(* 1. a) *)
let vzporedna (x1,y1) (x2,y2) =
  x1/y1 == x2/y2

(* 1. b) *)
let rec zlozi_pocez l1 l2 =
  match l1, l2 with
  |[], [] -> []
  |x::x1::xs, y::y1::ys -> (x, y1)::(x1, y)::zlozi_pocez xs ys
(* 1. c) *)
let kompozitum f a =
  let rec aux a g =
  match a with
  |0 -> []
  |a -> (fun g -> f g) :: aux (a-1) (fun g -> f g)
  in
  aux a (fun x -> x)
(* 1. d) *)

(* 1. e) *)
