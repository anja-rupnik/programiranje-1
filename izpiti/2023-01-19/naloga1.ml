(* 1. a) *)
let permutacije a b c=
  [(a,b,c);(a,c,b)]
(* 1. b) *)
let rec zip_opt lst1 lst2=
  match lst1, lst2 with
  |[], [] -> []
  |[], x::xs -> (None, Some x):: (zip_opt [] xs)
  |x::xs, [] -> (Some x, None):: (zip_opt xs [])
  |x::xs, y::ys -> (Some x, Some y)::(zip_opt xs ys)


(* 1. c) *)
let rec zip_default lst1 lst2 a b=
  match lst1, lst2 with
  |[], [] -> []
  |[], x::xs -> (a, x):: (zip_default [] xs a b)
  |x::xs, [] -> (x, b):: (zip_default xs [] a b)
  |x::xs, y::ys -> (x, y)::(zip_default xs ys a b)
(* 1. d) *)

type response = Left | Middle | Right

let distribute f lst =
  let rec aux l r m lst=
  match lst with
  |[] -> (List.rev l, List.rev m, List.rev r)
  |x:: xs when f x == Left -> aux (x::l) r m xs
  |x:: xs when f x == Middle -> aux  l r (x::m) xs
  |x:: xs -> aux l (x::r) m xs
in
aux [] [] [] lst


(* 1. e) *)

type ('a, 'b) sum = Left of 'a | Right of 'b

let iso1 f =
  (fun x -> f (Left x)), (fun x -> f (Right x))

let iso2 (f, g) = function
|Left x -> f x
|Right x -> g x

